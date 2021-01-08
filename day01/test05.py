a=input('input numver...?');
num=0;
try:
    num=int(a);
except:
    print("Invalid Input Number,,,Try Again");
exit();

sum=0
average=0;
for y in range(1,num+1) :
    sum=sum+y

average = sum/num
print(sum,average,sep=",")