# Almanac config
# By Clok Much
import datetime
from datetime import date, timedelta
class Default:
    year = datetime.datetime.today().year
    month = datetime.datetime.today().month
    todayy=datetime.datetime.now().strftime('%d')
    today=int(todayy)
    if month >= 10:
        if today >= 26:
            year = year + 1


    # Default config
    year = str(year)
    other = "other2021.json"
    yj = year+".json"
    name = "节假日"

class MonthDate:
    # pool of month and date
    large_month = ['01', '03', '05', '07', '08', '10', '12']
    small_month = ['04', '06', '09', '11']
    special_month = ['02']
