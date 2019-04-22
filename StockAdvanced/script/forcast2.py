# -*- coding: utf-8 -*-
from datetime import datetime
from quantdata.stock import quotes
'''
df = quotes.get_forcast_list(2016,2)
print df
'''
def get_quarter(curmonth):
    if curmonth in(1,2,3):
        curquarter = 1
    elif curmonth in (4,5,6):
        curquarter = 2
    elif curmonth in (7,8,9):
        curquarter = 3
    elif curmonth in(10,11,12):
        curquarter = 4
    return curquarter
current_time = datetime.now()
year = current_time.year
month = current_time.month

quarter = get_quarter(month)
forcast_data = quotes.get_forcast_list(year,quarter)
print forcast_data
    


 