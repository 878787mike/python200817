en=int(input('english score:'))
ma=int(input('math score:'))
if en>=0 and en<=100 and ma>=0 and ma<=100:   
    if ma>=90 and en>=90:
        print('goood!!!!!!!!!!!!!!!')
    elif en>=90 or ma>=90:
        print('再加油')
    else:
        print('you are dead!!!!!!!')
else:
    print('???????')