for n in range(2,10):
    if n>6:
        break;
    if n%2==1:
        continue;
    print(str(n)+"단");
    for d in range(1,10):
        print(n,d,(n*d),sep='-');
        if n==6 and d==5:
            break;