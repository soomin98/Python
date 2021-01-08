num=1000;
str1='result:';
str2='won';
print('result:'+str(num)+' won');

print();
print('%s %d %s'%(str1,num,str2));
print('%10d' %num);

nums1=[1000,2000,30,21000];
for n in nums1:
    print('Price: %-10d Won'%n);