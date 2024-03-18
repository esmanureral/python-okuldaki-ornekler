A=open("A.txt")
Averiler=A.readlines()
for i in Averiler:
    print(i)
print("------")

B=open("B.txt")
Bveriler=B.readlines()
for i in Bveriler:
    print(i)


#A,B,C dosyalarındaki verilerek okunarak diziye aktarılacaktır.Bu veriler birbirine 
#karşılık gelenler ile toplanacak,toplam değerleri d dizisine aktarılacak.
#sonuçlar ekrana yazdırılacak

A=open("A.txt")
Averi=Areadlines()
for i in Averi:
    print(i)
B=open("B.txt")
Bveri=Breadlines()
for i in Bveri:
    print(i)
c=open("C.txt")
Cveri=Creadlines()
for i in Cveri:
    print(i)
D=[]
if(len(Averi)==len(Bveri)==len(Cveri)):
    for i in range(len(Averi)):
        D.append(int(Averi[i]+int(Bveri[i]+int(Cveri[i]))))
    print(D)