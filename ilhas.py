# 1. Cria uma lista com os nomes das ilhas do grupo central
islands = ["São Jorge", "Pico", "Terceira", "Faial", "Graciosa"]

# 2. Cria uma lista com 5 casas, inicializadas a 0
vendas = [0,0,0,0,0]

# 3. Pede ao utilizador para inserir vendas para cada ilha e apresenta o total de vendas
total = 0
for island_index in range(len(islands)):
    island_sales = ""
    
    while(island_sales.isnumeric() == False):
        island_sales = input(f"Insira vendas para a ilha {islands[island_index]}:\n")
    
    vendas[island_index] = int(island_sales)
    total = total + int(island_sales)

print(f"Total de vendas:\n{total}")


#Média de vendas
average = total / len(islands)
print(f"Media: {average}")

#Ilha(s) que venderam mais
max = vendas[0]
max_islands = []
for i in range(len(vendas)):
    if vendas[i] > max:
        max_islands = []
        max_islands.append(islands[i])
        max = vendas[i]
    elif vendas[i] == max:
        max_islands.append(islands[i])

print(f"Ilha(s) com mais vendas: {max_islands} com {max} vendas")


#Acima da média
above_average_islands = []
for i in range(len(vendas)):
    if vendas[i] > average:
        above_average_islands.append(islands[i])

print(f"Ilha(s) acima da média de vendas: {above_average_islands}")

#Abaixo da média
below_average_islands = []
for i in range(len(vendas)):
    if vendas[i] < average:
        below_average_islands.append(islands[i])

print(f"Ilha(s) abaixo da média de vendas: {below_average_islands}")



#Ordenar islhas por vendas de forma crescente
for i in range(len(islands)):
    for i in range(len(islands)-i-1):
        if i+1 < len(islands):
            if(vendas[i] > vendas[i+1]):
                vendas[i], vendas[i+1] = vendas[i+1], vendas[i]
                islands[i], islands[i+1] = islands[i+1], islands[i]

print("\n")
print("Crescente:")
for i in range(len(vendas)):
    print(f"{islands[i]} com {vendas[i]}")

print("\n")
print("Decrescente:")
for i in range(len(vendas)):
    print(f"{islands[len(vendas)-1-i]} com {vendas[len(vendas)-1-i]}")


