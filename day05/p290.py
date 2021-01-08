#예외상황처리하기
'''a=input('Input Number..?');
result=0;
try:
    result = 2 / int(a);
except:
    print('Invalid Input Number..');
    exit();
print(result);'''

#p294
d='a';
result=0;
try:
    num=int(d);
    result=10/num;
except ValueError as e:
    print('Invalid Data..');
    exit();
except ZeroDivisionError:
    print('ZeroDivisionError..');
    exit();
print(result);

