import random

datas=input('input 3 numbers');
d=datas.split(' ');
print(d);
for n in d:
    print('%s %s' %(n,n.isdecimal()));
