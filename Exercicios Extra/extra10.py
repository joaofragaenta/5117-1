number_string = input("Escreva um inteiro: ")
final_number = 0

for i in range(len(number_string)):
    if(int(number_string[i])%2 == 1):
        final_number = final_number * 10 + int(number_string[i])

print(f"Resultado: {final_number}")