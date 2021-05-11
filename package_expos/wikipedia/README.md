# Package Expo: Wikipedia 1.4.0 
*Group 6: Joe Burnett, Sofia Cenciarelli, Harrison O'Neal, and Cressie Rynne*

## Introduction
Wikipedia 1.4.0 is an application programming interface (API). This particular API acts as a messenger that delivers requested information for Wikipedia to Python. When used, it creates a Python library using Wikipedia information making it easier to extract data from their evergrowing database.

The Wikipedia API is a useful tool to link to Wikipedia articles for reference material. In this way, the API call is much easier semantically than having to scrap a HTML page. This API is actually acting as a wrapper for the MediaWiki API, and in the words of the owner, “Wikipedia (works) so you can focus on using Wikipedia data, not getting it”. Another key advantage of this approach over a normal web scraping procedure, is the resiliency built into passing through an API VS hard coding. For example, let’s say the webpage for Python (programming language) changed. If you had hard coded in the website URL, then this would brick your application. Since we are passing our calls through this API, built in resiliency for webpage changes is taken care of on the APIs side so that the user can focus on just what they want to use the information for instead of building resiliency into their code (since this is already done for us!). For grabbing information quickly and efficiently, using the Wikipedia package is far superior to the alternative web scraping methods. 

## Installation
To initially install the program, enter the code below without the hashtag in a terminal window:


```python
#!pip install wikipedia
```

Once installed, you will no longer need the installation line of code. Anytime you would like to use the package you will simply need to import the package using the code below without the hashtag:


```python
import wikipedia
```

## Helpful Links
Video Explanation: [Google Drive Link](https://drive.google.com/file/d/1aIEVLPMaikSp3gcJvszh4IQl32JqRURc/view?usp=sharing) or [Vimeo Link](https://vimeo.com/544842485)

[Python Package Index by Wikipedia on Wikipedia 1.4.0](https://pypi.org/project/wikipedia/)

