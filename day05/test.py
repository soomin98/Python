num=[]
num = input("공백을 구분자로 수 입력:")
num=num.split(' ');
num = list(map(int,num));
print(num);

def print_even(num):
      for i in range(len(num)):
          if num[i]%2==0:
              print(num)

print_even(num);