import binascii
import datetime
import csv
import time
from pygame import mixer

if __name__ == '__main__':
    while True:    
        def read_id():
            global idm
            clf = nfc.ContactlessFrontend("usb")

            tag = clf.connect(rdwr={'on-connect':lambda tag: False})
            #print(tag) #点検用
            tag.sys=3
            idm=binascii.hexlify(tag.idm)
            
        def daytime():
            global now
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
                
        def fa_id():
            global idm
            with open('file/now.csv') as f:
                lst = list(csv.reader(f))

            for n in lst:
                if n[0] == idm:
                    if n[2] == '0':
                        n[2] = '1'
                    else:
                        n[2] = '0'

            with open('file/now.csv', 'w') as f:
                writer = csv.writer(f,lineterminator='\n')
                writer.writerows(lst)
                        
        def play():
            mixer.init()
            mixer.music.load('cursor3.mp3')
            mixer.music.play(1)
        
        read_id()
        print(idm.decode())
        
        now=datetime.datetime.now()
        daytime()
        print(now.strftime('%Y/%m/%d %H:%M:%S'))
        
        play()
        
        lst = [[now.strftime('%Y/%m/%d %H:%M:%S'),idm.decode()]]
        
        time.sleep(1)
        
        with open('file/all_log.csv','a') as f:
            writer = csv.writer(f,lineterminator='\n')
            writer.writerows(lst)

        n = ('log/'+now.strftime('%Y%m')+'.csv')

        with open(n,'a') as f:
            writer = csv.writer(f,lineterminator='\n')
            writer.writerows(lst)