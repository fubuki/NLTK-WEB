import nltk
from pymongo import MongoClient
from nltk.probability import ConditionalFreqDist
from nltk.tokenize import word_tokenize
from nltk.corpus import treebank

client = MongoClient()
scrapy = client.scrapy
bbc = scrapy.bbc
html = bbc.find_one()

# tokens
tokens = nltk.word_tokenize(html['body'])
# identify
result = nltk.pos_tag(tokens)

# parse tree
tree = treebank.parsed_sents(html['title'])[0]

tree.draw()