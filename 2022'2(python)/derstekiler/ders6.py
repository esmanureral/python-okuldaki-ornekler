#rastgele işlemler

import random
def islemyap(tur,A,B):
    if tur==1:
        sonuç=A+B
    elif tur==2:
        sonuç=A-B
    elif tur==3:
        sonuç=A*B
    else:
        sonuç=A/B
        return sonuç
    
def turtespit(tur):
    if tur==1:
        islemtur="toplama"
    elif tur==2:
        islemtur="çıkarma"
    elif tur==3:
        islemtur="çarpma"
    else:
        islemtur="bölme"
    return islemtur
Isayı=int(input("işlem sayısını giriniz:"))
for i in range(Isayı):
    tur=random.randrange(1,5)
    A=random.randrange(1,5)
    B=random.randrange(1,5)
    islemtur=turtespit(tur)
    sonuç=islemyap(tur,A,B)
    print(i+1,".işlem",islemtur,"A=",A,"B=",B,"sonuç=",sonuç)