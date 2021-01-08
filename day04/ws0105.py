'''1. 시나리오
2. 전제조건: 당첨금은 랜덤하게 만든다
당첨번호는 랜덤하게 만든다
순위에 따라 당첨금을 차등 지급한다.
게임을 끝내고 다시 시작할 수 있다.'''

import random


while True:
    print('Lotto Start!');
    rn = [];
    for i in range(1, 7):  # 로또숫자 #set을 사용하면 중복되지않는다.!
        rnum = random.randint(1, 45);
        if rnum not in rn:
            rn.append(rnum);
    rn.sort();
    #print(str('랜덤숫자:'),rn);

    pn = [];
    for p in range(1, 6):  # 상금
        pnum = random.randint(5000, 30000);
        if pnum not in pn:
            pn.append(pnum);
    pn.sort();
    print(str('상금:'),pn);

    num = (input('Input 6 number'));
    list1 = num.split(' ');
    list1 = list(map(int, list1));  # 문자열을 정수로 변환
    list1.sort();
    print(str('랜덤숫자:'), rn);
    if list1 == rn:
        print('1등입니다 %d' % (pn[4]));
        re=int(input('다시 하겠습니까? 0=아니오,1=예'));
        if re==0:
            break;

    else:
        cnt = [];
        list2 = list(set(rn).intersection(list1))
        if len(list2) >= 1:
            print('등수확인');
            for n in list2:
                cnt.append(n);
            if len(cnt) == 5:
                print('2등입니다. 금액: %d원' % (pn[3]));
            elif len(cnt) == 4:
                print('3등입니다. 금액: %d원' % (pn[2]));
            elif len(cnt) == 3:
                print('4등입니다. 금액: %d원' % (pn[1]));
            elif len(cnt) == 2:
                print('5등입니다. 금액: %d원' % (pn[0]));
            elif len(cnt) == 1:
                print('6등입니다. 당첨금은 없습니다.');
        else:
            print('꽝');

        re=int(input('다시 하겠습니까? 0=아니오,1=예'));
        if re==0:
            break;




