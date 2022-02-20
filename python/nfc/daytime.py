import datetime
import csv

now=datetime.datetime.now()

with open('file/daytime.csv') as f:
    lst = list(csv.reader(f))

if lst[0][0] == now.strftime('%Y'):
    if lst[0][1] < now.strftime('%m'):
        n = ('log/'+now.strftime('%Y%m')+'.csv')
        with open(n, 'w'):
             pass

if now.strftime('%Y') > lst[0][0]:
    if lst[0][1] == '12':
        n = ('log/'+now.strftime('%Y%m')+'.csv')
        with open(n, 'w'):
             pass

daytime = [[now.strftime('%Y'),now.strftime('%m'),now.strftime('%d')],[now.strftime('%Y/%m/%d %H:%M:%S')]]

with open('file/daytime.csv','w') as f:
    writer = csv.writer(f,lineterminator='\n')
    writer.writerows(daytime)