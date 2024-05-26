---
author: Sam Edwardes
date: 2023-10-12
description: Reticulate is an R library that lets you execute Python code from within R. Recently, I attempted to use reticulate to access numpy from Python. Numpy was installed, but I kept getting an error message.
keywords:
- r
- reticulate
- NumPy
- Python
tags:
- linux
- r
- data science
title: How to Fix renv Numpy Issues
---

[Reticulate](https://github.com/rstudio/reticulate) is an R library that lets you execute Python code from within R. Recently, I attempted to use reticulate to access numpy from Python. Numpy was installed, but I kept getting the following message:

```r
> reticulate::py_config()
python:         /usr/home/sam.edwardes/rstudio-demos/applications/shiny-for-r-with-reticulate/.venv/bin/python3
libpython:      /opt/python/3.10.11/lib/libpython3.10.so
pythonhome:     /usr/home/sam.edwardes/rstudio-demos/applications/shiny-for-r-with-reticulate/.venv:/usr/home/sam.edwardes/rstudio-demos/applications/shiny-for-r-with-reticulate/.venv
version:        3.10.11 (main, Jun  4 2023, 22:34:21) [GCC 11.3.0]
numpy:           [NOT FOUND]
```

<!--truncate-->

However, I know that numpy was installed:

```bash
$ .venv/bin/python3 -m pip list | grep numpy
numpy      1.26.0
```

After some investigation, I discovered that the `pip install numpy` was installing a binary version of numpy. Usually, this is good because it is much faster and more reliable than building numpy from source. But, for some reason, on my operating system (Ubuntu 22.04), reticulate could not find numpy. To solve the problem, I forced numpy to be installed from source:

```bash
$ .venv/bin/python3 -m pip install --force-reinstall --no-binary numpy numpy
```

It took several minutes to finish. After installing from source, reticulate was able to find numpy:

```r
> reticulate::py_config()
python:         /usr/home/sam.edwardes/rstudio-demos/applications/shiny-for-r-with-reticulate/.venv/bin/python3
libpython:      /opt/python/3.10.11/lib/libpython3.10.so
pythonhome:     /usr/home/sam.edwardes/rstudio-demos/applications/shiny-for-r-with-reticulate/.venv:/usr/home/sam.edwardes/rstudio-demos/applications/shiny-for-r-with-reticulate/.venv
version:        3.10.11 (main, Jun  4 2023, 22:34:21) [GCC 11.3.0]
numpy:          /usr/home/sam.edwardes/rstudio-demos/applications/shiny-for-r-with-reticulate/.venv/lib/python3.10/site-packages/numpy
numpy_version:  1.26.0
numpy:          /usr/home/sam.edwardes/rstudio-demos/applications/shiny-for-r-with-reticulate/.venv/lib/python3.10/site-packages/numpy
```

I can now use numpy from within my R script:

```r
> library(reticulate)
> np <- import("numpy")
> np$array(c(1, 2, 3))
[1] 1 2 3
```