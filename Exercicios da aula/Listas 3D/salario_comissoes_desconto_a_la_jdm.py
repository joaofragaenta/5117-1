def calcular(tabela, valor, fator=1):

    resultado = 0

    for x in range(len(tabela[0])):

        if valor > tabela[0][x]:

            resultado += (valor - tabela[0][x]) * tabela[1][x] 

            valor = tabela[0][x] #Não necessita de cálculos

    return resultado * fator

 

 

nome = input('Nome? ')

salario = calcular([[60, 40, 0],[2, 1.5, 1]], int(input('Horas?')), float(input('Custo Hora? ')))

bonus = calcular([[40000, 30000, 20000, 10000, 0],[.05, .04, .03, .02, .01]], int(input('Vendas?')))

seg_soc = (salario + bonus)*0.11

 

print(f'Salário: {salario}')

print(f'Bónus: {bonus}')

print(f'Total: {salario + bonus}')

print(f'Segurança Social: {seg_soc}')

print(f'Valor a receber: {salario + bonus - seg_soc}')