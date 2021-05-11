# Quandl

 Presentation [Presentation link](https://youtu.be/60qDeSNc-Wc)

### Background
The premier source for financial, economic and alternative datasets, serving investment professionals. 
Nasdaq’s Quandl platform is used by analysts from the world’s top hedge funds, asset managers and investment banks.

### Formats
Quandl data comes in two formats, Time-series and Table format. This is the focus of our demo where we will show what the quandl platform provides with these two options. 

__Time-series__ - Data taken over a period of time

__Table__ - Data can be numerical or categorical, but was observed at a single point in time. 

![Quandl Data Diagram](https://files.readme.io/1881d5f-quandl-databases.jpg)


### Accessing the data
Quandl data is accessible, much of it for free, through their RESTful API. You need an API token to query the API and can sign up for one [here](https://www.quandl.com/sign-up)

Authenticated users have a limit of 300 calls per 10 seconds, 2,000 calls per 10 minutes and a limit of 50,000 calls per day.

While there is a paid tier with many more data, the free datasets are extensive and plentiful. Some free datasets worthy of mention are:

* Wiki Continuous Futures – This dataset is built on top of raw data from ICE, CME, LIFFE, etc, and is curated by the Quandl community.

* Zillow Real Estate Data – This dataset is the leading real estate and rental marketplace.

* Federal Reserve Economic Data – This dataset includes things such as growth, employment, inflation, labor, manufacturing and many more US economic data.

[Explore Quandl Datasets](https://www.quandl.com/search)

#### Asset Classes

* Equities
* Currencies
* Interest Rates & Fixed Income
* Options
* Indexes
* Mutual Funds & ETFs
* Real Estate
* Venture Capital & Private Equity
* Economy & Society
* Energy
* Agriculture
* Metals
* Futures
* Other

## Getting Started
Quandl has a python package that can be installed using your favorite package manager. For example:

`pip install quandl`

`conda install -c anaconda quandl`

Quandl is also avaliable and has use guides for Excel, R, Ruby, MATLAB, and direct API calls. 

### Getting Data

In Python, querying the data is as simple as:

```
import quandl
quandl.ApiConfig.api_key = YOUR_API_KEY_HERE

quandl.get(DATASET_CODE)
```

This returns a Pandas DataFrame object by default. 


## Conclusion

Quandl is an easy to use and extremely simple tool to get accurate, feature rich data in one line of code. The uses are vast with its builtin support for Pandas, being easy to implement in Artificial Intelligence and Machine Learning models that may require large datasets. 

Dataset categories are also broad, with data ranging from financial to healthcare to world economic indicators. 