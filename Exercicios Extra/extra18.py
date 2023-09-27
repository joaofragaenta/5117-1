

def single_occurence():
    #Para o caso de "000" só contar como 1 ocorrência de "00"
    user_num = input("Escreva um número inteiro: ")

    was_last_zero = False
    double_zero_counter = 0

    for i in user_num:
        if i == "0":
            if was_last_zero == True:
                double_zero_counter += 1
                was_last_zero = False
            else:
                was_last_zero = True
        else:
            was_last_zero = False

    print(f"Ocorrências de \"00\": {double_zero_counter}")
    input("Prima ENTER para continuar")


def double_occurence():
    #Para o caso de "000" contar como 2 ocorrências de "00"
    user_num = input("Escreva um número inteiro: ")

    was_last_zero = False
    double_zero_counter = 0

    for i in user_num:
        if i == "0":
            if was_last_zero == True:
                double_zero_counter += 1
            else:
                was_last_zero = True
        else:
            was_last_zero = False

    print(f"Ocorrências de \"00\": {double_zero_counter}")
    input("Prima ENTER para continuar")

def zeroes_in_a_row():
    user_num = input("Escreva um número inteiro: ")

    was_last_zero = False
    longest_zero_streak = 0
    current_zero_streak = 0
    for i in user_num:
        if i == "0":
            if was_last_zero == True:
                current_zero_streak += 1
            else:
                was_last_zero = False
        else:
            if current_zero_streak > longest_zero_streak:
                longest_zero_streak = current_zero_streak

    if current_zero_streak > longest_zero_streak:
        longest_zero_streak = current_zero_streak
    
    print(f"O numero tem {longest_zero_streak} zeros seguidos")
    input("Prima ENTER para continuar")


while True:
    print("O exercicio não é claro com especificar se \"000\" conta como 1 ou 2 \"00\"")
    print("Abaixo está resolvido para se 000 só contar como 1 ocorrência de \"00\"")
    print("O exercicio também apresenta a frase \"O numero tem 3 zeros seguidos\" o que nem é o que pede")
    print("\n\n")
    print("1- \"000\" só conta como 1 ocorrência")
    print("2- \"000\" conta como 2 ocorrências")
    print("3- Para o caso de o exemplo estar correto e pede é o número máximos de zeros seguidos")

    user_input = int(input("Escolha uma opção: "))

    if user_input == 1:
        single_occurence()
    elif user_input == 2:
        double_occurence()
    elif user_input == 3:
        zeroes_in_a_row()
    else:
        print("Resposta inválida")
        input("Prima ENTER para continuar")
