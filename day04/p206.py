s=[];
s.append(10);
s.append(20);
s.append(30);
s.append(40);
s.append(50);
s.insert(2,99);
s[3]=[1,2,3];
del(s[0]);
s.remove(50);
print(s.pop(0));
print(s.index(40));#몇번째에있는지알려줌
s.append(30);
print(s.count(30));
print(s);

str=['A','B','C','D','D'];

if 'A' in str:
     str.remove('A');
else:
    str.append('A');

print(str);