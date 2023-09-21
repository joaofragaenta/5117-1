# Python 3

#importa a biblioteca "os" e define a variavel clear para ser uma função que limpa a consola
import os
clear = lambda: os.system('clear')

def aritmetica(op,a,b):
    if(op == "somar"):
        #Apresenta no ecrã o valor de "a" convertido para string, o sinal de mais, o valor de "b" convertido para string, o sinal de igual e o valor de a+b convertido para string
        print (str(a)+" + "+str(b)+" = " + str(a+b))
    elif(op == "sub"):
        #Apresenta no ecrã o valor de "a" convertido para string, o sinal de menos, o valor de "b" convertido para string, o sinal de igual e o valor de a-b convertido para string
        print (str(a)+" - "+str(b)+" = " + str(a-b))
    elif(op == "mult"):
        #Apresenta no ecrã o valor de "a" convertido para string, o sinal de multiplicação, o valor de "b" convertido para string, o sinal de igual e o valor de a*b convertido para string
        print (str(a)+" * "+str(b)+" = " + str(a*b))
    elif(op == "div"):
        #Apresenta no ecrã o valor de "a" convertido para string, o sinal de divisão, o valor de "b" convertido para string, o sinal de igual e o valor de a/b convertido para string
        print (str(a)+" / "+str(b)+" = " + str(a/b))


def menu():
    #Titulo
    print("CALCULADORA \n")

    #Apresenta as opções do menu
    print("Escolha uma operação:")
    print("somar")
    print("sub")
    print("mult")
    print("div")
    print("\n") # Linha extra

    menu_choice = input() # Recolhe o input do utilizador e guarda na variavel menu_choice

    return menu_choice # Retorna a escolha do menu



clear() # Limpa a consola
menu_choice = menu(); # Mostra o menu e guarda a escolha na variavel "menu_choice"



while True: #Loop infinito para o programa nunca desligar
    while(menu_choice not in ["somar", "sub", "mult", "div"]):
        menu_choice = menu()

    a = "" # Declara a variavel "a" como string para não ser null
    b = "" # Declara a variavel "b" como string para não ser null


    # Verifica se "a" é numérico, que nunca será da primeira vez pois "a" foi definido como string um pouco a cima
    # Enquanto não for numérico corre o seguinte bloco de código
    while(a.isnumeric() == False): 
        a = input("Escolha o primeiro valor:\n") #Pede o primeiro valor e guarda-o na variavel "a"

        # Verifica se "a" ainda não é numérico. Se ainda não for numérico o valor de "a" deve ser letras ou simbolos e por isso é inválido.
        # Enquanto inválido, informa o utilizador que o valor foi inválido e pede-o novamente
        while(a.isnumeric() == False): 
            a = input("Valor invalido. Insira novamente o primeiro valor:\n") #

    # Verifica se "b" é numérico, que nunca será da primeira vez pois "b" foi definido como string um pouco a cima
    # Enquanto não for numérico corre o seguinte bloco de código
    while(b.isnumeric() == False):
        b = input("Escolha o segundo valor:\n") #Pede o segundo valor e guarda-o na variavel "b"

        # Verifica se "b" ainda não é numérico. Se ainda não for numérico o valor de "b" deve ser letras ou simbolos e por isso é inválido.
        # Enquanto inválido, informa o utilizador que o valor foi inválido e pede-o novamente
        while(b.isnumeric() == False):
            b = input("Valor invalido. Insira novamente o segundo valor:\n")
    

    aritmetica(menu_choice, int(a),int(b)) # Corre a função aritmetica passando a operação, o valor a e o valor b 
    input("Pressione ENTER para continuar") # Pede um input qualquer mas não faz nada com ele, apenas pede que se toque no enter para continuar

    # Após o ENTER volta ao "while True" e corre o programa novamente







