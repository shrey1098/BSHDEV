from django.shortcuts import render, redirect, HttpResponseRedirect, HttpResponse
from django.contrib.auth.forms import UserCreationForm, forms
from homepage.index_prices import args
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
    global x, rows, signal
    start = dt.datetime(2017, 1, 1)
    end = date.today()
    dfn = web.DataReader("^NSEI", 'yahoo', start, end)

    closen = dfn['Close']
    pricen1 = closen[-1]
    pricen2 = closen[-2]
    pdiffn = ((pricen1 - pricen2) / pricen2) * 100
    diffn = "%.2f" % pdiffn
    price_nifty = "%.2f" % pricen1
    if pdiffn > 0:
        diffn_green = "+" + diffn + "%"
    else:
        diffn_green = ""

    if pdiffn < 0:
        diffn_red = diffn + "%"
    else:
        diffn_red = ""

    dfs = web.DataReader("^BSESN", 'yahoo', start, end)
    closes = dfs['Close']
    prices1 = closes[-1]
    prices2 = closes[-2]
    pdiffs = ((prices1 - prices2) / prices2) * 100
    diffs = "%.2f" % pdiffs
    price_sensex = "%.2f" % prices1
    if pdiffs >= 0:
        diffs_green = "+" + diffs + "%"
    else:
        diffs_green = ""

    if pdiffs <= 0:
        diffs_red = diffs + "%"
    else:
        diffs_red = ""

    dfnb = web.DataReader("^NSEBANK", 'yahoo', start, end)
    closenb = dfnb['Close']
    pricenb1 = closenb[-1]
    pricenb2 = closenb[-2]
    pdiffnb = ((pricenb1 - pricenb2) / pricenb2) * 100
    diffnb = "%.2f" % pdiffnb
    if pdiffnb > 0:
        diffnb_green = "+" + diffnb + "%"
    else:
        diffnb_green = ""

    if pdiffnb < 0:
        diffnb_red = diffnb + "%"
    else:
        diffnb_red = ""
    price_nb = "%.2f" % pricenb1

    dfbm = web.DataReader("BSE-MIDCAP.BO", 'yahoo', start, end)
    closebm = dfbm['Close']
    pricebm1 = closebm[-1]
    pricebm2 = closebm[-2]
    pdiffbm = ((pricebm1 - pricebm2) / pricebm2) * 100
    diffbm = "%.2f" % pdiffbm
    if pdiffbm > 0:
        diffbm_green = "+" + diffbm + "%"
    else:
        diffbm_green = ""

    if pdiffbm < 0:
        diffbm_red = diffbm + "%"
    else:
        diffbm_red = ""
    price_bm = "%.2f" % pricebm1
    tickers = ['LT.BO', 'ITC.NS', 'RELIANCE.NS', 'WIPRO.BO', 'TCS.NS']
    stocks = ["Larsen & Toubro", "ITC Limited", "Reliance Industries", "Wipro", "TATA Consultancy Services"]
    closeps = []
    x = []
    price_diff_green = []
    price_diff_red = []
    hpbar = []
    signal = []
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



            # print("news name: {}".format(first_news_result.name))
            #
            # print("news description: {}".format(first_news_result.description))


        else:
            HttpResponse("NIL")

        # --------------------------------------------

        TEXT_ANALYTICS_SUBSCRIPTION_KEY = '4d1d3697dc8548b59163e2592b22beb7'
        subscription_key = TEXT_ANALYTICS_SUBSCRIPTION_KEY

        TEXT_ANALYTICS_ENDPOINT = 'https://analytics4sentiment.cognitiveservices.azure.com/'
        endpoint = TEXT_ANALYTICS_ENDPOINT

        credentials = CognitiveServicesCredentials(subscription_key)
        text_analytics_client = TextAnalyticsClient(
            endpoint=endpoint, credentials=credentials)

        client = text_analytics_client

        documents = [
            {"id": "1", "language": "en", "text": data},
                   
        ]

        response = client.sentiment(documents=documents)
        res = []
        for document in response.documents:
            res.append(float(format(document.score)))

        res_mean = (sum(res) * 100)

        if res_mean > 80:
            hpbar.append("StrongBuy_hpbar.svg")
            signal.append("Strong Buy")
        elif 80 > res_mean > 60:
            hpbar.append("Buy_hpbar.svg")
            signal.append("Buy")
        elif 60 > res_mean > 35:
            hpbar.append("Hold_hpbar.svg")
            signal.append("Hold")
        elif 20 > res_mean > 35:
            hpbar.append("Sell_hpbar.svg")
            signal.append("Sell")
        else:
            hpbar.append("StrongSell_hpbar.svg")
            signal.append("Strong Sell")

    rows = zip(x, closeps, price_diff_green, price_diff_red, hpbar, signal, stocks)

    return render(request, 'homepage/homepage.html',
                  {"rows": rows, 'price_nifty': price_nifty, 'diffn_green': diffn_green, 'diffn_red': diffn_red,
                   'price_sensex': price_sensex,
                   'diffs_red': diffs_red, 'diffs_green': diffs_green, 'price_nb': price_nb,
                   'diffnb_green': diffnb_green,
                   'diffnb_red': diffnb_red, 'price_bm': price_bm, 'diffbm_green': diffbm_green,
                   'diffbm_red': diffbm_red})


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


def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('login')
        else:
            return HttpResponse("Ooopss!! Something was wrong with your information. Please go back and try again.")
    else:
        form = RegistrationForm()

        arg = {'form': form}
        return render(request, 'homepage/register.html', arg)
