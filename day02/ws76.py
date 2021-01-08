#1.한자리숫자를 입력받는다
#2. 숫자의 범위는 1~9
#. 아니면 프로그램 종료
a=input('input number1...?');
sum=0;
cnt=0;
for n in range(int(a)):
    sum=sum+n+1;
    cnt=cnt+1;



print(sum);
print(sum/cnt);