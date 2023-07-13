---
title: How to use pyenv with reticulate
authors: sedwardes
tags: [python, r]
keywords:
    - reticulate
    - pyenv
    - R
    - python
draft: false
---

The [reticulate](https://rstudio.github.io/reticulate/) package allows you to execute Python code from R. If you use [pyenv](https://github.com/pyenv/pyenv) to install Python the default options will not work with reticulate.

<!--truncate-->

For example:

```R
Sys.setenv(RETICULATE_PYTHON="/Users/samedwardes/.pyenv/versions/3.11.1/bin/python")
library("reticulate")
py_discover_config()
# python:         /Users/samedwardes/.pyenv/versions/3.11.1/bin/python
# libpython:      [NOT FOUND]
# pythonhome:     /Users/samedwardes/.pyenv/versions/3.11.1:/Users/samedwardes/.pyenv/versions/3.11.1
# version:        3.11.1 (main, Jan  5 2023, 15:09:14) [Clang 14.0.0 (clang-1400.0.29.202)]
# numpy:          /Users/samedwardes/.pyenv/versions/3.11.1/lib/python3.11/site-packages/numpy
# numpy_version:  1.23.5

# NOTE: Python version was forced by RETICULATE_PYTHON
> os <- import("os")
# Error: Python shared library not found, Python bindings not loaded.
# Use reticulate::install_miniconda() if you'd like to install a Miniconda Python environment.
```

The problem is that when you install Python, you need to enable shared libraries. You can do this in pyenv with the following (see pyenv [docs](https://github.com/pyenv/pyenv/blob/master/plugins/python-build/README.md#building-with---enable-shared)):

```bash
env PYTHON_CONFIGURE_OPTS="--enable-shared" pyenv install 3.10.12
```

Now, if you use the new Python binary reticulate will work:

```R
Sys.setenv(RETICULATE_PYTHON="/Users/samedwardes/.pyenv/versions/3.10.12/bin/python")
library("reticulate")
py_discover_config()
# python:         /Users/samedwardes/.pyenv/versions/3.10.12/bin/python
# libpython:      /Users/samedwardes/.pyenv/versions/3.10.12/lib/libpython3.10.dylib
# pythonhome:     /Users/samedwardes/.pyenv/versions/3.10.12:/Users/samedwardes/.pyenv/versions/3.10.12
# version:        3.10.12 (main, Jul 13 2023, 09:53:58) [Clang 14.0.3 (clang-1403.0.22.14.1)]
# numpy:           [NOT FOUND]

# NOTE: Python version was forced by RETICULATE_PYTHON
os <- import("os")
os$listdir(".")
# [1] ".Renviron"        "requirements.txt" ".Rprofile"        "app.R"            ".venv"           
# [6] "app.Rproj"        "renv.lock"        "renv"             ".Rproj.user"
```