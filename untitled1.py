import quantstats as qs
import pandas as pd
import numpy.random as npr
import investpy as ip
import numpy as np

x = ip.get_stock_recent_data('PETR4','brazil').Close
x
qs.reports.html(x,'SPY')

candidates = ip.get_stocks(country='brazil')
candidates

x = ip.get_stocks_overview('brazil', n_results=700)
x.sort_values('turnover',ascending=False)
len(x)

x.turnover.describe()
q3 = np.quantile(x.turnover, .75)
q3

y = x[x.turnover >= q3]
y
