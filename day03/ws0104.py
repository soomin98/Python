import random;


while True:
    cnt=0;

    print('Start Number Guess Game');
    num1 = int(input('input number1?'));
    num2 = int(input('input number2?'));
    rn = random.randint(num1, num2);
    print('random number=%d' % rn);

    for cnt in range(1,11):
        cnt+=1;

        num=int(input('Guess number??'));

        if cnt<10:
            if num<rn:
                print('small');
            elif num>rn:
                print('big');
            else:
                print('answer!');
                print('new game start!!');
                break;

            print('%d번째' %(cnt));
        else:
            print('FAIL!');

