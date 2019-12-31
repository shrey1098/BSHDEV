import pandas_datareader.data as web
import datetime as dt
from datetime import date

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
args = {'price_nifty': price_nifty, 'diffn_green': diffn_green, 'diffn_red': diffn_red, 'price_sensex': price_sensex,
        'diffs_red': diffs_red, 'diffs_green': diffs_green, 'price_nb': price_nb, 'diffnb_green': diffnb_green,
        'diffnb_red': diffnb_red, 'price_bm': price_bm, 'diffbm_green': diffbm_green, 'diffbm_red': diffbm_red}
