for i in range(1,101):
    print("i=",i)
################################

i=1
while i<=100:
    print("i=",i)
    i=i+1
################################
#çarpımtablosu1
i=1 
j=1 
while i<=10:
    while j<=10:
        sonuç=i*j
        print(i,"x",j,"=",sonuç)
        j=j+1
    j=1
    i=i+1
#çarpımtabloso2
for i in range(1,11):
    for j in range(1,11):
        sonuç=i*j
        print(i,"x",j,"=",sonuç)

################################

for i in range(1,1001):
    if(i%2==0):
        print(i)
for i in range(1,1001):
    if(i%3==0):
        print(i)
for i in range(i%4==0):
    print(i)
for i in range(1,1001):
    if(i%2==0) and (i%3==0) and (i%4==0):
        print(i)