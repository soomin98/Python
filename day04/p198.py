score=[];
score1=[10,20,30,40,50,60,70,80];
score2=[[1,2,3,4],[5,6,7,8],[9,10]];
#print(score2[1][3]);
suma=0;
for i in score2:
    sum=0;

    for n in i:
        sum+=n;

    print(sum,sum/len(i));
    print();
    suma+=sum
print(suma,round(suma/9));
print('-------------------');

'''각 리스트의 합 평균을 출력하고 
전체 합과 평균을 출력하시오'''
#답
total=0;
totalcnt=0;
for i1 in score2:
    sum=0;
    cnt=len(i1);
    for i2 in i1:
        sum+=i2;
    print('%d %.2f' %(sum,sum/cnt));
    total+=sum;
    totalcnt+=cnt;
print('%d %.2f' %(total, total/totalcnt));




