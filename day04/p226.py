#Dictionary
score=(1,2,3,4,5);
item1=['item1',1000,1];

item2={'name':'item1','price':1000,'count':1};

print(item2.get('pri','Empty'));

if 'count' in item2:
    print(item2.get('count')*100);