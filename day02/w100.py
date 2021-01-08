w=int(int(input("몸무게?")));
h=int((input("키?")));
g=int((input("성별?0은 여자 1은 남자")));
bmi=w/h**2;
if g == 0:
    if bmi<25:
        print("정상");
    elif  25<=bmi<=30:
        print("과체중");
    else:
        print("비만");
else:
    if bmi<25:
        print("정상");
    elif  25<=bmi<=30:
        print("과체중");
    else :
        print("비만");