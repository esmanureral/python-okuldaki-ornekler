arkadaşlık=["irem yıldız","esma karataş","hatice canyurt","ikbal bilir"]
moderator="ikbal bilir"
kullanicisayisi=0
moderatorsayisi=0
for kullanici in arkadaşlık:
    ad, soyad= kullanici.split()[0], kullanici.split()[1]
    if(kullanici==moderator):
        moderatorsayisi+=1
        print( '{0}. moderator ismi {1} ve soyadi {2}'.format(moderatorsayisi, ad, soyad))
    else:
            kullanicisayisi+=1
            print( '{0}. kullanici ismi {1} ve soyadi {2}'.format(kullanicisayisi, ad, soyad))

#####################################################################################################

liste=[(1,2),(4,5),(8,6)]
for x,y in liste:
    print(x*y)