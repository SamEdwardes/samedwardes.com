---
title: The Ultimate Data Science Setup for Mac (2022 update)
authors: sedwardes
tags: [data science, mac]
---

:::caution

This blog post is a work in progress and will be updated!

:::

You may think I am crazy, but I really enjoy setting up my computer. I am the kind of person who likes to wipe their computer clean every so often and start fresh with a clean slate. This blog post is an update to an earlier [blog post](/2020/06/08/datascience-setup) from 2020. A lot has changed since then, so here is a look at my current setup. 

<!--truncate-->

## TL/DR

Feeling bold and want to completely clone my setup? Just run the following script:

<details>
<summary>setup.sh</summary>

```bash
# Install Homebrew
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Install cli tools with Homebrew
brew install just
brew install starship
brew install git
brew install gh
brew install pyenv
brew install mas
brew install exa
brew install bat

# Install others tools using Homebrew cask
brew install --cask docker

# Fonts
# brew tap homebrew/cask-fonts 
brew install --cask font-fira-code

# Install other tools

# Install apps via the app store
mas install 937984704  # Amphetamine
mas install 441258766  # Magnet
```

</details>

## Package managers

Using a package manager is an easy to keep tools up to date, and forces a consistent approach for downloading and installing new tools. When ever possible, I try to `brew` install tools / software using [**Homebrew**](https://brew.sh/). To install homebrew run the following command:

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

Throughout this blog post we will use `brew install` where ever possible to install our tools.

## Terminal

Every nerds favourite place to be... the terminal. As a data scientist / developer your terminal setup is a great way to express yourself. Do you like to get crazy and customize everything? Do you keep it simple and stick to the defaults? I like to take a middle ground approach. I want things to look pretty, but I also do not want to waste too much time configuring things.

### Iterm2

### Starship

[Starship.rs] 

## Developer tools

### exa

https://the.exa.website/ a modern replacement for `ls`.

```bash
brew install exa
```

### bat

https://github.com/sharkdp/bat

> A cat(1) clone with wings.

```bash
brew install bat
```

### just

From the [just repo](https://github.com/casey/just):

> `just` is a handy way to save and run project-specific commands.

`just` is very similar to the ubiquitous `make` command. It is inspired by `make`, but focuses on just being a command runner as opposed to a build tool. To install just run the following command:

```bash
brew install just
```

### Docker desktop

```bash
brew install --cask docker
```

### Typora

### Fonts



## VS Code

### Python plugins

### R plugins

## Python

Search *how to install python* on Google and you will find many differing opinions. My current approach is:

- Use pyenv to manage your python versions
- Use venv for creating virtual environments
- Use poetry for managing dependencies in projects
- Use pipx to install system wide packages and command line tools

### pyenv

### venv

### poetry

[https://python-poetry.org/](https://python-poetry.org/).

```bash
curl -sSL https://install.python-poetry.org | python3 -
```

### pipx

### Most used packages

#### typer

## R

## Inspiration and reference

I have referenced and used the below guides many times. Check them out for additional inspiration and ideas on how to create your perfect data science setup.

- [Modern Python Developers Toolkit](https://pycon.switowski.com/) by Sebastian Witowski.
- [UBC MDS software stack](https://ubc-mds.github.io/resources_pages/install_ds_stack_mac/).

