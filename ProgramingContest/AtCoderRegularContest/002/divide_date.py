import datetime
YMD = input()
ymd = datetime.datetime.strptime(YMD,'%Y/%m/%d')

while True:
    if int(ymd.year)% (int(ymd.day)*int(ymd.month))==0:
        print(ymd.strftime('%Y/%m/%d'))
        exit()
    ymd = ymd+datetime.timedelta(days=1)
