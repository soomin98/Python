a=input('input number1...?');
b=input('input number2...?');
result = float(a)*float(b); #int는 문자를 숫자로 바꿔줌,float는 실수,str=문자
print(a,b,sep="|",end="="+str(result));
