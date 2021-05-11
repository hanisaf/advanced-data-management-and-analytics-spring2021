# Bokeh

## Package Expo Video
Video Link: [here](https://youtu.be/VCFpxd5_taI)

## Package Expo Files

- `bokeh_demo.ipynb`: this notebook contains the code used during the demo video
- `demo.csv`: this file contains the data used in the demo video

## Bokeh Guide

### Installation
`pip install bokeh`

### Overview
[Bokeh](https://bokeh.org/) is a data visualization package that focuses on creating interactive visualizations within browser. The packages' functionality ranges from simplistic to complex applications. Some of the more complex visualization use cases include real time data streaming, 3-D plotting, dashboards, etc..

Bokeh has two main user interfaces, bokeh.plotting and bokeh.models. The models interface is more complex and requires more user experience, but it allows the user mopre control over the visuals that they create. For our purpose, I did my demo over the plotting interface since it is more simple and still gives a good overview of the functionality of the package. 

Bokeh's visualizations are created through the `figure()` function which allows users to customize the plots that they create.

Renderers are the data points themselves within a plot. Renderers such get added to figures and represent the data visually. There is a huge range of different kinds of renderers with each having different attributes that a user can customize. 
ex: `plot1 = figure()
    plot1.circle([1,2], [1,2])`
this code would create a simple plot with two points that are shown as circles. The first list of values are the x values for the plot and the second set are the y values. The video demo gives a better overview of the different attributes for the renderers and the various ways that data can be defined for the plots.

Bokeh provides users with a huge variety of functionality that can be used to create all kinds of visualizations and it's a great resource to have. In the video demo I go over a slighly more complex example that gives some insight on how powerful Bokeh can be.

## Resources used
-[website used for demo](https://towardsdatascience.com/creating-an-interactive-map-in-python-using-bokeh-and-pandas-f84414536a06)
this site gave me some great insight and code on how to correctly transform by data to the values that I needed in order to be able to plot my points on the Map tile that I imported. 