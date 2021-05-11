# PyGalExpo
# Presentation
You can find the video presentation [here](https://www.youtube.com/watch?v=N0_N1DweVSo)
# Summary of Support Files
- `PyGal Walkthrough.ipynb`: the notebook containing this tutorial code
- `coffee-chain.csv`: a small file containing coffee-chain.csv data used in the tutorial code

# Guide
[PyGal](http://www.pygal.org/en/stable/index.html) is a module that creates SVG (Scalable Vector Graphics) graphs and charts. PyGal offers in-depth customization but is simple and intuitive.

# Installation Steps
* First install PyGal, and import it as well.
  * !pip install pygal
  * import pygal
* Pandas allows us to import our needed dataset easily.
  * import pandas as pd
  * df = pd.read_csv('coffee-chain.csv')

# Functionalities and Use Cases
PyGal's usage of SVG images allows your visualizations to be easily transported and embedded within websites or applications such as dashboards. The SVG preserves the integrity of the visualization's shapes, and gives you the option to make your images interactive and animated.

PyGal has the functionality to create 14 types of visualizations, from a simple bar chart to a funnel chart detailing progressively changing proportions. These charts have a bevy of styles that can be applied as well. PyGal has 14 built-in styles that are eye-pleasing and seamless to integrate into your visualizations. PyGal is a simple but powerful tool to tell stories visually with your data.