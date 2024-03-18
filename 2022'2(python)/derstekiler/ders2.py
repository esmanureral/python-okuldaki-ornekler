vize=int(input("vize notunu giriniz:"))
final=int(input("final notunu giriniz:"))
ortalama=((vize*0,4)+(final*0,6))
if final<45:
    HN="FF"
elif ortalama>=85:
    HN="AA"
elif ortalama>=75:
    HN="BA"
elif ortalama>=65:
    HN="BB"
else:
    HN="FF"
print("harf notu:",HN)

