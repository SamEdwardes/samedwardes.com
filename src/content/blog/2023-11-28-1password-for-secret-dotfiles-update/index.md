---
author: Sam Edwardes
date: 2023-11-28
description: An update on how I managed my secretes in the terminal with 1Password.
keywords:
- 1password
- cli
- op
tags:
- command line
title: How to use 1Password for Secrets in ~/.bashrc or ~/.zshrc (UPDATE)
---

At the start of the month I wrote a blog post about how to use 1Password for managing all of your secrets on the command line: [How to use 1Password for Secrets in ~/.bashrc or ~/.zshrc](/blog/2023-11-03-1password-for-secret-dotfiles/). After 1 month of using this approach in the wild, I have a few updates.

My primary problem was that it was very annoying to authenticate every time I opened a new terminal session. But... liked the idea of using 1Password to store all of my secrets, and not copying and pasting secrets into my startup scripts.

After some experimentation, I found a compromise that works for me.

```bash
export DOTFILES_DIR="${HOME}/.dotfiles"

# If zhs/secrets-out.zsh does not exist, create it.
secrets_out_path="${DOTFILES_DIR}/zsh/secrets-out.zsh"

if [ ! -f "$secrets_out_path" ]; then
    echo "Creating ${secrets_out_path}..."
    op --account "my.1password.com" inject --in-file "${DOTFILES_DIR}/zsh/secrets-in.zsh"  --out-file "${DOTFILES_DIR}/zsh/secrets-out.zsh"
fi

# Check to see that if after removing everything to the right of `=` in
# zsh/secrets-in.zsh and zsh/secrets-out.zsh, the files are the same. If they
# are the same do nothing. If the are different create an updated version of
# zsh/secrets-out.zsh.
secrets_in_no_values=$(cat "${DOTFILES_DIR}/zsh/secrets-in.zsh" | sed 's/=.*//' | base64)
secrets_out_no_values=$(cat "${DOTFILES_DIR}/zsh/secrets-out.zsh" | sed 's/=.*//' | base64)

if [ ! "$secrets_in_no_values" = "$secrets_out_no_values" ]; then
    echo "Secrets have changed... Updating ${secrets_out_path}"
    rm "${DOTFILES_DIR}/zsh/secrets-out.zsh"
    op --account "my.1password.com" inject --in-file "${DOTFILES_DIR}/zsh/secrets-in.zsh"  --out-file "${DOTFILES_DIR}/zsh/secrets-out.zsh"
fi
```

- In the previous version, the `op inject` command was run every time I opened a new terminal session, which required me to authenticate every session.
- Now, the `op inject` command is only run when the `zsh/secrets-out.zsh` file does not exist, or when the `zsh/secrets-in.zsh` file has changed. Only in one of those two circumstances will I be prompted to authenticate.

This approach does introduce a new downside however. There is now a file on my disk `"${DOTFILES_DIR}/zsh/secrets-out.zsh"` that stores secrets in plain text (similar to what I did before). But now that I am using 1Password to manage this file I do not need to manually update this file.

I also created an alias so I can manually update the secrets if I need to. For example if I were to change a password in 1Password.

```bash
alias update-secrets='rm "${DOTFILES_DIR}/zsh/secrets-out.zsh" && op --account "my.1password.com" inject --in-file "${DOTFILES_DIR}/zsh/secrets-in.zsh"  --out-file "${DOTFILES_DIR}/zsh/secrets-out.zsh" && source "${DOTFILES_DIR}/zsh/secrets-out.zsh"'
```