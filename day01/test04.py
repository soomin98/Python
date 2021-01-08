#숫자를 입력 받는다
#1에서 입력 받은 숫자 값 만큼 출력한다.
a=input("number?");

sum=0
average=0;
for y in range(1,int(a)+1) :
    sum=sum+y

average = sum/int(a)
print(sum,average,sep=",")

