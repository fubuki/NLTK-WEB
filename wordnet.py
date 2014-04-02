import nltk 
from pymongo import MongoClient
from nltk.corpus import wordnet


client = MongoClient()
scrapy = client.scrapy
bbc = scrapy.bbc
html = bbc.find_one()

tokens = nltk.word_tokenize(html['title'])


print wordnet.synsets(tokens[0])
