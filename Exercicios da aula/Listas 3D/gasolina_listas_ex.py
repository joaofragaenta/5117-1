import sys
vendas = [
    #-----------------------------------------------|
    #OR CT OC E1 E2 E3                              |
    [1, 2, 3,  5, 6, 7], #Primavera                 |
    [4, 5, 6,  7, 4, 2], #Verão                     |
    [7, 8, 9,  8, 6, 4], #Outono                    |
    [10,11,12, 3,14,67], #Inverno                   |---------2021
    [10,11,12,43,42,18], #Extra_season_1            |
    [10, 4,48,42,54,18], #Extra_season_2            |
    [10,11,12, 8, 6, 4], #Extra_season_3            |
    #-----------------------------------------------|

],[
    #-----------------------------------------------|
    #OR CT OC E1 E2 E3                              |
    [13,14,15,64,46,79], #Primavera                 |
    [16,17,18,23,42,63], #Verão                     |
    [19,20,21,32,45,67], #Outono                    |---------2022
    [22,23,24,12,45,68], #Inverno                   |
    [25,26,27,43,54,67], #Extra_season_1            |
    [22,29,28,12,13,14], #Extra_season_2            |
    [22,29,28,19,20,54]  #Extra_season_3            |
    #-----------------------------------------------|
],


seasons = ["Primavera", "Verão", "Outono", "Inverno", "Extra_season_1", "Extra_season_2", "Extra_season_3"]
island_groups = ["Oriental", "Central", "Ocidental", "Extra_group_1","Extra_group_2","Extra_group_3",]

#Vendas de Combustível
#1.Total
total_global = 0
for x in range(len(vendas)):
    for y in range(len(vendas[x])):
        for z in range(len(vendas[x][y])):
            total_global += vendas[x][y][z]

print(f"Total de Vendas: {total_global}")



#2.Total por estação
total_by_season = [0] * len(seasons)

for x in range(len(vendas)):
    for y in range(len(vendas[x])):
        for z in range(len(vendas[x][y])):
            total_by_season[y] += vendas[x][y][z]

print("----------------------------")
print("Por estação:")
for i in range(len(seasons)):
    print(f"Total {seasons[i]}: {total_by_season[i]}")

#3.Total por grupo
total_by_group = [0]* len(island_groups)

for x in range(len(vendas)):
    for y in range(len(vendas[0])):
        for z in range(len(vendas[0][0])):
            total_by_group[z] += vendas[x][y][z]

print("----------------------------")
print("Por Grupo:")
for i in range(len(island_groups)):
    print(f"Total {island_groups[i]}: {total_by_group[i]}")

print("----------------------------")
#4 Qual a estação que tem mais vendas
highest_sale_number_by_season = 0
estacao_com_mais_vendas = ""
for i in range(len(total_by_season)):
    if total_by_season[i] > highest_sale_number_by_season:
        highest_sale_number_by_season = total_by_season[i]
        estacao_com_mais_vendas = seasons[i]
    elif total_by_season[i] == highest_sale_number_by_season:
        estacao_com_mais_vendas += ", " + seasons[i]

print(f"Estação(ões) com mais vendas: {estacao_com_mais_vendas} com {highest_sale_number_by_season} vendas")

#5 Qual o grupo que vendeu menos
lowest_sale_number_by_group = total_by_group[0]+1
grupo_com_menos_vendas = ""
for i in range(len(total_by_group)):
    if total_by_group[i] < lowest_sale_number_by_group:
        lowest_sale_number_by_group = total_by_group[i]
        grupo_com_menos_vendas = island_groups[i]
    elif total_by_group[i] == lowest_sale_number_by_group:
        grupo_com_menos_vendas += ", " + island_groups[i]

print(f"Grupo(s) com menos vendas: {grupo_com_menos_vendas} com {lowest_sale_number_by_group} vendas")
