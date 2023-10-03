import random
quantos = int(input("Quantos?\n"))
inicio = int(input("Inicio?\n"))
fim = int(input("Fim?\n"))

numeros = []
pares = 0
primos = 0

for i in range(quantos):
    numeros.append(random.randint(inicio, fim))

for i in numeros:
    par = False
    if i % 2 == 0:
        par = True
        pares +=1
    elif i == 2 or not(i%2 == 0):
        primo = True
        if primo == True:
            for x in range(3,i,2):
                if(i % x == 0):
                    primo = False
                    break
        
        if primo == True:
            print(f"{i} é primo")
            primos +=1


print("------------------------")
print(f"{numeros}")
print(f"Há {pares} numeros pares")
print(f"Há {quantos - pares} numeros impares")
print(f"Há {primos} numeros primos")