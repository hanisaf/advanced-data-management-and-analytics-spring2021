# statsmodels

## Links

- [Video Presentation](https://youtu.be/1OJGA71EZ1c)
- [statsmodels Documentation](https://www.statsmodels.org/stable/index.html)
- [Insurance Dataset (Linear)](https://www.kaggle.com/mirichoi0218/insurance)
- [Diabetes Dataset (Logistic)](https://www.kaggle.com/uciml/pima-indians-diabetes-database)

## Summary of Files

- `demo.ipynb`: Tutorial notebook used in video presentation
- `logistic.png`: Image embedded in demo notebook
- `insurance.csv`: Dataset used for Linear Regression, shows medical charges billed by health insurance
- `diabetes.csv`: Dataset used for Logistic Regression, shows diabetes and other health factors
- `logit_model.pkl`: <b>Not present initially,</b> but will be created if/when saving the logit model in the notebook

## Package Guide

### About

`statsmodels` is an open-source statistical package that provides models for many types of regression. `statsmodels` accepts `pandas` DataFrames for input data, and it allows you to specify your explanatory and response variables with [R formula syntax](https://thomasleeper.com/Rcourse/Tutorials/formulae.html)*:

`y ~ x1 + x2 + x3 ...`

This makes it easy for you to run simple regressions (e.g. Ordinary Least-Squares or Logistic) or advanced ones (e.g. Poisson or Ridge) with just a few lines of code. `statsmodels` allows you to easily generate a summary of the model, extract specific statistics, or save the model as a [.pkl file](https://docs.python.org/3/library/pickle.html) and load it later.

<i>*You can alternatively provide the feature matrix (X) and target array (y) like in </i>`scikit-learn`<i>.</i>

### Use Cases

`statsmodels` competes with the likes of `scikit-learn` for regression tasks, but its use cases are more closely tied to econometrics and time-series analysis than machine learning. Because of its R-like syntax, the package is popular among statisticians and econometricians migrating to Python. While it lacks in machine learning options, `statsmodels` offers a simple interface for complex statistical analysis, which is its main selling point.

### Installation

`statsmodels` is included in the Anaconda distribution, so you may already have it installed. If not, you can install it via `!pip install statsmodels`.

To start using the package, import it into your notebook with `import statsmodels.api`.
