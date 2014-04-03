import nltk 
from pymongo import MongoClient
from nltk.corpus import wordnet


client = MongoClient()
scrapy = client.scrapy
bbc = scrapy.bbc
html = bbc.find_one()

tokens = nltk.word_tokenize(html['title'])
lists = []

for t in tokens:
	lists.append(wordnet.synsets(t))


word = lists[0][0]


def word_process(word):
	print word
	print word.hypernyms()
	print word.lemmas
	print word.entailments()



word_process(word)