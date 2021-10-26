# Almanac
# By Clok Much
# Target json:
#       忌/宜: http://www.51wnl.com/YJData/2021.json
#       其他命理: http://www.51wnl.com/moreLumarData/2015.json
# Ref: icalics, By hxgz : https://github.com/hxgz/icalics
import datetime

import config
import fanfa
def sd():
    year = datetime.datetime.today().year
    # Default config
    year = str(year)
    with open(file="holiday.ics", encoding="utf8", mode="w") as file_object:
        start_string = "BEGIN:VCALENDAR\nVERSION:2.0\nCALSCALE:GREGORIAN\nMETHOD:PUBLISH\nX-WR-CALNAME:" \
                       + config.Default.name + "\nX-WR-TIMEZONE:Asia/Shanghai\n" \
                       + "X-WR-CALDESC:"+year+"节假日\n"
        file_object.write(start_string)
        body = fanfa.jk()
        body_string = ("BEGIN:VEVENT\nDTSTAMP:20190912T184136Z\nUID:",
                       "END:VEVENT\n")
        for item in body:
            body0 = body_string[0]
            body1 =   item[1] + 'almanac_in_' + config.Default.year + "\n"
            body2 = "DTSTART;VALUE=DATE:" + item[1] + "\nDTEND;VALUE=DATE:" + item[1] + "\n"
            beizhu = "DESCRIPTION:" +'国务院办公厅节假日安排的通知: '+ item[3]+ "\n"
            body3 = "SUMMARY:" + item[0] +'  '+ item[2] + "\n"
            tixing0 = "BEGIN:VALARM" + "\n" + "TRIGGER;VALUE=DATE-TIME:" + item[1] + "T220000Z" + "\n"
            tixing1 = "ACTION:DISPLAY" + "\n" + "END:VALARM" + "\n"
            body4 = body_string[1]
            full_body = body0 + body1 + body2 +beizhu+ body3 +tixing0 +tixing1 + body4
            file_object.write(full_body)
        end_string = "END:VCALENDAR"
        file_object.write(end_string)




#
if __name__ == '__main__':
    a=sd()
    print(a)
