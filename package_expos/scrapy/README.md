```python
import scrapy
from scrapy.crawler import CrawlerProcess
import requests
from scrapy.http import TextResponse
import pandas as pd
import json
import logging
```

Presentation: [link](https://www.youtube.com/watch?v=G4kcSFcJO48)

## Scrapy

Scrapy is a fast high-level web crawling and web scraping framework, used to crawl websites and extract structured data from their pages. It can be used for a wide range of purposes, from data mining to monitoring and automated testing.


The main tools for creating and running scrapy objects are spiders and then processing them through a crawler.

to start, type:

    pip install Scrapy

then at the beginning of your notebook:

    import scrapy

below is a basic construction of a spider class using scrapy

    class QuotesSpider(scrapy.Spider):
        name = "quotes"
        start_urls = [
            'http://quotes.toscrape.com/page/1/',
            'http://quotes.toscrape.com/page/2/',
        ]

        def parse(self, response):
            page = response.url.split("/")[-2]
            filename = f'quotes-{page}.html'
            with open(filename, 'wb') as f:
                f.write(response.body)

you're going to want start by naming your Spider, then with either the `start_requests` or `start_urls` functions, input the starter urls you want to scrape from.

The `parse()` method usually parses the response, extracting the scraped data as dicts and also finding new URLs to follow and creating new requests `(Request)` from them.

Scrapy has a couple of issues when trying to run only on Jupyter Notebooks as using the shell to test different selectors does not work.

However we can slightly get around this by using a get request: 


```python
r = requests.get('https://www.basketball-reference.com/teams/ATL/2021.html/')
response = TextResponse(r.url, body=r.text, encoding='utf-8')
```

then you can test whether your selectors are working by running them in the notebook, for example:


```python
response.css('.left:nth-child(6)::text').extract()
```




    ['March 18, 1991',
     'August 27, 1998',
     'May 18, 1994',
     'September 19, 1998',
     'September 23, 1997',
     'August 8, 1988',
     'October 2, 1995',
     'December 11, 2000',
     'November 10, 1991',
     'August 18, 1992',
     'September 20, 1997',
     'September 5, 1997',
     'August 15, 1998',
     'September 1, 1999',
     'December 2, 1997',
     'October 27, 1986',
     'March 18, 1994']



If you run the above code it will bring back all of the birthdays of Hawks players for the 2020-2021 season.

Then you can add those selectors to your spider to grab the info you need.

The demo will show how the following code all works to together to get the desired result.:


```python
import scrapy
from scrapy.crawler import CrawlerProcess
import requests
from scrapy.http import TextResponse
import pandas as pd
import json
import logging


class JsonWriterPipeline(object):

    def open_spider(self, spider):
        self.file = open('quoteresult.jl', 'w')

    def close_spider(self, spider):
        self.file.close()

    def process_item(self, item, spider):
        line = json.dumps(dict(item)) + "\n"
        self.file.write(line)
        return item

class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = [
        'http://quotes.toscrape.com/page/1/',
        'http://quotes.toscrape.com/page/2/',
    ]
    custom_settings = {
        'LOG_LEVEL': logging.WARNING,
        'ITEM_PIPELINES': {'__main__.JsonWriterPipeline': 1}, # Used for pipeline 1
        'FEED_FORMAT':'json',                                 # Used for pipeline 2
        'FEED_URI': 'quoteresult.json'                        # Used for pipeline 2
    }
    
    def parse(self, response):
        for quote in response.css('div.quote'):
            yield {
                'text': quote.css('span.text::text').extract_first(),
                'author': quote.css('span small::text').extract_first(),
                'tags': quote.css('div.tags a.tag::text').extract(),
            }


process = CrawlerProcess({
    'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
})

process.crawl(QuotesSpider)
process.start()

dfjl = pd.read_json('quoteresult.jl', lines=True)
dfjl
```

    2021-05-03 17:11:22 [scrapy.utils.log] INFO: Scrapy 2.5.0 started (bot: scrapybot)
    2021-05-03 17:11:22 [scrapy.utils.log] INFO: Versions: lxml 4.6.1.0, libxml2 2.9.10, cssselect 1.1.0, parsel 1.6.0, w3lib 1.22.0, Twisted 21.2.0, Python 3.8.5 (default, Sep  4 2020, 02:22:02) - [Clang 10.0.0 ], pyOpenSSL 19.1.0 (OpenSSL 1.1.1h  22 Sep 2020), cryptography 3.1.1, Platform macOS-10.15.7-x86_64-i386-64bit
    2021-05-03 17:11:22 [scrapy.utils.log] DEBUG: Using reactor: twisted.internet.selectreactor.SelectReactor
    2021-05-03 17:11:22 [scrapy.crawler] INFO: Overridden settings:
    {'LOG_LEVEL': 30,
     'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'}
    2021-05-03 17:11:22 [py.warnings] WARNING: /Users/jackg/opt/anaconda3/lib/python3.8/site-packages/scrapy/extensions/feedexport.py:247: ScrapyDeprecationWarning: The `FEED_URI` and `FEED_FORMAT` settings have been deprecated in favor of the `FEEDS` setting. Please see the `FEEDS` setting docs for more details
      exporter = cls(crawler)
    





<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>text</th>
      <th>author</th>
      <th>tags</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>“The world as we have created it is a process ...</td>
      <td>Albert Einstein</td>
      <td>[change, deep-thoughts, thinking, world]</td>
    </tr>
    <tr>
      <th>1</th>
      <td>“It is our choices, Harry, that show what we t...</td>
      <td>J.K. Rowling</td>
      <td>[abilities, choices]</td>
    </tr>
    <tr>
      <th>2</th>
      <td>“There are only two ways to live your life. On...</td>
      <td>Albert Einstein</td>
      <td>[inspirational, life, live, miracle, miracles]</td>
    </tr>
    <tr>
      <th>3</th>
      <td>“The person, be it gentleman or lady, who has ...</td>
      <td>Jane Austen</td>
      <td>[aliteracy, books, classic, humor]</td>
    </tr>
    <tr>
      <th>4</th>
      <td>“Imperfection is beauty, madness is genius and...</td>
      <td>Marilyn Monroe</td>
      <td>[be-yourself, inspirational]</td>
    </tr>
    <tr>
      <th>5</th>
      <td>“Try not to become a man of success. Rather be...</td>
      <td>Albert Einstein</td>
      <td>[adulthood, success, value]</td>
    </tr>
    <tr>
      <th>6</th>
      <td>“It is better to be hated for what you are tha...</td>
      <td>André Gide</td>
      <td>[life, love]</td>
    </tr>
    <tr>
      <th>7</th>
      <td>“I have not failed. I've just found 10,000 way...</td>
      <td>Thomas A. Edison</td>
      <td>[edison, failure, inspirational, paraphrased]</td>
    </tr>
    <tr>
      <th>8</th>
      <td>“A woman is like a tea bag; you never know how...</td>
      <td>Eleanor Roosevelt</td>
      <td>[misattributed-eleanor-roosevelt]</td>
    </tr>
    <tr>
      <th>9</th>
      <td>“A day without sunshine is like, you know, nig...</td>
      <td>Steve Martin</td>
      <td>[humor, obvious, simile]</td>
    </tr>
    <tr>
      <th>10</th>
      <td>“This life is what you make it. No matter what...</td>
      <td>Marilyn Monroe</td>
      <td>[friends, heartbreak, inspirational, life, lov...</td>
    </tr>
    <tr>
      <th>11</th>
      <td>“It takes a great deal of bravery to stand up ...</td>
      <td>J.K. Rowling</td>
      <td>[courage, friends]</td>
    </tr>
    <tr>
      <th>12</th>
      <td>“If you can't explain it to a six year old, yo...</td>
      <td>Albert Einstein</td>
      <td>[simplicity, understand]</td>
    </tr>
    <tr>
      <th>13</th>
      <td>“You may not be her first, her last, or her on...</td>
      <td>Bob Marley</td>
      <td>[love]</td>
    </tr>
    <tr>
      <th>14</th>
      <td>“I like nonsense, it wakes up the brain cells....</td>
      <td>Dr. Seuss</td>
      <td>[fantasy]</td>
    </tr>
    <tr>
      <th>15</th>
      <td>“I may not have gone where I intended to go, b...</td>
      <td>Douglas Adams</td>
      <td>[life, navigation]</td>
    </tr>
    <tr>
      <th>16</th>
      <td>“The opposite of love is not hate, it's indiff...</td>
      <td>Elie Wiesel</td>
      <td>[activism, apathy, hate, indifference, inspira...</td>
    </tr>
    <tr>
      <th>17</th>
      <td>“It is not a lack of love, but a lack of frien...</td>
      <td>Friedrich Nietzsche</td>
      <td>[friendship, lack-of-friendship, lack-of-love,...</td>
    </tr>
    <tr>
      <th>18</th>
      <td>“Good friends, good books, and a sleepy consci...</td>
      <td>Mark Twain</td>
      <td>[books, contentment, friends, friendship, life]</td>
    </tr>
    <tr>
      <th>19</th>
      <td>“Life is what happens to us while we are makin...</td>
      <td>Allen Saunders</td>
      <td>[fate, life, misattributed-john-lennon, planni...</td>
    </tr>
  </tbody>
</table>
</div>




```python

```
