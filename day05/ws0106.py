'''
<도어락>
-비밀번호4자리입력,
-비밀번호 일치하면 열리고 불일치하면 경고옴.다시시도가능
-4번불일치하는경우,1분간 재시도 불가능
3.프로세스
    0)비밀번호설정
    1) 비밀번호 입력 대기
	2) 비밀번호 입력
	3) 비밀번호 일치 여부 확인
	    3-1) 일치 시 - 4)로 진행
	    3-2) 불일치 시
	        3-2-1) 3번 이하 일 때 1)로 돌아간다
	        3-2-2) 4번 이상 일 때 1분간 잠금상태가 된 후 1로 돌아간다
	        이때 시간얼마나 남았는지 표시해야함
	4) 문이 열린다 :문이열렸습니다.
	5) 절차 반복
'''

import time;
import datetime;

#전역변수 선언
pwd=[];#비밀번호
cnt = 0;# 시도횟수

def inputpwd(n):#비밀번호 설정함수
    for i in range(0,4):
        num1 = int(input('비밀번호 %d번째자리 설정:' %(i+1)));
        while num1>9:
            num1 = int(input('다시 설정해주세요.inputnumber?:')); #숫자 다시입력
            print('비밀번호 %d번째자리 설정 %d' %(i+1,num1));
        n.append(num1);
    #print(n);
    return n

def inputnum():#비밀번호입력함수
    pwdu = [];
    while True:
        num = input('비밀번호4자리를 입력해주세요,숫자간 공백필요');
        pwdu = num.split(' ');
        m1 = list(map(int, pwdu));
        for i in range(len(m1)):
            if type(num[i]) != type(1):
                print('다시 입력해주세요');  # 숫자 다시입력
            else:
                exit();
        m1 = tuple(m1);
        return m1;

def check(n):#일치불일치 검사
    if n == result1:
        print('door open!');
        exit();
    else:
        errorcount(cnt);
def errorcount(n):#틀린횟수검사
    if (n%4)!=0:
        print('error! try again');
    else:
        print('system locked..wait..');
        showtime();


def showtime():#남은시간 보여주기
    for i in range(1, 61):
        print("%d초 남았습니다." %(60-i));
        time.sleep(1);


inputpwd(pwd);
result1 = tuple(pwd);
print(str('설정된 비밀번호:'),result1);

while True:
    result2 = inputnum();
    print(str('입력된 비밀번호:'),result2);
    cnt += 1;
    print('%d번째 시도' %(cnt));
    check(result2);




