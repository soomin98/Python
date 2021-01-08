import time;

try:
    print('네트워트 접속 시도');
    time.sleep(2);
    print('네트워트 접속 성공');
    time.sleep(2);
    8/0
    print('네트워트 데이터 전송');
    time.sleep(2);

except:
    print('문제발생');
finally:#문제가있거나없거나 실행됨*중요~*
    print('네트워크접속해지');



