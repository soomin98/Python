import random;

score=(10,20,30,40);
print(score[0:2]);
score=score+(50,60,70);
print(score);
score=list(score);
print(score);

t=[];
for i in range(1,7):
    temp=random.randint(1,45);
    t.append(temp);

print(t);
t=tuple(t);
print(t);


