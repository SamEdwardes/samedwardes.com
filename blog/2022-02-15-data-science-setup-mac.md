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
brew install --cask iterm2

# Fonts
# brew tap homebrew/cask-fonts 
brew install --cask font-fira-code

# Install other tools

# Install apps via the app store
mas install 937984704  # Amphetamine
mas install 441258766  # Magnet
```

</details>

## Homebrew

Using a package manager is an easy to keep tools up to date, and forces a consistent approach for downloading and installing new tools. When ever possible, I try to `brew` install tools / software using [**Homebrew**](https://brew.sh/). To install homebrew run the following command:

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

Throughout this blog post we will use `brew install` where ever possible to install our tools.

## Terminal

Every nerds favourite place to be... the terminal. As a data scientist / developer your terminal setup is a great way to express yourself. Do you like to get crazy and customize everything? Do you keep it simple and stick to the defaults? I like to take a middle ground approach. I want things to look pretty, but I also do not want to waste too much time configuring things.

### iTerm2

[iTerm2](https://iterm2.com/index.html) is a replacement for the default terminal app that comes with your mac. It includes some nice features such as tabs and split panes.

![iterm2-screenshot](https://iterm2.com/img/screenshots/split_panes.png)

*Image from https://iterm2.com/features.html*

To install run the following command:

```bash
brew install --cask iterm2
```

### Starship

[starship](https://starship.rs/) is a cross-shell prompt. According to their website:

> The minimal, blazing-fast, and infinitely customizable prompt for any shell!

![starship-gif](https://raw.githubusercontent.com/starship/starship/master/media/demo.gif)

*Gif from https://starship.rs/guide/*

I really like starship because:

- I think the defaults look good and are reasonable.
- I can easily have a consistent prompt across all of my devices.
- When needed, starship also has lots of customization options.

To install starship run the following command:

```bash
brew install starship
```

## Command line tools

### exa

https://the.exa.website/ a modern replacement for `ls`. It has defaults that I prefer, and has a nice coloured output.

![exa-image](https://github.com/ogham/exa/raw/master/screenshots.png)

*Image from https://github.com/ogham/exa*

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

## Apps

### Docker desktop

```bash
brew install --cask docker
```

### Typora

## Fonts

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

### Python packages

Below is a collection of my favourite Python packages.

```bash
# Data
pip install pandas

# Nautal langague processing (NLP)
pip install spacy

# Visualization
pip install

# Fun stuff
pip install rich         # Beautiful command line outputs
pip install typer        # Create command line applications
```

## R

### Installing R

Install the latest version of R from CRAN:

![cran-homepage](https://imgur.com/kLHQ02Q.png)

*Select "Download R for macOS.*

![download-correct-version-of-r](https://imgur.com/y4akbAT.png)

*If you are using a newer Mac with an M1 chip select the second option for **Apple silicon arm64**. Otherwise, choose the first option for **Intel 64-bit**.*

![installer-r](https://imgur.com/sbOiv8K.png)

*Click on the link and follow the instructions as prompted. Select all of the default configuration options.*

### RStudio

If you use R, you are probably already using RStudio.

### R packages

Below is a collection of my favourite R packages.

```r
install.packages("tidyverse")
```

#### Tidyverse

The tidyverse is a collection of packages that follow a common design language. The tidyverse is my favourite part of R!

## Inspiration and reference

I have referenced and used the below guides many times. Check them out for additional inspiration and ideas on how to create your perfect data science setup.

- [Modern Python Developers Toolkit](https://pycon.switowski.com/) by Sebastian Witowski.
- [UBC MDS software stack](https://ubc-mds.github.io/resources_pages/install_ds_stack_mac/).

