import calendar;
import sys;#시스템이 실행되는 플랫폼의 정보를 알 수 있다.

calendar.setfirstweekday(6);#월요일이아닌 일요일부터 시작되게

print(calendar.calendar(2020));

print(calendar.weekday(2020,12,25));

print(sys.version);
print(sys.platform);

data=input('Input number..?');
print('Input Number:'+str(data));
