havadurumu="karlı"
if havadurumu=='yagmurlu':
    print("şemsiye al")
elif havadurumu=='karlı':
    print("atkını tak")
else:
    print("sorun yok")
    
###################################

liste=['a','b','3']
hedefharf='c'
if hedefharf in liste:
    print("mevcut")
else:
    liste.append(hedefharf)
    print("listeye eklendi.")
    print('liste:{}'.format(liste))

###################################

liste=['a','b','3']
hedefharf='a'
if hedefharf in liste and hedefharf==liste[0]:
    print("mevcut ve ilk eleman.")
elif hedefharf in liste:
    print("mevcut ilk eleman değil")
else:
    print("mevcut değil.")


