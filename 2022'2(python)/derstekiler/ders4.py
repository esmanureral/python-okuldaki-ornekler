#1-999 arasındaki tek sayıların toplamını veren kod
toplam=1 
for i in range(1,1000):
    if(i%2==1):
        toplam=toplam+i
        print(i)
print("toplam=",toplam)

i=0
toplam=0
while i<=999:
    if(i%2==1):
        toplam=toplam+i
    i=i+1 
print("toplam",toplam)

#bakteri 4 dk da bir ikiye bölünerek çoğalmaktadır.Başlangıçta bir bakteri varsa
#40 dk da oluşacak bakteri sayısı

bakterisayısı=1 
for i in range(1,41):
    if(i%4==0):
        bakterisayısı=bakterisayısı*2
print("bakterisayısı=",bakterisayısı)

zaman=1
bakterisayısı=1 
while zaman <=40:
    if(zaman%4==0):
        bakterisayısı=bakterisayısı*2
    zaman=zaman+1
print("bakterisayısı",bakterisayısı)

#Bir satranç tahtasının 1.karesine 1 buğday,2 karesine 1.karenin 2 katı buğday
#3.karesine 2.karenin 2 katı buğday konuluyor.Satranç tahtasının 16.karesine gelindiğinde konulan toplam buğday sayısı

buğdaysayısı=1 
toplambuğdaysayısı=1 
for i in range(2,17):
    buğdaysayısı=buğdaysayısı*2
    toplambuğdaysayısı=toplambuğdaysayısı+buğdaysayısı
print("toplambuğdaysayısı",toplambuğdaysayısı)

buğdaysayısı=1 
toplambuğdaysayısı=1 
karebilgisi=1 
while karebilgisi<=16:
    karebilgisi=karebilgisi+1
    buğdaysayısı=buğdaysayısı*2
    toplambuğdaysayısı=toplambuğdaysayısı+buğdaysayısı
print("toplambuğdaysayısı",toplambuğdaysayısı)