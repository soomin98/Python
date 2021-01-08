print('start');
cart=[];
def viewCart(c):

    sump = 0;
    sumc = 0;
    for item in cart:
        print('Item: %s %d %d' % (item[0], int(item[1]), int(item[2])));
        sump += int(item[1]);
        sumc += int(item[2]);
    print('Total: %d %d' % (sump, sumc));

while True:

    menu=input('Input menu(i,v,r,q)');
    if menu =='i':
        item=input('Input item(name,price,count)');
        item=item.split(' ');
        cart.append(item);
    if menu == 'v':
        print('view');
        viewCart(cart);
    if menu=='r':#삭제기능
        it=input('Input Item name');
        for citem in cart:
            if it in citem:
                cart.remove(citem);
            else:
                print('Wrong item');

        viewCart(cart);
    if menu == 'q':
        print('bye');
        break;

print('end')

