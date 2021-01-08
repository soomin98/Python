print('start........');

while True:
    data = input('input number?[q:quit]');
    if data.lower()=='q': #알파벳을 다 소문자로 바꾸는것
        print('bye');
        exit();
    if data.isdecimal():
     result=int(data)*1000;
     print(result);
    else:
        print('invalid number type');

print('end........');


#data.isalnum() 숫자 또는 문자냐
