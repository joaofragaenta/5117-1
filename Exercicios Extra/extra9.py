final_number = 0
input_number = 0
while input_number >= 0:
    input_number = int(input("Escreava um dígito\n(-1 para terminar)"))

    if input_number >= 0:
        final_number = final_number * 10 + input_number

print(f"O número é {final_number}")


