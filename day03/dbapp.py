import dbutil;

print('start');
while True:
    menu=input('Input menu: i,s,sa,q');
    if menu=='q':
        print('bye');
        break;
    if menu=='i':
        datas=input('Input information..');
        datas=datas.split(' ');
        dbutil.insert(id=datas[0].strip(),
                      pwd=datas[1].strip(),
                      name=datas[2].strip(),
                      age=int(datas[3].strip()));

    if menu=='sa':
        users=dbutil.selectall(); #list안에 List
                #for n in range(len(users)):
                 # print(users[n]);

        for user in users:
            print('User info: %s %s %s %d' %(user[0],user[1],user[2],user[3]));

    if menu=='s':
        id=input('input user id..');
        user=dbutil.select(id=id);
        print('User Info %s %s %s %d ' %(user[0],user[1],user[2],user[3]))






print('end');