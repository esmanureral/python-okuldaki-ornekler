#şubat
def şubatgüntespit (yıl):
    if(yıl%4==0):
        sonuç=29
    else:
        sonuç=28
    return sonuç
for i in range(0,2024):
    sonuç=şubatgüntespit(i)
    if(sonuç==29):
        print(i)

#DÖRTGENİN TÜRÜNÜ VERİP ALAN ÇEVRE BULMA

def dörtgenalan(k1,k2):
    alan=k1*k2
    return alan
def dörtgençevre(k1,k2):
    çevre=2(k1+k2)
    return çevre
def dörtgentür(k1,k2):
    if(k1==k2):
        tür="kare"
    else:
        tür="dikdörtgen"
Isayı=int(input("dörgen sayısını giriniz:"))
import random
for i in range(Isayı):
    
    k1=random.randrange(1,4)
    k2=random.randrange(1,4)
    tür=dörtgentür(k1,k2)
    alan=dörtgenalan(k1,k2)
    çevre=dörtgençevre(k1,k2)
print("i+1".dörtgen,"k1=",k1,"k2=",k2,"alan=",alan,"çevre=",çevre,"tür=",tür)