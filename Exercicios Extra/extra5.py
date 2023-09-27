from math import sqrt

input_numbers = [0,0,0,0,0]

for i in range(5):
    input_number = None
    while(type(input_number) == type(None)):
        input_number = int(input(f"Insira o {i+1}º número real: "))
    input_numbers[i] = input_number


array_sum = 0

for i in input_numbers:
    array_sum = array_sum + i

average = array_sum / len(input_numbers)


temp_dev = 0

for i in input_numbers:
    temp_dev = temp_dev + (i - average)*(i- average)

standard_dev = sqrt(0.25 * temp_dev)

print(f"Média: {average}")
print(f"Desvio Padrão: {standard_dev}")