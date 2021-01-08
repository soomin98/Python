def insert(**a):
    id=a['id'];
    pwd=a['pwd'];
    name= a['name'];
    age=a['age'];
    print('%s %s %s %d inserted....'%(id,pwd,name,age));

def select(**a):
    id=a['id'];
    data=[];
    data.append('id');
    data.append('pw01');
    data.append('lee');
    data.append(25);
    return data;

def selectall():
    data=[];
    data.append(['id01','pw01','lee',25]);
    data.append(['id02','pw02','pee',26]);
    data.append(['id03','pw03','mee',27]);
    data.append(['id04','pw04','dee',28]);
    return data;

