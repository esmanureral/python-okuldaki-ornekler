#range#
print(list(range(10)))
print(*range(10))
print(*range(2,5))

for sayi in range(10):
    if sayi>5:
        print(sayi)

#enumerate#
harfler=['a','b','C']
for harf in enumerate(harfler):
 print(harf)

 harfler=['a','b','c']
 for index,harf in enumerate(harfler):
    print(index,harf)

    #zip#
ülkeler=['tr','fr','de']
siralamalar=range(1,4)
for ülke in zip (ülkeler,siralamalar):
    print(ülke)