import datetime
date = datetime.date(2025,1,2) #littleary prints that date y/m/d
print(date)
today = datetime.date.today()
print(today)
time = datetime.time(12,30,0) #hour, min , sec
print(time)
now = datetime.datetime.now()
now = now.strftime("%H:%M:%S %m-%d-%y")#this is form doccumentaiton
print(now)

target_date_time = datetime.datetime(2026,1,2,12,30,1)
current_date_time = datetime.datetime.now()
if target_date_time < current_date_time:
    print('target_date_time has passed')
else:
    print("Target date hasn't passed")