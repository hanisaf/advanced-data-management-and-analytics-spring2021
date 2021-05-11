# Plotnine

Plotnine is a Python package made for graphical analysis and an implementation of the `Grammer of Graphics`.

Contians callable object `ggplot` which is used for all created visualizations. 

This package is built with the following packages:
- `matplotlib`
- `pandas`
- `mizani`
- `statsmodels`
- `scipy`

For more information on the history and objective of plotnine, find this [here](https://plotnine.readthedocs.io/en/stable/about-plotnine.html).


## Presentation

The link to our presentation can be found [here](https://www.youtube.com/watch?v=fjcOOV8UsV8).

## Installation

Use the package installation [instructions](https://plotnine.readthedocs.io/en/stable/installation.html) to install plotnine.

```bash
$ pip install plotnine
```

## Summary of support files

- `plotnine.ipynb`: the notebook containing this tutorial code
- `surveys.csv`: a data file with surveys of different animals atrributes recorded

## Data Description

### Surveys Data
- `record_id`: Unique id for the observation
- `month`: month of observation
- `day`: day of observation
- `year`: year of observation
- `plot_id`: ID of a particular site
- `species_id`: 2-letter code
- `sex`: sex of animal (“M”, “F”)
- `hindfoot_length`: length of the hindfoot in mm
- `weight`: weight of the animal in grams

### Cars Data
- `mpg`: Miles/(US) gallon
- `cyl`: Number of cylinders
- `disp`: Displacement (cu.in.)
- `hp`: Gross horsepower
- `drat`: Rear axle ratio
- `wt`: Weight (1000 lbs)
- `qsec`: 1/4 mile time
- `vs`: V/S
- `am`: Transmission (0 = automatic, 1 = manual)
- `gear`: Number of forward gears
- `carb`: Number of carburetors

## Guide

This is the guide used in our presentation of [making plots with plotnine](https://datacarpentry.org/python-ecology-lesson/07-visualization-ggplot-python/index.html).

Here is the main documentation of the [plotnine package](https://plotnine.readthedocs.io/en/stable/index.html).


