percentagem_seg_social = 0.11

escaloes_hora = [[0,1], [40,1.5], [60,2]]

escaloes_comissao = [[10000,0.01], [20000,0.02], [30000,0.03] , [40000,0.04], [50000,0.05]]

#
# Calcular salário por hora
#
def calcular_salario():
    nome = input("Qual o seu nome? ")
    horas = int(input("Quantas horas trabalhou? "))
    preco_hora = float(input("Quanto ganha à hora? "))
    vendeu = int(input("Quanto vendeu? "))
    
    salario = calc_salario_horas(horas, preco_hora)

    comissao = calc_comissoes(vendeu, escaloes_comissao)

    desconto_seg_soc = calc_desconto(salario, comissao, percentagem_seg_social)

    #
    # Calculo salario liquido
    #

    salario_liquido = calc_salario_liquido(salario,comissao, desconto_seg_soc)

    print(f"{nome} trabalhou {horas} horas a {preco_hora}€/h para um total de {salario}€")
    print(f"Ganhou {comissao}€ de comissões")
    print(f"Descontou {desconto_seg_soc}€ para a segurança social")
    print(f"Salario liquido final de {round(salario_liquido,2)}€")




#
# Calculo de salario
#
def calc_salario_horas(horas, preco_hora, escaloes=[]):
    salario = 0
    horas = horas
    while(horas > 0):
        for i in range(len(escaloes_hora)):
            if horas > escaloes_hora[len(escaloes_hora)-i-1][0]:
                salario += ((horas - escaloes_hora[len(escaloes_hora)-i-1][0]) * preco_hora * escaloes_hora[len(escaloes_hora)-i-1][1])
                horas = horas - (horas - escaloes_hora[len(escaloes_hora)-i-1][0])
        
    return salario


#
# Calculo de comissões
#
def calc_comissoes(vendas, escaloes_comissao):
    comissao = 0
    #escaloes_comissao = [[10000,0.01], [20000,0.02], [30000,0.03] , [40000,0.04], [50000,0.05]]
    for i in range(len(escaloes_comissao)):
        if (len(escaloes_comissao)-i-1-1 >= 0):
            if vendas >= escaloes_comissao[len(escaloes_comissao)-i-1][0]:
                comissao = comissao + (vendas - escaloes_comissao[len(escaloes_comissao)-i-1-1][0]) * escaloes_comissao[len(escaloes_comissao)-i-1][1]
                vendas = vendas - (vendas - escaloes_comissao[len(escaloes_comissao)-i-1-1][0])
            elif vendas >= escaloes_comissao[len(escaloes_comissao)-i-1-1][0]:
                comissao = comissao + (vendas - escaloes_comissao[len(escaloes_comissao)-i-1-1][0]) * escaloes_comissao[len(escaloes_comissao)-i-1][1]
                vendas = vendas - (vendas - escaloes_comissao[len(escaloes_comissao)-i-1-1][0])

        else:
            comissao = comissao + vendas*(escaloes_comissao[0][1])
    return comissao




#
# Calculo de desconto
#
def calc_desconto(salario,comissao,percentagem):
    return (salario + comissao) * percentagem_seg_social


def calc_salario_liquido(salario, comissao, desconto_seg_soc):
    return salario + comissao - desconto_seg_soc

calcular_salario()
