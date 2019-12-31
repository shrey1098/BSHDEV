import datetime as dt
from datetime import date
import pandas_datareader.data as web
import ta
from statistics import mean


def tech_analysis(request):
    if request.method == 'GET':
        form = request.GET
        ticker = form.get("Ticker", "0")
        # return HttpResponse(ticker)
        start = dt.datetime(2017, 1, 1)
        end = date.today()
        df = web.DataReader(ticker, 'yahoo', start, end)

        # dates: List[str] = []
        # for x in range(len(df)):
        #     newdate = str(df.index[x])
        #     newdate = newdate[0:10]
        #     dates.append(newdate)

        close = df['Close']
        high = df['High']
        low = df['Low']
        volume = df['Volume']

    def rs():
        r = ta.rsi(close, n=14, fillna=False)
        rsi = (r[-1])
        if 15.1 <= rsi <= 30:
            status = "RSI signal is: Buy"
        elif rsi <= 15:
            status = "RSI signal is: Strong Buy"
        elif 84.9 <= rsi >= 70:
            status = "RSI signal is: Sell"
        elif rsi >= 85:
            status = "RSI signal is: Strong Sell"
        else:
            status = "RSI signal is: Hold"
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
                status1 = "AO Signal is: Buy"
            else:
                status1 = "AO Signal is: Sell"

        elif 0 <= AO <= 0.5:
            def order():  # For descending
                for i in range(len(A) - 1):
                    if A[i] - A[i + 1] < 0:
                        return False
                    return True

            if order():
                status1 = "AO Signal is: Sell"
            else:
                status1 = "AO Signal is: Buy"

        elif AO <= -1:
            status1 = "AO Signal is: Buy"
        elif AO >= 1:
            status1 = "AO Signal is: Sell"
        else:
            status1 = "AO Signal is: Hold"
        return status1

    def mf():
        mfi = ta.money_flow_index(high, low, close, volume, n=14, fillna=False)
        MFI = mean(mfi[-7:])
        if MFI <= 20:
            status2 = "MFI signal is: Buy"
        elif MFI <= 30:
            status2 = "MFI signal is: Buy"
        elif MFI >= 80:
            status2 = "MFI signal is: Sell"
        elif MFI >= 70:
            status2 = "MFI signal is: Sell"
        else:
            status2 = "MFI signal is: Hold"
        return status2

    def so():
        so = ta.stoch(high, low, close, n=14, fillna=False)
        SO = (so[-1])
        if SO <= 20:
            status3 = "SO signal is: Buy"
        elif SO <= 30:
            status3 = "SO signal is: Buy"
        elif SO >= 80:
            status3 = "SO signal is: Sell"
        elif SO >= 70:
            status3 = "SO signal is: Sell"
        else:
            status3 = "SO signal is: Hold"
        return status3

    def s_o():
        sos = ta.stoch_signal(high, low, close, n=14, d_n=3, fillna=False)
        SOS = (sos[-1])
        if SOS <= 20:
            status4 = "SOS signal is: Buy"
        elif SOS <= 30:
            status4 = "SOS signal is: Buy"
        elif SOS >= 80:
            status4 = "SOS signal is: Sell"
        elif SOS >= 70:
            status4 = "SOS signal is: Sell"
        else:
            status4 = "SOS signal is: Hold"
        return status4

    def tsi():
        tsi = ta.tsi(close, r=25, s=13, fillna=False)
        TSI = tsi[-1]
        if TSI >= 20:
            status5 = "TSI signal is: Buy"
        elif 5 <= TSI <= 20:
            status5 = "TSI signal is: Buy"
        elif TSI <= 5:
            status5 = "TSI signal is: Hold"
        elif -20 <= TSI <= -5:
            status5 = "TSI signal is: Sell"
        elif TSI >= -20:
            status5 = "TSI signal is: Sell"
        return status5

    def u_o():
        uo = ta.uo(high, low, close, s=7, m=14, len=28, ws=4.0, wm=2.0, wl=1.0, fillna=False)
        UO = uo[-1]
        if UO <= 10:
            status6 = "UO signals is: Buy"
        elif 10.1 <= UO <= 30:
            status6 = "UO signals is: Buy"
        elif 70 <= UO <= 90:
            status6 = "UO signals is: Sell"
        elif UO >= 90:
            status6 = "UO signals is: Sell"
        else:
            status6 = "UO signals is: Hold"
        return status6

    def w_r():
        wr = ta.wr(high, low, close, lbp=14, fillna=False)
        WR = wr[-1]
        if 0 >= WR >= 20:
            status7 = "WR signals is: Sell"
        elif -80 <= WR:
            status7 = "WR signals is: Buy"
        else:
            status7 = "WR signals is: Hold"
        return status7

    def cm():
        cmf = ta.chaikin_money_flow(high, low, close, volume, n=20, fillna=False)
        CMF = cmf[-1]

        if CMF > 1.5:
            vol_status_cmf = "CMF Signal is: Buy"
        elif 0 <= CMF <= 1.5:
            vol_status_cmf = "CMF Signal is: Buy"
        elif CMF == 0:
            vol_status_cmf = "CMF Signal is: Hold"
        elif -1.5 <= CMF <= 0:
            vol_status_cmf = "CMF Signal is: Sell"
        else:
            vol_status_cmf = "CMF Signal is: Sell"
        return vol_status_cmf

    def em():
        emv = ta.ease_of_movement(high, low, close, volume, n=20, fillna=False)
        EMV = emv[-1]
        if EMV >= 1.5:
            vol_status_emv = "EMV Signal is: Buy"
        elif -1.5 <= EMV <= 1.5:
            vol_status_emv = "EMV Signal is: Hold"
        else:
            vol_status_emv = "EMV Signal is: Sell"
        return vol_status_emv

    def f_i():
        fi = ta.force_index(close, volume, n=2, fillna=False)
        FI = fi[-1]
        if FI >= 0:
            vol_status_fi = "FI Signal is: Buy"
        elif FI <= 0:
            vol_status_fi = "FI Signal is: Sell"
        else:
            vol_status_fi = "FI Signal is: Hold"
        return vol_status_fi

    def nv():
        nvi = ta.negative_volume_index(close, volume, fillna=False)
        ema255 = ta.ema_indicator(close, n=255, fillna=False)
        NVI = nvi[-1]
        E = ema255[-1]
        if NVI > E:
            vol_status_nvi = "NVI Signal is: Buy"
        elif NVI < E:
            vol_status_nvi = "NVI Signal is: Sell"
        else:
            vol_status_nvi = "NVI Signal is: Hold"
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
            vol_status_obv = "OBV Signal is: Buy"
        else:
            vol_status_obv = "OBV Signal is: Buy"
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
                vol_status_add = "ADI Signal is: Buy"
            else:
                vol_status_add = "ADI signal is: Sell"

        else:
            vol_status_add = "No signal"

        return vol_status_add

    def at():
        atr = ta.average_true_range(high, low, close, n=14, fillna=False)

        if atr[-1] >= 1.5 + mean(atr[-10:]):
            vot_status_atr = "ATR Signal is: Buy"
        elif atr[-1] <= mean(atr[-10:] - 1.5):
            vot_status_atr = "ATR Signal is: Sell"
        else:
            vot_status_atr = "ATR Signal is: Hold"
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
            vot_status_bb = "BB signal is: Buy"
        elif sub < sub2:
            vot_status_bb = "BB signal is: Sell"
        else:
            vot_status_bb = "BB signal is: Hold"
        return vot_status_bb

    def dch():
        dch = ta.donchian_channel_hband(close, n=20, fillna=False)
        dchi = ta.donchian_channel_hband_indicator(close, n=20, fillna=False)
        dcl = ta.donchian_channel_lband(close, n=20, fillna=False)
        dcli = ta.donchian_channel_lband_indicator(close, n=20, fillna=False)

        if close[-1] == dch[-1]:
            vot_status_dc = "DCH Signals is: Strong Sell"
        elif dch[-1] > close[-1] > dch[-1] - 2:
            vot_status_dc = "DCH Signals is: Sell"
        elif dcl[-1] == close[-1]:
            vot_status_dc = "DCH Signals is: Strong Buy"
        elif dcl[-1] < close[-1] <= dcl[-1] + 2:
            vot_status_dc = "DCH Signals is: Buy"
        else:
            vot_status_dc = "DCH Signals is: Hold"
        return vot_status_dc

    def adx():
        adx = ta.adx(high, low, close, n=14, fillna=False)
        adxn = ta.adx_neg(high, low, close, n=14, fillna=False)
        adxp = ta.adx_pos(high, low, close, n=14, fillna=False)

        if adxp[-1] > adxn[-1]:
            trn_adx_status = "ADX signal is: Buy"
        elif adxp[-1] < adxn[-1]:
            trn_adx_status = "ADX signal is: Sell"
        else:
            trn_adx_status = "ADX signal is: Hold"
        return trn_adx_status

    def ai():
        aid = ta.aroon_down(close, n=25, fillna=False)
        aiu = ta.aroon_up(close, n=25, fillna=False)
        if aiu[-1] > aid[-1]:
            trn_ai_status = "AI signal is: Buy"
        elif aiu[-1] < aid[-1]:
            trn_ai_status = "AI signal is: Sell"
        else:
            trn_ai_status = "AI signal is: Hold"
        return trn_ai_status

    def c():
        cci = ta.cci(high, low, close, n=20, c=0.015, fillna=False)
        cc = cci[-1]

        if 0 <= cc <= 50:
            trn_cci_status = "CCI Signal is: Buy"
        elif 50.1 <= cc <= 100:
            trn_cci_status = "CCI Signal is: Hold"
        elif 100.1 <= cc:
            trn_cci_status = "CCI Signal is: Sell"
        elif -50 <= cc <= 0:
            trn_cci_status = "CCI Signal is: Sell"
        elif -100 <= cc <= -50.1:
            trn_cci_status = "CCI Signal is: Hold"
        else:
            trn_cci_status = "CCI Signal is: Buy"
        return trn_cci_status

    def dpo():
        d = ta.dpo(close, n=20, fillna=False)
        do = d[-1]
        if do >= 0:
            trn_dpo_status = "DPO Signals is: Buy"
        elif do <= 0:
            trn_dpo_status = "DPO Signal is: Sell"
        else:
            trn_dpo_status = "DPo Signal is: Hold"
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
                trn_ema_status = "EMA Signal is: Sell"
            else:
                trn_ema_status = "EMA Signal is: Buy"
            return trn_ema_status
        elif em[-1] > close[-1]:
            def order():  # For ascending
                for i in range(len(e) - 1):
                    if e[i] - e[i + 1] > 0:
                        return False
                    return True

            if order():
                trn_ema_status = "EMA Signal is: Buy"
            else:
                trn_ema_status = "EMA Signal is: Sell"
            return trn_ema_status

    def ich():
        ica = ta.ichimoku_a(high, low, n1=9, n2=26, visual=False, fillna=False)
        icb = ta.ichimoku_b(high, low, n2=26, n3=52, visual=False, fillna=False)

        if ica[-1] > icb[-1]:
            trn_ich_status = "ICH Signal is: Buy"
        elif ica[-1] < icb[-1]:
            trn_ich_status = "ICH Signal is: Sell"
        else:
            trn_ich_status = "ICH Signal is: Hold"
        return trn_ich_status

    def kst():
        kst = ta.kst(close, r1=10, r2=15, r3=20, r4=30, n1=10, n2=10, n3=10, n4=15, fillna=False)
        kst_sig = ta.kst_sig(close, r1=10, r2=15, r3=20, r4=30, n1=10, n2=10, n3=10, n4=15, nsig=9, fillna=False)
        if kst[-1] < kst_sig[-1]:
            trn_kst_status = "KST Signal is: Sell"
        elif kst[-1] > kst_sig[-1]:
            trn_kst_status = "KST Signal is: Buy"
        else:
            trn_kst_status = "KST Signal is: Hold"
        return trn_kst_status

    def macd():
        macd = ta.macd(close, n_fast=12, n_slow=26, fillna=False)
        macd_sig = ta.macd_signal(close, n_fast=12, n_slow=26, n_sign=9, fillna=False)
        if macd[-1] > macd_sig[-1]:
            trn_macd_status = "MACD Signal is: Buy"
        elif macd[-1] < macd_sig[-1]:
            trn_macd_status = "MACD Signal is: Sell"
        else:
            trn_macd_status = "MACD Signal is: Hold"
        return trn_macd_status


