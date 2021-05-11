# Package Expo - Prophet

## MIST 5730

## Evan Shope and Taylor Last




## Link to video
Prophet Presentation: https://www.youtube.com/watch?v=f2Omn5fiZNE

## Link to package website
Prophet: https://facebook.github.io/prophet/
Prophet in Python: https://facebook.github.io/prophet/docs/quick_start.html#python-api

## What is Prophet?
Prophet is a forecasting procedure that Facebook wrote, implemented in R and Python. The package uses time series data to automate forecasts that can be tuned by data scientists and analysts. Prophet analyzes trends in yearly, weekly, and daily seasonality. It works best with data that is highly seasonal and has several seasons of historical data.

## Why use Prophet?
Forecasting is a form predictive analytics and answers the question 'What will happen?' Prophet makes it easy to make high quality forecasts for experts and novices alike. Some benefit of the package include:

 - Accurate
 - Quick
 - Automated
 - Customizable
 - Cross-platform
 
## Functionalities
 
 - It allows users to easily add a specified number of future date stamps by year, month, and day.
 - Easily fit the time series model by calling `Prophet().fit(df)`, where df is your dataframe with time series data.
 - Users can tune/customize the parameters of the prophet object in order to make the best model possible. Examples include:
      - Interval width: controls the amount of uncertainty in the trend
      - Changepoint prior scale: sets how well the trend fits the data (over/under fit)
      - Daily Seasonality: helps account for daily seasonality if present in the data
 - Create plots with predefined functions
      - uses the plot fucntion to plot scatter plot of your desired variable over time
      - adds smoother and confidence interval to the scatter plot
      - plots can be made interactive with plotly
      - pass in forecast data as the parameter to view historical data and future predicted data (with confidence interval)
      - view components of the model: trend, weekly seasonality, and yearly seasonality
      - include changepoint function to view shifts in the trend

## Use Cases:

 - Temperature Data
 - Stock Data
 - Sales Data: Business Forecasts
 - Website metrics
 - Heart rate monitor
 - Key economic metrics (GDP, Unemployment,etc.)

## Installation instructions

Run the following code:

```
!pip install pystan
!pip install fbprophet
!pip3 install plotly
!pip install ipywidgets
```