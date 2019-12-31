from django.shortcuts import render, redirect, HttpResponseRedirect, HttpResponse
from django.contrib.auth.forms import UserCreationForm, forms
from homepage.index_prices import args, price_nifty, diffn_green, diffn_red, price_sensex, diffs_red, diffs_green, \
    price_nb, diffnb_green, diffnb_red, price_bm, diffbm_green, diffbm_red

from homepage.forms import RegistrationForm
from .models import Homepage_db
import datetime as dt
from datetime import date
import pandas_datareader.data as web
from tech_analysis.models import Conames
import json
from django.contrib.auth import login
from azure.cognitiveservices.search.newssearch import NewsSearchAPI
from azure.cognitiveservices.language.textanalytics import TextAnalyticsClient
from msrest.authentication import CognitiveServicesCredentials
import os


def homepage(request):
    global x, rows
    tickers = ['LT.BO', 'MARUTI.BO', 'RELIANCE.NS', 'WIPRO.BO', 'KOTAKBANK.NS']
    closeps = []
    x = []
    price_diff_green = []
    price_diff_red = []
    hpbar = []
    for ticker in tickers:
        start = dt.datetime(2019, 1, 1)
        end = date.today()
        df = web.DataReader(ticker, 'yahoo', start, end)
        close = df['Close']
        price_diff = ((close[-1] - close[-2]) / close[-2]) * 100
        if price_diff > 0:
            price_diff_green.append("+" + "%.2f" % price_diff + "%")
        else:
            price_diff_green.append("")

        if price_diff < 0:
            price_diff_red.append("%.2f" % price_diff + "%")
        else:
            price_diff_red.append("")
        closeps.append("%.2f" % close[-1])
        x.append(Homepage_db.objects.only('hco_logo').get(htic_name=ticker).hco_logo)
        subscription_key = "d225b3f12aab446aa34af931359edbe0"
        search_term = ticker

        client = NewsSearchAPI(CognitiveServicesCredentials(subscription_key))
        news_result = client.news.search(query=search_term, market="en-us", count=10)

        if news_result.value:

            first_news_result = news_result.value[0]
            data = format(first_news_result.description)

            sec_news_result = news_result.value[1]
            data1 = format(sec_news_result.description)

            third_news_result = news_result.value[2]
            data2 = format(third_news_result.description)

            fourth_news_result = news_result.value[3]
            data3 = format(fourth_news_result.description)
            # print("news name: {}".format(first_news_result.name))
            #
            # print("news description: {}".format(first_news_result.description))


        else:
            HttpResponse("NIL")

        # --------------------------------------------

        TEXT_ANALYTICS_SUBSCRIPTION_KEY = 'TEXT_ANALYTICS_SUBSCRIPTION_KEY'
        if not TEXT_ANALYTICS_SUBSCRIPTION_KEY in os.environ:
            raise Exception('Please set/export the environment variable: {}'.format(TEXT_ANALYTICS_SUBSCRIPTION_KEY))
        subscription_key = os.environ[TEXT_ANALYTICS_SUBSCRIPTION_KEY]

        TEXT_ANALYTICS_ENDPOINT = 'TEXT_ANALYTICS_ENDPOINT'
        if not TEXT_ANALYTICS_ENDPOINT in os.environ:
            raise Exception('Please set/export the environment variable: {}'.format(TEXT_ANALYTICS_ENDPOINT))
        endpoint = os.environ[TEXT_ANALYTICS_ENDPOINT]

        credentials = CognitiveServicesCredentials(subscription_key)
        text_analytics_client = TextAnalyticsClient(
            endpoint=endpoint, credentials=credentials)

        client = text_analytics_client

        documents = [
            {"id": "1", "language": "en", "text": data},
            {"id": "2", "language": "en", "text": data1},
            {"id": "3", "language": "en", "text": data2},
            {"id": "4 ", "language": "en", "text": data3},

        ]

        response = client.sentiment(documents=documents)
        res = []
        for document in response.documents:
            res.append(float(format(document.score)))

        res_mean = (sum(res) / 4) * 100

        if res_mean > 80:
            hpbar.append("StrongBuy_hpbar.svg")
        elif 80 > res_mean > 60:
            hpbar.append("Buy_hpbar.svg")
        elif 60 > res_mean > 35:
            hpbar.append("Hold_hpbar.svg")
        elif 20 > res_mean > 35:
            hpbar.append("Sell_hpbar.svg")
        else:
            hpbar.append("StrongSell_hpbar.svg")

    rows = zip(x, closeps, price_diff_green, price_diff_red, hpbar)

    return render(request, 'homepage/homepage.html',
                  {"rows": rows, 'price_nifty': price_nifty, 'diffn_green': diffn_green, 'diffn_red': diffn_red,
                   'price_sensex': price_sensex,
                   'diffs_red': diffs_red, 'diffs_green': diffs_green, 'price_nb': price_nb,
                   'diffnb_green': diffnb_green,
                   'diffnb_red': diffnb_red, 'price_bm': price_bm, 'diffbm_green': diffbm_green,
                   'diffbm_red': diffbm_red})


def menu(request):
    return render(request, 'homepage/menu.html')


def how_it_works(request):
    return render(request, 'homepage/how_it_works.html', args)


def our_goal(request):
    return render(request, 'homepage/our_goal.html', args)


def our_inspiration(request):
    return render(request, 'homepage/our_inspiration.html', args)


def what_do_we_do(request):
    return render(request, 'homepage/What_do_we_do.html', args)


def who_we_are(request):
    return render(request, 'homepage/who_we_are.html', args)


def future(request):
    return render(request, 'homepage/future.html')


def future1(request):
    return render(request, 'homepage/future1.html')


def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('login')
    else:
        form = RegistrationForm()

        arg = {'form': form}
        return render(request, 'homepage/register.html', arg)
