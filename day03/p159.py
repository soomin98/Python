data=20;
def calcsum(n):
    sum=0;
    for d in range(n+1):
        sum+=d;
    return sum+data;

result=calcsum(10);
print(result);