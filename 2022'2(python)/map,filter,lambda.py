def kare(x):
    return x**2
sayilar = [*range(1,10)]
x=[*map(kare,sayilar)]
print(sayilar,x)