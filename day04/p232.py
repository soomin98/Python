data="""Python is also a object oriented programming language used very often on the Internet by web based tools such as Google."""

temp='abc def ghi';
count={};# 'a':10, 'b':120 'c':90;
for c in data:
    if c.isalpha()==False:
        continue;
    c=c.lower();
    if c not in count:
        count[c]=1;
    else:
        count[c]+=1;
print(count.items());
result=sorted(count.items(),key=lambda x:x[1],reverse=True);

print(result);