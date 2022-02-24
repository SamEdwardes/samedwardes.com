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

# Install python tools
curl https://pyenv.run | bash
curl -sSL https://install.python-poetry.org | python3 -

# Install cli tools with Homebrew
brew install just
brew install starship
brew install git
brew install gh
brew install pyenv
brew install mas
brew install exa
brew install bat
brew install xclip

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


## Python

Search *how to install python* on Google and you will find many differing opinions. My current approach is:

- Use pyenv to manage my python versions (e.g. enables me to have both Python `3.9` and `3.10` on my computer).
- Use venv for creating virtual environments.
- Use poetry for managing dependencies in projects.
- Use pipx to install system wide packages and command line tools.

### pyenv

#### Installation

pyenv ([https://github.com/pyenv/pyenv](https://github.com/pyenv/pyenv)) allows you to manage multiple versions of Python on your computer. To install I like to use the pyenv install script from [https://github.com/pyenv/pyenv-installer](https://github.com/pyenv/pyenv-installer):

```bash
curl https://pyenv.run | bash
```

The script install "*pyenv and friends*" which includes:

- pyenv
- pyenv-doctor
- pyenv-installer
- pyenv-update
- pyenv-virtualenv
- pyenv-which-ext

#### Using pyenv

Now that pyenv is installed, you can start to install different versions of python. Check all of the available versions using the `pyenv install --list` command:

```bash
pyenv install --list
```

```bash
Available versions:
  2.1.3
  2.2.3
  ...
  3.9.1
  3.9.2
  3.9.4
  3.9.5
  3.9.6
  3.9.7
  3.10.0
  ...
```

As of writing this blog post `3.10.0` is the most current version of Python. You can install it using:

```bash
pyenv install 3.10.0
```

And then validate that the installation worked:

```bash
pyenv versions
```

```bash
  system
  3.10.0
  3.7.10
* 3.9.4 (set by /Users/samedwardes/.pyenv/version)
```

#### Global pyenv

I want to make the latest version of Python as my default. To do so I run the following command:

```bash
pyenv global 3.10.0
pyenv versions
```

```bash
  system
* 3.10.0 (set by /Users/samedwardes/.pyenv/version)
  3.7.10
  3.9.4
```

#### Local pyenv

For some projects I may want to use a different version of Python then my default `3.10.0`. To change the default version for a specific project I can use the `local` command.

```bash
mkdir old-py-project
cd old-py-project
pyenv local 3.7.10
pyenv versions
```

```bash
  system
  3.10.0
* 3.7.10 (set by /Users/samedwardes/tmp/old-py-project/.python-version)
  3.9.4
```

As soon as I navigate away from the project, my python version changes back to my global default.

```bash
cd ..
pyenv versions
```

```bash
  system
* 3.10.0 (set by /Users/samedwardes/.pyenv/version)
  3.7.10
  3.9.4
```

### venv

#### Creating a new virtual environment

`venv` comes built into Python. It is used to create virtual environments. Every time I start a new project I create a new virtual environment. Lets demonstrate by creating a new project:

```bash
mkdir toy-project
cd toy-project
```

To create a new virtual environment run the following command:

```bash
python -m venv venv
```

Lets break down the command above:

- `python -m venv` runs the `venv` program from the command line.
- The last part of the command, the second `venv` is the positional argument for `ENV_DIR`. Run `python -m venv --help` to see all the arguments and options for the `venv program.
- By convention, I always name the `ENV_DIR` as `venv`. However, you can name it anything you like (e.g. `python -m venv my-virtual-environment` would also work).

The `python -m venv venv` create a new directory in our current project named `venv`. Lets take a look inside:

```bash
tree venv -L 2
```

```bash
venv
├── bin
│   ├── Activate.ps1
│   ├── activate
│   ├── activate.csh
│   ├── activate.fish
│   ├── pip
│   ├── pip3
│   ├── pip3.10
│   ├── python -> /Users/samedwardes/.pyenv/versions/3.10.0/bin/python
│   ├── python3 -> python
│   └── python3.10 -> python
├── include
├── lib
│   └── python3.10
└── pyvenv.cfg
```

Inside the `venv/bin/` directory are several files and scripts. These are used to activate the virtual environment. Run the following command to activate your virtual environment:

```bash
source venv/bin/activate
```

If you are using [starship](https://starship.rs/) your command line will now have a nice indicator letting you know that you are using a virtual environment:

```bash
~/tmp/toy-project via 🐍 pyenv 3.10.0 (venv)
```

You can prove to yourself that you are in a brand new isolated Python environment by running:

```bash
pip list
```

```bash
Package    Version
---------- -------
pip        21.2.3
setuptools 57.4.0
WARNING: You are using pip version 21.2.3; however, version 22.0.3 is available.
You should consider upgrading via the '/Users/samedwardes/tmp/toy-project/venv/bin/python -m pip install --upgrade pip' command.
```

Nice! You have a brand new canvas to start  your next python project on. While the virtual environment is activated, anything you pip install will only be installed into the virtual environment.

First I will update pip to the most current version.

```bash
python -m pip install --upgrade pip
```

Then lets install a package:

```bash
pip install wheel
pip list
```

```bash
Package    Version
---------- -------
pip        22.0.3
setuptools 57.4.0
wheel      0.37.1
```

#### Using with pyenv

When you run the command `python -m venv venv` the virtual environment will automatically be created using which ever version of python you currently have activated. If you are unsure, run the following command to check before creating a new virtual environment:

```bash
pyenv versions
```

```bash
  system
* 3.10.0 (set by /Users/samedwardes/.pyenv/version)
  3.7.10
  3.9.4
```

I can see that Python `3.10.0` is currently active. I can double check by just running:

```bash
python --version
```

```bash
Python 3.10.0
```

If I want to create my virtual environment using a different python version I must first activate the other version using pyenv:

```bash
pyenv local 3.9.4
```

Then I can create my virtual environment:

```bash
python -m venv venv-394
```

Lets compare the two different virtual environments we created:

```bash
tree -L 3
```

```bash
.
├── venv
│   ├── bin
│   │   ├── Activate.ps1
│   │   ├── activate
│   │   ├── activate.csh
│   │   ├── activate.fish
│   │   ├── pip
│   │   ├── pip3
│   │   ├── pip3.10
│   │   ├── python -> /Users/samedwardes/.pyenv/versions/3.10.0/bin/python
│   │   ├── python3 -> python
│   │   ├── python3.10 -> python
│   │   └── wheel
│   ├── include
│   ├── lib
│   │   └── python3.10
│   └── pyvenv.cfg
└── venv-394
    ├── bin
    │   ├── Activate.ps1
    │   ├── activate
    │   ├── activate.csh
    │   ├── activate.fish
    │   ├── easy_install
    │   ├── easy_install-3.9
    │   ├── pip
    │   ├── pip3
    │   ├── pip3.9
    │   ├── python -> /Users/samedwardes/.pyenv/versions/3.9.4/bin/python
    │   ├── python3 -> python
    │   └── python3.9 -> python
    ├── include
    ├── lib
    │   └── python3.9
    └── pyvenv.cfg

10 directories, 25 files
```

You can see that the first one we created (`venv`) is using `python3.10`, and the second one we created (`venv-394`) is using `python3.9`.

#### venv vs. pyenv

When I first started using these tools I would often get mixed up. What is venv doing? What is pyenv doing? Do I need both?

- `pyenv` controls your python version (e.g. 3.10 vs. 3.9).
- `venv` isolates your project dependencies (the things you pip install).

### poetry

poetry is a tool for python dependency management and packing. From their website [https://python-poetry.org/](https://python-poetry.org/):

> *Python packaging and dependency management made easy*

#### Installation

To install poetry run the following command:

```bash
curl -sSL https://install.python-poetry.org | python3 -
```

Follow the instructions from the terminal output to configure poetry. For me, I added the following line to my `~/.zshrc` file:

```bash title="~/.zshrc"
export PATH="$HOME/.poetry/bin:$PATH"
```

Verify that the installation worked by running:

```bash
poetry --version
```

```bash
Poetry version 1.1.12
```

#### Starting a new project with poetry

I use poetry for almost every new project that I start. Lets create an example project to demonstrate:

```bash
mkdir new-project
cd new-project
poetry init -n    # The `-n` flag tells poetry to not ask any questions interactively.
tree
```

```bash
.
└── pyproject.toml

0 directories, 1 file
```

Your directory now has a new file, *pyproject.toml*. This file is used to keep track of the dependencies required for your project.

```bash
cat pyproject.toml
```

```toml
[tool.poetry]
name = "new-project"
version = "0.1.0"
description = ""

[tool.poetry.dependencies]
python = "^3.9"

[tool.poetry.dev-dependencies]

[build-system]
requires = ["poetry-core>=1.0.0"]
build-backend = "poetry.core.masonry.api"
```

Go ahead and manually update the projects description in *pyproject.toml*. Too add a dependency use the `poetry add` command. When using poetry this command essentially replaces `pip install`. When you use `poetry add` a few things happen:

- The new package is added to your *pyproject.toml* file.
- The poetry dependency resolver verifies the version requirements.
- A virtual environment is created by poetry.

```bash
poetry add requests
```

```bash
Creating virtualenv new-project-ubTVXCow-py3.9 in /Users/samedwardes/Library/Caches/pypoetry/virtualenvs
Using version ^2.27.1 for requests

Updating dependencies
Resolving dependencies... (3.1s)

Writing lock file

Package operations: 5 installs, 0 updates, 0 removals

  • Installing certifi (2021.10.8)
  • Installing charset-normalizer (2.0.12)
  • Installing idna (3.3)
  • Installing urllib3 (1.26.8)
  • Installing requests (2.27.1)
```

Take a look at your project, you will notice a new file:

```bash
tree
```

```bash
.
├── poetry.lock
└── pyproject.toml

0 directories, 2 files
```

The new *poetry.lock* file contains a detailed description of all the packages you are using (this includes requests, and all of the packages that requests depends on). The *pyproject.toml* file has been automatically updated to include requests as a dependency.

```bash
cat pyproject.toml
```

```toml
[tool.poetry]
name = "new-project"
version = "0.1.0"
description = ""
authors = ["SamEdwardes <edwardes.s@gmail.com>"]

[tool.poetry.dependencies]
python = "^3.9"
requests = "^2.27.1"

[tool.poetry.dev-dependencies]

[build-system]
requires = ["poetry-core>=1.0.0"]
build-backend = "poetry.core.masonry.api"
```

#### Using the poetry virtual environment

In order to isolate your package poetry creates a virtual environment. To access this virtual environment you can prefix any command with `poetry run` and it will run inside the virtual environment.

```bash
poetry run pip list
```

```bash
Package            Version
------------------ ---------
certifi            2021.10.8
charset-normalizer 2.0.12
idna               3.3
pip                21.3.1
requests           2.27.1
setuptools         58.3.0
urllib3            1.26.8
wheel              0.37.0
```

It can be annoying to prefix every command with `poetry run`. Alternatively, you can run all commands in the poetry virtual environment with `poetry shell`.

```bash
poetry shell
pip list
```

```bash
Package            Version
------------------ ---------
certifi            2021.10.8
charset-normalizer 2.0.12
idna               3.3
pip                21.3.1
requests           2.27.1
setuptools         58.3.0
urllib3            1.26.8
wheel              0.37.0
```

#### Adding development dependencies

When creating a python package it is common that you as the developer will need a particular package (e.g. like [black](https://github.com/psf/black) for code formatting), but that the end user will not require that same package to run the program. poetry has a mechanism to handle this by allowing you to specify development dependencies with the `--dev` option.

```bash
poetry add --dev black
cat pyproject.toml
```

<details>
<summary><i>show output</i></summary>

```toml
[tool.poetry]
name = "new-project"
version = "0.1.0"
description = ""
authors = ["SamEdwardes <edwardes.s@gmail.com>"]

[tool.poetry.dependencies]
python = "^3.9"
requests = "^2.27.1"

[tool.poetry.dev-dependencies]
black = "^22.1.0"

[build-system]
requires = ["poetry-core>=1.0.0"]
build-backend = "poetry.core.masonry.api"
```

</details>

As you can see, black has been added as *dev-dependency*. When you publish your package to PyPi it will not include black as a requirement, but it will include requests.

### poetry vs venv

It may not be clear when you should use poetry, vs. when you should us venv. There is not correct answer, but in general I use **poetry** when:

- I am creating a python package that I will share with others via PyPi and/or GitHub.

I use **venv** when:

- I do not think that I will be sharing the code with anyone.
- I want to quickly experiment

If you are unsure about which tool to use, just choose one and get started! You can always change your mind later on the. The important thing is that you are using a virtual environment!

### pipx



### Python packages

Below is a collection of my favourite Python packages.

```bash
# Data
pip install pandas

# Natural language processing (NLP)
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

## Inspiration and reference

I have referenced and used the below guides many times. Check them out for additional inspiration and ideas on how to create your perfect data science setup.

- [Modern Python Developers Toolkit](https://pycon.switowski.com/) by Sebastian Witowski.
- [UBC MDS software stack](https://ubc-mds.github.io/resources_pages/install_ds_stack_mac/).

