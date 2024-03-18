print(" ".join(["esmanur","eral"]))

#######################################
#args de birden çok kelime birleşebilir#

def isim_soyisim_birleştirme(*args):
    return "  ".join(args)
print(isim_soyisim_birleştirme("Esma","Nur","Eral"))

#######################################

def göbek_adi_yazdir(**kwargs):
    if 'gobekadi' in kwargs:
        print(kwargs['gobekadi'])
    else:
        print('gobekadi yok')
print(göbek_adi_yazdir(ad="Esmanur",gobekadi="nur",soyisim="eral"))