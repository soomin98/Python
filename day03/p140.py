data=100;

def calcsum(n):
    sum=0;
    for d in n:     #n이List
        sum+=d;
    return sum;

def f2(s,e):
    sum=0;
    avg=0;
    for data in range(s,e+1):
        sum+=data;
    return sum/(e-s+1);

def f3(s,e):
    sum=0;
    avg=0;
    for data in range(s,e+1):
        sum+=data;
    print('Result: ');
    print (sum/(e-s+1));

def f4(*n):
    sum=0;
    for d in n:
        sum+=d;
    return sum;

def f5(m,*n):
    sum=0;
    for d in n:
        sum+=d;
    return sum+m;

def f6(begin,end,step):
    """begin: start data....default value=1
    """
    sum=0;
    for d in range(begin,end+1,step):
        sum=sum+d;
    return sum;

def f7(**args):
    b = args['b'];
    e = args['e'];
    s = args['s'];
    sum = 0;
    for d in range(b, e+ 1, s):
        sum = sum + d;
    return sum;

def f8(n, *m, **args):
    print('Test');
    print(n);
    print(m);
    print(args);

