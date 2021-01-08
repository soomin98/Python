str1='python';

print(len(str1));
print(str1[0]);
print(str1[-3]);

for i in str1:
    print(i,end=',');
print();
for i in range(len(str1)):
    print(str1[i], end=',');
print();

for i in range(len(str1)-1,-1,-1):
    print(str1[i],end=',');
print();

#str1[1]='e';
print(str1);
print(str1[:3]);
print(str1[3:-1]);
print(str1[0:4:2]);

filename= '20210104-1324.jpg';
#2021년1월4일
#1시24분
#파일 형식 jpg'
#함수로 만드시오
def name(str):
      print(str[0:4] +'년'+str[4:6]+'월'+str[6:8]+'일' );
name(filename)




