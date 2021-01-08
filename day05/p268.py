'''현재시간과 로그아웃시간을 빼서 얼마나 있었는지'''
import time;

start=time.time();
for i in range(1,5):
    print(i);
    time.sleep(1)
end=time.time();

print(end-start);