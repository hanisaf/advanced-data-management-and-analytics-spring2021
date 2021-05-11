# **Seaborn**

**Presentation**

You can find the video presentation [here](https://youtu.be/7Y11b6LFEb4)

**Summary of support files**

- `Seaborn expo.ipynb`: the notebook containing this tutorial code
- `tips.csv`: a file containing tip data, this dataset is built in to seaborn, but we have provided a copy as well

**Guide**

Seaborn is a Python data visualization library based on matplotlib. It provides a high-level interface for drawing attractive and informative statistical graphics. The plotting functions operate on dataframes and arrays containing whole datasets. The delcarative API lets you focus on what the different elements of your plots mean, rather than on the details of how to draw them.

**Installation**

Seaborn is part of the Anaconda distribution but if it is not already installed on your computer, you can install it by typing. Once it is installed, you can quickstart it and test it out by using one of the example datasets: 


**Seaborn Visualizations**

There are many different graphs within the Seaborn interface. There are distribution plots which include dist-plots, joint plots, pair plots, and rug plots. Categorical plots include bar plots, count plots, box plots, and violin plots. Some advanced plots are strip plots and swarm plots. There are also matrix plots which include heat maps and cluster maps. Grids include facets grids. Seaborn also has regression plots built into the interface. 

**Example**

We will start with Seaborn's categorical plots. There are three different families of categorical plots, and those families are scatterplots, distribution plots, and estimate plots. First, we will look into scatterpots. `stripplot()` is the default kind in `catplot()`. It adjusts the positions of the points on the categorical axis with a small amount of random "jitter". To create this plot you would write code similar to this:
`tips = sns.load_dataset("tips")
sns.catplot(x="day", y="total_bill", data=tips)`
You have to specify which variable is the x-axis and which is the y-axis. 

A swarm plot can be a bettern approach to a small dataset, because it adjusts the points along the categorical axis using an algorithim that prevents them from overlapping. It is sometimes called a "beeswarm" and is drawn by using `swarmplot()`. This can be activiated by setting kind="swarm" in `catplot()`.

You can also add dimensions to categrorial plots by using hue semantics. This can be set to a variable such as "gender".

