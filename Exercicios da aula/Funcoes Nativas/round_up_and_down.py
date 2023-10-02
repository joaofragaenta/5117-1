import math

numero = input("Insira um numero com casas decimais: ")
numero_fixed = ""
for i in range(len(numero)):
    if numero[i] == ',':
        numero_fixed += '.'
    else:
        numero_fixed += numero[i]

numero_floor = math.floor(float(numero_fixed))
numero_ceil = math.ceil(float(numero_fixed))

print(f"O numero arredondado para cima dá: {numero_ceil}")
print(f"O numero arredondado para baixo dá: {numero_floor}")
        

