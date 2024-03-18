#snake_case
def bes_bastir():
    print(5)
print(bes_bastir())

######################
def sayi_döndür(sayi):
    return sayi
print(sayi_döndür(100))
######################
def sayi_döndür(sayi=250):
    return sayi
print(sayi_döndür(100))
######################
def sayi_döndür(sayi=250):
    return sayi
print(sayi_döndür())
############################################
def büyük_sayi_döndür(a,b):
    if a<b:
        return b
    elif b<a:
        return a
print(büyük_sayi_döndür(5,10))
############################################
def büyük_sayi_döndür(a,b):
    return a   ##ilk return e uğrar sonra fonksiyondan çıkar
    return b
print(büyük_sayi_döndür(5,10))

def metin_yazdır(a,b):
    büyük_sayi=buyuk_sayı_döndür(a,b)
    sablon_metin="{} daha büyük sayıdır.".format(büyük_sayi)
    print(sablon_metin)
    print(metin_yazdır(5,10))