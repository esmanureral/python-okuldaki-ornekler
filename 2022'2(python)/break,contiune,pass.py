#break#
harfler=["a","b","c"]*100
for index,harf in enumerate(harfler):
    if harf=='c':
        print('{} harfi {}. indexte!'.format(harf,index))
        break

#contiune#
for sayi in range(1,6):
 if sayi%2==0:
    continue
 print(sayi)

 #pass#
 for sayi in range(1,6):
    if sayi%2==0:
        pass
    else:
        print(sayi)