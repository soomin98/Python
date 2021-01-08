data=[1,2,3,4,5];
print(data);
sum=0;
for d in data:
    sum+=d;
    print(d);

print(sum);
print('-------------------------');

datas=[
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12]
];
sum=0;
for d1 in datas:
    for d2 in d1:
        print(d2, end='');

    print('');

