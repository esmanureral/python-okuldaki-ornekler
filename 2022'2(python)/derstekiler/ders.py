sayi1=int(input("1.sayıyı giriniz:"))
sayi2=int(input("2.sayıyı giriniz:"))
toplam=sayi1+sayi2
print("toplam",toplam)

##########################################

s1=int(input('s1'))
s2=int(input('s2'))
s3=int(input('s3'))
s4=int(input('s4'))
islem=(s1*s2)/s4+s3
print("sonuc",islem)

#########################################

#iki sayını kareleri toplamı

a=int(input("birinci sayıyı giriniz:"))
b=int(input("ikinci sayıyı giriniz:"))
toplam=a*a+b*b
print("girilen sayılarının kareleri toplamı:",toplam)

###################################################
maliyet=float(input("maliyet:"))
KDV=float(input("KDV"))
satış=maliyet+(maliyet/100)*KDV
print("satışfiyatı:",satış)

##############################################
import math
r=float(input("yarıçapı giriniz:"))
alan=math.pi*r*math.pow(r,2)
çevre=2*math.pi*r
print("alanı:",alan)
print("çevresi:",çevre)