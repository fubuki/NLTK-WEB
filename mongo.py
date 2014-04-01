import nltk
from pymongo import MongoClient
from nltk.probability import ConditionalFreqDist
from nltk.tokenize import word_tokenize

client = MongoClient()
scrapy = client.scrapy
bbc = scrapy.bbc
html = bbc.find_one()

text = nltk.word_tokenize(html['body'])
result = nltk.pos_tag(text)
print result

