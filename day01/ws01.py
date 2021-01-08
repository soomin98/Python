a=input('input number1?');
b=input('input number2?');
c=input('input number3?');
num1=0;
num2=0;
num3=0;
sum=0;
avg=0.0;
try:
    num1=int(a);
    num2=int(b);
    num3=int(c);

    for a in range(1, num1 + 1):
        for b in range(1, num2 + 1):
            for c in range(1, num3 + 1):
                sum = a + b + c

    avg = sum / 3;
    if avg!=int(avg):
        avg = round(avg,2);
        print(sum, avg, sep=",");
    else:
        print(sum, avg, sep=",");

except:
    print("Invalid Input Number,,,Try Again");
exit();



