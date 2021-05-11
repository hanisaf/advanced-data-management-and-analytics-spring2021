# FlashText

## Presentation
The video presentation is available [here](https://kaltura.uga.edu/media/t/1_6e9xt8ol).


## Summary of support files

- `FlashText Tutorial.ipynb`: the notebook containing the tutorial code, also used in the presentation
- `The Hunger Games.txt`: the text of the novel *The Hunger Games* by Suzanne Collins, used in the tutorial code

## Guide
[FlashText](https://flashtext.readthedocs.io/en/latest/) is an open source Python library with the purpose of searching/extracting and replacing keywords in text. Although its function is similar to that of regular expressions, it is faster than regular expressions at both extracting and replacing keywords, especially with large numbers of keywords.

The FlashText library is based on the [FlashText algorithm](https://arxiv.org/abs/1711.00046). FlashText operates by storing keywords – the words the user selects to extract and/or replace – in an internal Trie dictionary. In the given sample of text, it then checks each word in the sample against the dictionary of keywords. The speed of checking words against a dictionary allows for the fast processing time of FlashText. Further details of this process are described in the video presentation linked above.

**Some of the functions available in FlashText are: adding keywords to the Trie dictionary (either individually or many at a time), extracting keywords from the text, replacing keywords, extracting additional information using keywords, and identifying and amending the keywords in the dictionary.** In searching for keywords in a text, regular expressions are slightly faster than FlashText only when the number of keywords is below 500. In replacing keywords in a text, FlashText is always significantly faster than regular expressions, because its speed remains nearly constant regardless of the number of keywords in the dictionary.

In sum, FlashText's offerings are advantageous in some cases and less so in others. FlashText is mainly used in processing large texts. It is recommended over regular expressions when the number of keywords to be searched is greater than 500 due to its speed and ease. However, it cannot search special characters (such as "@, $, ^, etc.") as regular expressions can – if keywords contain any of these characters, regular expressions are recommended instead.

### To install FlashText:
`!{sys.executable} -m pip install flashtext`


```python

```
