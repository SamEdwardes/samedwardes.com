---
title: Replacing pip with uv for Python projects
authors: sedwardes
tags: [python, kubernetes]
keywords:
    - python
    - uv
    - pip
draft: false
---

import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

uv is "an extremely fast Python package installer and resolver, written in Rust" from <https://astral.sh>. Recently, I have started using uv in my day-to-day Python workflows. After a few weeks of usage I am sold! uv will be my go-to package manager for Python projects moving forward. It is MUCH faster than pip and I really like the new workflow it provides me with `uv pip compile` and `uv pip sync`.

## TL/DR

I am now using `uv` instead of `pip` for most of my projects. My workflow looks like this:

```bash
alias uvinit='uv venv && source .venv/bin/activate'
alias uvsync='uv pip compile requirements.in --quiet --output-file requirements.txt && uv pip sync requirements.txt'

uvinit
echo "pandas" > requirements.in
uvsync
```

<!--truncate-->

## Why uv?

For all of my future projects I plan to use uv because:

- uv is much faster than pip.
- uv pip compile and uv pip sync are a better workflow for managing dependencies.
- uv enforces best practices by forcing you to use virtual environments.

There is one exception. For package development, I plan to still use poetry (<https://python-poetry.org>) because it some features that are specific to package development that uv does not have (e.g. like `poetry publish`).

## Install uv

See <https://github.com/astral-sh/uv> for more details.

```bash
# On macOS and Linux.
curl -LsSf https://astral.sh/uv/install.sh | sh

# On Windows.
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```

## Workflow comparison

### Creating a virtual environment


<Tabs groupId="workflow">
<TabItem value="uv" label="uv">

```bash
uv venv
```

</TabItem>
<TabItem value="pip" label="pip">

```bash
python -m venv .venv
source .venv/bin/activate
pip install --upgrade pip wheel setuptools
```

</TabItem>
</Tabs>


### Installing first package

Define your initial requirements.

```bash showLineNumbers title="requirements.in"
pandas
```

Then install the requirements and the transitive dependencies.

<Tabs groupId="workflow">
<TabItem value="uv" label="uv">

```bash
# Identify all transitive dependencies and create requirements.txt
uv pip compile requirements.in --quiet --output-file requirements.txt

# Update environment to match requirements.txt
uv pip sync requirements.txt
```

</TabItem>
<TabItem value="pip" label="pip">

```bash
# Install all packages in requirements.in and the transitive dependencies
pip install -r requirements.in
```

</TabItem>
</Tabs>


### Adding new packages

Update requirements.in to include the additional packages you want to install.

```bash showLineNumbers title="requirements.in"
pandas
rich
htmx
```

Then install the new packages and the transitive dependencies.

<Tabs groupId="workflow">
<TabItem value="uv" label="uv">

```bash
# Identify all transitive dependencies and create requirements.txt
uv pip compile requirements.in --quiet --output-file requirements.txt

# Update environment to match requirements.txt
uv pip sync requirements.txt
```

</TabItem>
<TabItem value="pip" label="pip">

```bash
pip install -r requirements.in
```

</TabItem>
</Tabs>


### Removing packages

Up until now, other than the speed improvements it may not be obvious why uv is better than pip. Lets say we want to remove the pandas package from our project. This is an area where uv really shines. With uv, we can remove the package from requirements.in and run `uv pip compile` and `uv pip sync` to update our environment.

With pip, we need to remove the package from requirements.txt and delete the current virtual environment,and then re-create it. If you were to use `pip uninstall pandas`, it would remove pandas from our environment, but not all of the transitive dependencies that pandas brought in that we no longer require.

```bash showLineNumbers title="requirements.in"
rich
htmx
```

<Tabs groupId="workflow">
<TabItem value="uv" label="uv">

```bash
# Identify all transitive dependencies and create requirements.txt
uv pip compile requirements.in --quiet --output-file requirements.txt

# Update environment to match requirements.txt
uv pip sync requirements.txt
```

</TabItem>
<TabItem value="pip" label="pip">

```bash
# Deactivate the current virtual environment
deactivate

# Delete the virtual environment
rm -rf .venv

# Recreate the virtual environment
python -m venv .venv
source .venv/bin/activate
pip install --upgrade pip wheel setuptools

# Install all the packages again
pip install -r requirements.txt
```

</TabItem>
</Tabs>

## Using aliases

It is true that for parts of the workflow using uv requires more typing. I have found these two aliases to be very helpful in my workflow.

```bash
alias uvinit='uv venv && source .venv/bin/activate'
alias uvsync='uv pip compile requirements.in --quiet --output-file requirements.txt && uv pip sync requirements.txt'
```

You can add these to your `.bashrc` or `.zshrc` file to make them available in all of your projects.

Now when I start a new project I run:

```bash
uvinit
```

Whenever I make a change to requirements.in I run:

```bash
uvsync
```