"""
Exercicio com lista
"""

lista = [10,20,30,40,50,60,70,80,90]

max = lista[0]
min = lista[0]

max_index = 0
min_index = 0

current_index = 0

for i in lista:
    if i > max:
        max = i
        max_index = current_index
    if i < min:
        min = i
        min_index = current_index

    current_index = current_index + 1

print ("Numero máximo é " + str(max) + " na casa " + str(max_index))
print ("Numero mínimo é " + str(min) + " na casa " + str(min_index))