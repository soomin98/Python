import time;
import datetime;



t=time.time();
print(t);#1970.1.1~현재까지의 초
#localt=time.localtime()
localt=datetime.datetime.now();
#print(time.localtime(t));#괄호에 t를 안넣어도 상관x
print(type(localt));
print(localt.year);
print(localt.month);
print(localt.day);
