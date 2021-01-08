data=[
    [100,90,98,88],
[100,90,98,87],
[100,90,98,86],
[100,90,98,85]
    ]

sum=0;
avg=0;
scoresum=[];

for x in range(len(data)):
    for y in data[x]:
        sum+=y;
        avg=sum/4;
    scoresum.append(sum)
    sum=0;
for i in range(len(scoresum)):
    print("각 학생의 합=",scoresum[i])
    print("각 학생의 평균=",scoresum[i]/len(scoresum))

num = 0
for i in range(len(data)):
    for j in range(len(data[i])):
        num = num + 1
        sum = sum + data[i][j]
print("전체학생점수합=",sum);
print("전체학생점수평균=",sum / num);


















