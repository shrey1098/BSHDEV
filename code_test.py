import datetime as dt
from datetime import date
import pandas_datareader.data as web
from azure.cognitiveservices.search.newssearch import NewsSearchAPI
from azure.cognitiveservices.language.textanalytics import TextAnalyticsClient
from msrest.authentication import CognitiveServicesCredentials
import os
from statistics import mean, mode
import ta

companys = ["PCJEWELLER.NS", "VAKRANGEE.NS", "PFIZER.NS", "PNB.NS", "SHOPERSTOP.NS", "JSWSTEEL.NS", "LT.NS", "LUPIN.NS",
            "M&M.NS", "MRF.NS", "GAIL.NS"]

tickers = ["PC Jeweller Ltd", "Vakrangee Limited", "Pfizer Limited", "Punjab National Bank", "Shoppers Stop Limited",
           "JW Steel Limited",
           "Larsen & Toubro Limited", "Lupin Limited", "Mahindra & Mahindra limited", "MRF Tyres limited",
           "Gail Limited"]
rows = zip(companys, tickers)
for companys, tickers in rows:
    start = dt.datetime(2019, 1, 1)
    end = dt.datetime(2019, 12, 1)
    end1 = dt.datetime(2019, 12, 25)
    df = web.DataReader(companys, 'yahoo', start, end)
    df1 = web.DataReader(companys, 'yahoo', start, end1)
    close = df['Close']
    high = df['High']
    low = df['Low']
    volume = df['Volume']
    price = close[-1]

    close1 = df1['Close']
    price1 = close1[-1]

    diff = price - price1


    def rs():
        r = ta.rsi(close, n=14, fillna=False)
        rsi = (r[-1])
        if 15.1 <= rsi <= 30:
            status = "Buy"
        elif rsi <= 15:
            status = "Strong Buy"
        elif 84.9 <= rsi >= 70:
            status = "Sell"
        elif rsi >= 85:
            status = "Strong Sell"
        else:
            status = "Hold"
        return status


    def ao():
        ao = ta.ao(high, low, s=5, len=34, fillna=False)
        AO = ao[-1]
        A = (ao[-10:])
        if 0 >= AO >= -0.5:
            def order():  # For ascending
                for i in range(len(A) - 1):
                    if A[i] - A[i + 1] > 0:
                        return False
                    return True

            if order():
                status1 = "Buy"
            else:
                status1 = "Sell"

        elif 0 <= AO <= 0.5:
            def order():  # For descending
                for i in range(len(A) - 1):
                    if A[i] - A[i + 1] < 0:
                        return False
                    return True

            if order():
                status1 = "Sell"
            else:
                status1 = "Buy"

        elif AO <= -1:
            status1 = "Buy"
        elif AO >= 1:
            status1 = "Sell"
        else:
            status1 = "Hold"
        return status1


    def mf():
        mfi = ta.money_flow_index(high, low, close, volume, n=14, fillna=False)
        MFI = mean(mfi[-7:])
        if MFI <= 20:
            status2 = "Buy"
        elif MFI <= 30:
            status2 = "Buy"
        elif MFI >= 80:
            status2 = "Sell"
        elif MFI >= 70:
            status2 = "Sell"
        else:
            status2 = "Hold"
        return status2


    def so():
        so = ta.stoch(high, low, close, n=14, fillna=False)
        SO = (so[-1])
        if SO <= 20:
            status3 = "Buy"
        elif SO <= 30:
            status3 = "Buy"
        elif SO >= 80:
            status3 = "Sell"
        elif SO >= 70:
            status3 = "Sell"
        else:
            status3 = "Hold"
        return status3


    def s_o():
        sos = ta.stoch_signal(high, low, close, n=14, d_n=3, fillna=False)
        SOS = (sos[-1])
        if SOS <= 20:
            status4 = "Buy"
        elif SOS <= 30:
            status4 = "Buy"
        elif SOS >= 80:
            status4 = "Sell"
        elif SOS >= 70:
            status4 = "Sell"
        else:
            status4 = "Hold"
        return status4


    def tsi():
        tsi = ta.tsi(close, r=25, s=13, fillna=False)
        TSI = tsi[-1]
        if TSI >= 20:
            status5 = "Buy"
        elif 5 <= TSI <= 20:
            status5 = "Buy"
        elif TSI <= 5:
            status5 = "Hold"
        elif -20 <= TSI <= -5:
            status5 = "Sell"
        elif TSI >= -20:
            status5 = "Sell"
        return status5


    def u_o():
        uo = ta.uo(high, low, close, s=7, m=14, len=28, ws=4.0, wm=2.0, wl=1.0, fillna=False)
        UO = uo[-1]
        if UO <= 10:
            status6 = "Buy"
        elif 10.1 <= UO <= 30:
            status6 = "Buy"
        elif 70 <= UO <= 90:
            status6 = "Sell"
        elif UO >= 90:
            status6 = "Sell"
        else:
            status6 = "Hold"
        return status6


    def w_r():
        wr = ta.wr(high, low, close, lbp=14, fillna=False)
        WR = wr[-1]
        if 0 >= WR >= 20:
            status7 = "Sell"
        elif -80 <= WR:
            status7 = "Buy"
        else:
            status7 = "Hold"
        return status7


    def cm():
        cmf = ta.chaikin_money_flow(high, low, close, volume, n=20, fillna=False)
        CMF = cmf[-1]

        if CMF > 1.5:
            vol_status_cmf = "Buy"
        elif 0 <= CMF <= 1.5:
            vol_status_cmf = "Buy"
        elif CMF == 0:
            vol_status_cmf = "Hold"
        elif -1.5 <= CMF <= 0:
            vol_status_cmf = "Sell"
        else:
            vol_status_cmf = "Sell"
        return vol_status_cmf


    def em():
        emv = ta.ease_of_movement(high, low, close, volume, n=20, fillna=False)
        EMV = emv[-1]
        if EMV >= 1.5:
            vol_status_emv = "Buy"
        elif -1.5 <= EMV <= 1.5:
            vol_status_emv = "Hold"
        else:
            vol_status_emv = "Sell"
        return vol_status_emv


    def f_i():
        fi = ta.force_index(close, volume, n=2, fillna=False)
        FI = fi[-1]
        if FI >= 0:
            vol_status_fi = "Buy"
        elif FI <= 0:
            vol_status_fi = "Sell"
        else:
            vol_status_fi = "Hold"
        return vol_status_fi


    def nv():
        nvi = ta.negative_volume_index(close, volume, fillna=False)
        ema255 = ta.ema_indicator(close, n=255, fillna=False)
        NVI = nvi[-1]
        E = ema255[-1]
        if NVI > E:
            vol_status_nvi = "Buy"
        elif NVI < E:
            vol_status_nvi = "Sell"
        else:
            vol_status_nvi = "Hold"
        return vol_status_nvi


    def ob():
        obv = ta.on_balance_volume(close, volume, fillna=False)
        OBV = obv[-10:]

        def order():  # For ascending
            for i in range(len(OBV) - 1):
                if OBV[i] - OBV[i + 1] > 0:
                    return False
                return True

        if order():
            vol_status_obv = "Buy"
        else:
            vol_status_obv = "Buy"
        return vol_status_obv


    def adi():
        add = ta.acc_dist_index(high, low, close, volume, fillna=False)
        a = add[-1]
        ad = add[-7:]

        if a <= 1000:
            def order():  # For ascending
                for i in range(len(ad) - 1):
                    if ad[i] - ad[i + 1] > 0:
                        return False
                    return True

            if order():
                vol_status_add = "Buy"
            else:
                vol_status_add = "Sell"

        else:
            vol_status_add = "No signal"

        return vol_status_add


    def at():
        atr = ta.average_true_range(high, low, close, n=14, fillna=False)

        if atr[-1] >= 1.5 + mean(atr[-10:]):
            vot_status_atr = "Buy"
        elif atr[-1] <= mean(atr[-10:] - 1.5):
            vot_status_atr = "Sell"
        else:
            vot_status_atr = "Hold"
        return vot_status_atr


    def bb():
        bbhb = ta.bollinger_hband(close, n=20, ndev=2, fillna=False)
        bbhb_ind = ta.bollinger_hband_indicator(close, n=20, ndev=2, fillna=False)
        bblb = ta.bollinger_lband(close, n=20, ndev=2, fillna=False)
        bblb_ind = ta.bollinger_lband_indicator(close, n=20, ndev=2, fillna=False)
        bbmavg = ta.bollinger_mavg(close, n=20, fillna=False)
        sub = bbhb[-1] - close[-1]
        sub2 = close[-1] - bblb[-1]

        if sub > sub2:
            vot_status_bb = "Buy"
        elif sub < sub2:
            vot_status_bb = "Sell"
        else:
            vot_status_bb = "Hold"
        return vot_status_bb


    def dch():
        dch = ta.donchian_channel_hband(close, n=20, fillna=False)
        dchi = ta.donchian_channel_hband_indicator(close, n=20, fillna=False)
        dcl = ta.donchian_channel_lband(close, n=20, fillna=False)
        dcli = ta.donchian_channel_lband_indicator(close, n=20, fillna=False)

        if close[-1] == dch[-1]:
            vot_status_dc = "Strong Sell"
        elif dch[-1] > close[-1] > dch[-1] - 2:
            vot_status_dc = "Sell"
        elif dcl[-1] == close[-1]:
            vot_status_dc = "Strong Buy"
        elif dcl[-1] < close[-1] <= dcl[-1] + 2:
            vot_status_dc = "Buy"
        else:
            vot_status_dc = "Hold"
        return vot_status_dc


    def ai():
        aid = ta.aroon_down(close, n=25, fillna=False)
        aiu = ta.aroon_up(close, n=25, fillna=False)
        if aiu[-1] > aid[-1]:
            trn_ai_status = "Buy"
        elif aiu[-1] < aid[-1]:
            trn_ai_status = "Sell"
        else:
            trn_ai_status = "Hold"
        return trn_ai_status


    def c():
        cci = ta.cci(high, low, close, n=20, c=0.015, fillna=False)
        cc = cci[-1]

        if 0 <= cc <= 50:
            trn_cci_status = "Buy"
        elif 50.1 <= cc <= 100:
            trn_cci_status = "Hold"
        elif 100.1 <= cc:
            trn_cci_status = "Sell"
        elif -50 <= cc <= 0:
            trn_cci_status = "Sell"
        elif -100 <= cc <= -50.1:
            trn_cci_status = "Hold"
        else:
            trn_cci_status = "Buy"
        return trn_cci_status


    def dpo():
        d = ta.dpo(close, n=20, fillna=False)
        do = d[-1]
        if do >= 0:
            trn_dpo_status = "Buy"
        elif do <= 0:
            trn_dpo_status = "Sell"
        else:
            trn_dpo_status = "Hold"
        return trn_dpo_status


    def ema():
        em = ta.ema_indicator(close, n=12, fillna=False)
        e = em[-7:]
        if em[-1] < close[-1]:
            def order():  # For ascending
                for i in range(len(e) - 1):
                    if e[i] - e[i + 1] > 0:
                        return False
                    return True

            if order():
                trn_ema_status = "Sell"
            else:
                trn_ema_status = "Buy"
            return trn_ema_status
        elif em[-1] > close[-1]:
            def order():  # For ascending
                for i in range(len(e) - 1):
                    if e[i] - e[i + 1] > 0:
                        return False
                    return True

            if order():
                trn_ema_status = "Buy"
            else:
                trn_ema_status = "Sell"
            return trn_ema_status


    def ich():
        ica = ta.ichimoku_a(high, low, n1=9, n2=26, visual=False, fillna=False)
        icb = ta.ichimoku_b(high, low, n2=26, n3=52, visual=False, fillna=False)

        if ica[-1] > icb[-1]:
            trn_ich_status = "Buy"
        elif ica[-1] < icb[-1]:
            trn_ich_status = "Sell"
        else:
            trn_ich_status = "Hold"
        return trn_ich_status


    def kst():
        kst = ta.kst(close, r1=10, r2=15, r3=20, r4=30, n1=10, n2=10, n3=10, n4=15, fillna=False)
        kst_sig = ta.kst_sig(close, r1=10, r2=15, r3=20, r4=30, n1=10, n2=10, n3=10, n4=15, nsig=9, fillna=False)
        if kst[-1] < kst_sig[-1]:
            trn_kst_status = "Sell"
        elif kst[-1] > kst_sig[-1]:
            trn_kst_status = "Buy"
        else:
            trn_kst_status = "Hold"
        return trn_kst_status


    def macd():
        macd = ta.macd(close, n_fast=12, n_slow=26, fillna=False)
        macd_sig = ta.macd_signal(close, n_fast=12, n_slow=26, n_sign=9, fillna=False)
        if macd[-1] > macd_sig[-1]:
            trn_macd_status = "Buy"
        elif macd[-1] < macd_sig[-1]:
            trn_macd_status = "Sell"
        else:
            trn_macd_status = "Hold"
        return trn_macd_status


    subscription_key = "d225b3f12aab446aa34af931359edbe0"
    search_term = tickers
    date = 2018, 1, 1
    client = NewsSearchAPI(CognitiveServicesCredentials(subscription_key))
    news_result = client.news.search(query=search_term)

    if news_result.value:
        first_news_result = news_result.value[2]
        data = format(first_news_result.description)

        sec_news_result = news_result.value[3]
        data1 = format(sec_news_result.description)

        third_news_result = news_result.value[4]
        data2 = format(third_news_result.description)

        # print("news name: {}".format(first_news_result.name))
        #
        # print("news description: {}".format(first_news_result.description))

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

    ]

    response = client.sentiment(documents=documents)
    res = []
    for document in response.documents:
        res.append(float(format(document.score)))

    res_mean = (sum(res) / 4) * 100

    tech_signals = [rs(), ao(), mf(), so(), s_o(), tsi(), u_o(), w_r(), cm(), em(), f_i(), nv(), ob(), adi(),
                    at(), bb(), dch(), ai(), c(), dpo(), ema(), ich(), kst(), macd(), ]
    buy = tech_signals.count("Buy")
    hold = tech_signals.count("Hold")
    tech_score = ((buy * 4) + (hold * 2)) / 2
    news_score = res_mean / 2

    final_score = news_score + tech_score

    if final_score >= 80:
        signal = 'Strong Buy'
    elif 50 <= final_score < 80:
        signal = 'Buy'
    elif 40 <= final_score < 50:
        signal = 'Hold'
    elif 10 < final_score < 40:
        signal = 'Sell'
    elif final_score <= 10:
        signal = 'Strong Sell'

    print(tickers)
    print(signal)
    print(companys)
    print(diff)
