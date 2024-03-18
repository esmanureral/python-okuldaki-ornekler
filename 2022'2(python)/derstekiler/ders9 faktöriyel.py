#iteratif faktöriyel hesabı

def faktöriyelbulma(n):
    sonuç=1 
    for i in range(1,n+1):
        sonuç=sonuç*i
    return sonuç
  
print(faktöriyelbulma(6))
print(faktöriyelbulma(4))

#rekürsif faktöriyel hesabı

def Rfaktöriyelhesabı(n):
    if n==1 :
        return 1 
    else:
        return n*Rfaktöriyelhesabı(n-1)
print(Rfaktöriyelhesabı(5))
print(Rfaktöriyelhesabı(4))
