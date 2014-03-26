from pymongo import MongoClient


client = MongoClient()
scrapy = client.scrapy
yahoo = scrapy.yahoo
html = yahoo.find_one()
print html
