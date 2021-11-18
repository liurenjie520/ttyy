# Almanac config
# By Clok Much
import datetime
from datetime import date, timedelta
class Default:
    year = datetime.datetime.today().year
    today = datetime.datetime.today()
    d = datetime.datetime.strptime('2021/11/17', '%Y/%m/%d')
    if today > d:
        # print("888")
        year = year + 1
    else:
        print("当年数据")

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
