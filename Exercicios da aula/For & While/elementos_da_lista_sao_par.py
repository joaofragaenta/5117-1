#Python 3

lista = [10,20,20,15,5,60,140,80,40]
print(lista)

index = 0

for i in lista:
    if i >= 20:
        if i%2 != 0:  
            lista[index] = float(i/2)
        else:
            lista[index] = int(i/2)

    index = index + 1

print(lista)
