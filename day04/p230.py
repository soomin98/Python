
st=[
    {'id':'st1','ko':90,'en':100,'ma':99},
    {'id':'st2','ko':90,'en':100,'ma':99},
    {'id':'st3','ko':90,'en':100,'ma':99}
];
'''학생 별 성적 평균과 전체 학생의 과목벼 평균을 출력하시오'''
vs=st[1].values();
print(range(len(st)))

for i in range(len(st)):
    sr=[];
    sum=0;
    vs = st[i].values();
    sr.append(vs);
    print(sr)
    for n in vs:
       print(n);
    print('%d' %(sum));

    #답

for sts in st:
    print('%s 학생의 평균 %.2f' %(sts.get('id'),(sts.get('ko')+sts.get('en')+sts.get('ma'))/3));

kosum=0;
ensum=0;
masum=0;

for sts in st:
    kosum+=sts.get('ko');
    ensum += sts.get('en');
    masum += sts.get('ma');


