import nfc
import binascii
import csv

gakuban = input('>>')

clf = nfc.ContactlessFrontend("usb")

tag = clf.connect(rdwr={'on-connect':lambda tag: False})
print(tag)

tag.sys=3
idm=binascii.hexlify(tag.idm)
#print(idm.decode())

with open('file/now.csv') as f:
    lst = list(csv.reader(f))

for i in lst:
    if gakuban == i[1]:
        i[0] = idm.decode()

with open('file/now.csv', 'w') as f:
    writer = csv.writer(f,lineterminator='\n')
    writer.writerows(lst)

print('終了')