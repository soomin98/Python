
def view(n):

    print('이름: %s 가격:%s 갯수: %s' %(cart[n-1][0],cart[n-1][1],cart[n-1][2]));



print('start');
cart = []
while True:

    menu=input('Input menu(i,v,q)');
    if menu =='i':
        item=input('Input item(name,price,count)');
        cart.append((item.split(' ')))
        print(cart);
    if menu == 'v':
        for n in cart[n]:
            print('이름: %s 가격:%s 갯수: %s' % (cart[n][0], cart[n][1], cart[n][2]));


    if menu == 'q':
        print('bye');
        break;

print('end')
