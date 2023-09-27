number_string = input("Escreva um inteiro: ")
final_number = 0

for i in range(len(number_string)):
    final_number = final_number * 10 + int(number_string[len(number_string)-i-1])

print(f"O número invertido é: {final_number}")