değer=5
x=değer-1
while x>1:
    if değer%x==0:
        print('{} sayisi asal değildir'.format(değer))
        break
    else:
            x-=1
else:
    print('{} sayisi asaldır'.format(değer))