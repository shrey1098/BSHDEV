from azure.cognitiveservices.search.newssearch import NewsSearchAPI
import requests
from msrest.authentication import CognitiveServicesCredentials
from newsapi import NewsApiClient

companys = "Vakrangee Limited"
subscription_key = "d225b3f12aab446aa34af931359edbe0"

search_term = companys
date = 2018, 1, 1
client = NewsSearchAPI(CognitiveServicesCredentials(subscription_key))
news_result = client.news.search(query=search_term, market="en-us", count=50, freshness="Month", sortBy="Date",
                                 since=1569888000)

if news_result.value:
    first_news_result = news_result.value[-1]
    data = format(first_news_result.description)

    sec_news_result = news_result.value[-2]
    data1 = format(sec_news_result.description)

    third_news_result = news_result.value[-3]
    data2 = format(third_news_result.description)

    fourth_news_result = news_result.value[-4]
    data3 = format(fourth_news_result.description)
    print("news name1: {}".format(first_news_result.name))
    print("news1: {}".format(first_news_result.description))
    print("news name2: {}".format(sec_news_result.name))
    print("news2: {}".format(sec_news_result.description))
    print("news name3: {}".format(third_news_result.name))
    print("news3: {}".format(third_news_result.description))
    print("news name4: {}".format(fourth_news_result.name))
    print("news4: {}".format(fourth_news_result.description))
