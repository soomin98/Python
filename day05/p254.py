a=1;
b=a;
c=1;

if a==b:
    print('ok1');
if a is b:
    print('ok2');
if a is c:
    print('ok3');

print('---------------------');
d1=[1,2,3];
d2=d1;
d3=d1.copy();

if d1==d3:
    print('ok1');
if d1 is d3: #메모리 판별
    print('ok2');