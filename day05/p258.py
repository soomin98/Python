from random import randint;
import myutil1 as m1;
import myutil2 as m2;
import math;
import turtle as t;#그림그리는것
import statistics;#통계

a=100;
b=randint(1,10);
print(a,b);
print(m1.sum(a,b));
print(m2.sum(a,b));

#261
print(math.sqrt(2));
print(math.hypot(2,4));

data=[10,44,20,98,100,70,29];
print(statistics.mean(data));
print(max(data));

t.penup();
t.goto(-720,0);
t.pendown();
for x in range(-720,720):
    t.goto(x,math.sin(math.radians(x))*100);

t.down();






