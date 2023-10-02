ilhas = ["Terceira","Graciosa", "Pico", "São Jorge", "Faial"]
vendas= [
    [14,18,5,140,5], #Gasolina
    [30,52,25,15,10] #Gasoleo
]

vendas_por_ilha = [0] * (len(ilhas))

total = 0
total_gasolina = 0
total_gasoleo = 0

for x in range(len(vendas)):
    for i in range(len(vendas[x])):
        if x == 0:
            total_gasolina += vendas[x][i]
            vendas_por_ilha[i] += vendas[x][i]
        if x == 1:
            total_gasoleo += vendas[x][i]
            vendas_por_ilha[i] += vendas[x][i]


for i in range(len(ilhas)):
    print(f"Vendas de combustivel para a ilha {ilhas[i]}: {vendas_por_ilha[i]}")

print(f"Total Gasolina: {total_gasolina}")
print(f"Total Gasoleo: {total_gasoleo}")