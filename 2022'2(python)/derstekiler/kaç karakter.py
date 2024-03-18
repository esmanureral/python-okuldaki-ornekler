#klavyeden girilen metnin kaç karakterden oluştuğunu bulmak
metin=input("bir metin giriniz:")
Esayisi=len(metin)
print("sayi=",Esayisi)
for i in metin:
    print(i)

#klavyeden girilen bir metinde karakter sorgulama:
metin=input("bir metin giriniz:")
karakter=input("sorgulanacak karakteri giriniz:")
KS=0
for i in metin:
    if(karakter==i):
        KS=KS+1 
print("bulunan sayı",KS)