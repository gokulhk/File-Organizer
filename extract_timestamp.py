import re, time, calendar 

img = ["20170603_210729.jpg", "IMG-20170731-WA0001.jpg", "PSX_20171008_140633.jpg"]
month = list(calendar.month_name)

#clean the file name to get only the number part
num = [re.sub(r'\D',"",img[i]) for i in [0,1,2]]
num = [i[:8] for i in num]
for i in num:
    y, m, d = i[:4], int(i[4:6]), i[6:8]
    print(y, month[m], d)
print(num)
