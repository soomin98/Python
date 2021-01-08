import myutil1;

#try:
#    result=myutil1.calc(d);
#    print(result);
#except ValueError:
#    print('숫자가 잘못 입력되었습니다');
#    exit();
d=1000;

try:
    result=myutil1.input(d);
    print('입력금액은 %d 입니다.' % (result));
except:

    print('숫자가 잘못 입력되었습니다');

