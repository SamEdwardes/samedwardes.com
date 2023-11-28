---
title: How to use 1Password for Secrets in ~/.bashrc or ~/.zshrc
authors: sedwardes
tags: [command line]
keywords:
    - 1password
    - cli
    - op
draft: false
---

:::tip Update
A new blog post has been written about this topic! Check out [How to use 1Password for Secrets in ~/.bashrc or ~/.zshrc (UPDATE)](../2023-11-28-1password-for-secret-dotfiles-update/index.md).
:::

[1Password](https://1password.com) is a password manager. Over the years, I have tried LastPass, BitWarden, and 1Password. Out of the three, 1Password has been my favourite. The Mac app, browser extension, and IOS app are well-polished. One of my favourite parts about 1Password is the ability to access passwords using the [1Password CLI](https://developer.1password.com/docs/cli/).

## Using `op inject` for secrets

I recently discovered a pattern to use the 1Password CLI to store all of my secrets in my dotfiles:

```bash
# ~/.zshrc
op  inject --in-file "${HOME}/.dotfiles/secrets.zsh" | while read -r line; do
  eval "$line"
done
```

```bash
# ~/.dotfiles/secrets.zsh
export NOTION_API_KEY="op://private/notion.so/api-token"
export TEST_PYPI_TOKEN="op://private/test.pypi.org/token"
```

<!--truncate-->

Before the 1Password CLI, I used this pattern:

```bash
# ~/.zshrc
source "${HOME}/.dotfiles/secrets.zsh"
```

```bash
# ~/.dotfiles/secrets.zsh
export NOTION_API_KEY="XXXXX"
export TEST_PYPI_TOKEN="YYYYY"
```

There are a few downsides to this old approach:

- I must be careful with `~/.dotfiles/secrets.zsh`. It contains my real secrets!
- If I accidentally check it into git, that would be bad.
- If I lose the file, that would also suck. I would need to recreate all of my tokens.
- To use the secrets on other computers, I need to copy and paste the values.

Now, with 1Password, I can use 1Password as my source of truth for all of my API keys. If they change, I only need to update them in one place.

The only downside to my new approach is that I am now prompted to authenticate every time I start a new terminal session. But thanks to my MacBook's built-in touch ID, this is not too cumbersome.

## Other methods

It took me a few iterations to get to my current approach. At first, I tried using `op read`:

```bash
export NOTION_API_KEY=$(op read "op://private/notion.so/api-token)
```

This worked but was much slower. In my actual secrets file, I have about 40 items. Running `op read` 40 times could take 5-10 seconds.

Using `op inject` gets around this by only running the `op` CLI once. The `~/.dotfiles/secrets.zsh` also looks cleaner this way. The downside is that the `~/.zshrc` file becomes more complicated with the `eval` loop.
