data=[98,87,90,34,56,43];
sum=0;
avg=0;
for n in range(1,6):
    sum=sum+data[n];
print(sum);
avg=sum/len(data)
print(avg);
if avg>=90:
    print("A");
elif 80<=avg<90:
    print("B");
elif 70<=avg<80:
    print("C");
elif 60<=avg<70:
    print("D");
else:
    print("F");

