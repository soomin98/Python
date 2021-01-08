#enumerate
score=[90,80,60,100];
#score.sort(reverse=True);
score2=sorted(score,reverse=True);
for i in enumerate(score2,1):# 1부터 시작해라
    print(i,sep=' ');
    print(type(i),sep=' ');

#filter p.247
def myfilter1(n):
    return n>=90;

for i in filter(myfilter1, score):
    print(i);
print('-------------------------');

for i in filter(lambda x:x>=90, score):
    print(i);
print('-------------------------');

#map p.248
def mymap(n):
    return n/3;


score=[93,87,65,100];

for i in map(mymap,score):
    print(i);

print('-------------------------');

for i in map(lambda x:x/3,score):
    print(i);




