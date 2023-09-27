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

def order_double_list(islands,vendas, ordem=1):
    #Ordenar ilhas por vendas de forma crescente
    sorting_done = False
    while sorting_done == False:
        sorting_done = True
        for i in range(len(islands)-1):
            if(vendas[i] > vendas[i+1] if ordem == 1 else vendas[i] < vendas[i+1]):
                vendas[i], vendas[i+1] = vendas[i+1], vendas[i]
                islands[i], islands[i+1] = islands[i+1], islands[i]
                sorting_done = False

    return islands, vendas

islands, vendas = order_double_list(islands,vendas)

print(f"\nIlhas com mais vendas:")
for i in range(len(vendas)):
    if(vendas[len(vendas)-i-1] == vendas[len(vendas)-1]):
        print(islands[len(vendas)-i-1] + " ")
    else:
        print(f"com {vendas[len(vendas)-1]}")
        break

print(f"\nIlhas com menos vendas:")
for i in range(len(vendas)):
    if(vendas[i] == vendas[0]):
        print(islands[i] + " ")
    else:
        print(f"com {vendas[0]}")
        break


#Apresenta as vendas das ilhas de forma crescente ao ler a lista em ordem
print("\n")
print("Crescente:")
for i in range(len(vendas)):
    print(f"{islands[i]} com {vendas[i]}")

#Apresenta as vendas das ilhas de forma decrescente ao ler a lista em ordem inversa
print("\n")
print("Decrescente:")
for i in range(len(vendas)):
    print(f"{islands[len(vendas)-1-i]} com {vendas[len(vendas)-1-i]}")


