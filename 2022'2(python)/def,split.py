def metin_yazdir(a,b):
    büyük_sayi=büyük_sayi_döndur(a,b)
    sablon_metin="{} sayisi daha büyüktür".format(büyük_sayi)
    print(sablon_metin)
    print(metin_yazdir(5,10))


    ##############################################################



def isim_soyisim_ayırma(isim_soyisim):
        isim=isim_soyisim.split()[0]
        soyisim=isim_soyisim.split()[1]
        return isim,soyisim
print(isim_soyisim_ayırma("Esmanur ERAL"))