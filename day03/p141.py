import p140;



data=[1,2,3,4,5];
result=p140.calcsum(data);
print(result);

result3=p140.f2(2,9);
print(str(result3)+'%'); #숫자랑 문자는 같이 프린트가 안되서 str로 바꿔줘야함

result4=p140.f4(1,2,3,4,5);
print(result4);

result5=p140.f5(100,1,2,3,4,5);
print(result5);


result6=p140.f6(1,100,2);
print(result6);

result7=p140.f7(s=2,e=100,b=1);
print(result7);

p140.f8('datas',1,2,3,4,5, start=10,end=100);