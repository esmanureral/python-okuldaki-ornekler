def karesini_al(x):
    return x**2
sayilar=[*range(1,6)]
print(sayilar)
for index in range(len(sayilar)):
    sayilar[index]=karesini_al(sayilar[index])
print(sayilar)


