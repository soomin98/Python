s='python programming';
print(type(s));
print(type(s[0]));

print(len(s));
print(s.find('o'));
print(s.rfind('o')); #끝에서부터찾음
print(s.index('r'));
print(s.rindex('r'));
print(s.count('o')); #o의 갯수 찾음
print('a'in s); #있냐없냐 물어보기
print('a'not in s);#없니 물어보기

if('a in s'):
    print('OK');
else:
    print('NO');


if str.startswith('p'):
    print('OK');

if str.endswith('g'):
    print('OK');





