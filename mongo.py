import nltk
from pymongo import MongoClient
from nltk.probability import ConditionalFreqDist
from nltk.tokenize import word_tokenize

client = MongoClient()
scrapy = client.scrapy
yahoo = scrapy.yahoo
html = yahoo.find_one()

text = nltk.word_tokenize(html['title'])
result = nltk.pos_tag(text)
print result

text = nltk.word_tokenize("And now for something completely different")
result = nltk.pos_tag(text)
print result