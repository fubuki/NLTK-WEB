import nltk
from pymongo import MongoClient
from nltk.probability import ConditionalFreqDist
from nltk.tokenize import word_tokenize
from nltk.corpus import treebank
from nltk.corpus import wordnet

client = MongoClient()
scrapy = client.scrapy
bbc = scrapy.bbc
html = bbc.find_one()

# tokens
# identify

def title_preprocess(document):
	sentences = nltk.sent_tokenize(document)
	sentences = [nltk.word_tokenize(sent) for sent in sentences] 
	sentences = [nltk.pos_tag(sent) for sent in sentences] 

	print sentences


title_preprocess(html['title'])