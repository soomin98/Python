data=[[100,90,98,88],
[100,90,98,87],
[100,90,98,86],
[100,90,98,85]]

sum = 0
num = 0
for i in range(len(data)):
    for j in range(len(data[i])):
        num = num + 1
        sum = sum + data[i][j]
print(sum / num)