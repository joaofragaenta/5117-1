lista = [10,40,20,50,60]

for i in enumerate(lista):
    index = i[0]
    if (index + 1) < len(lista):
        if lista[index] > lista[index+1]:
            temp = lista[index+1]
            lista[index+1] = lista[index]
            lista [index] = temp


print(lista)
