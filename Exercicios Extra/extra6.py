max = None
for i in range(3):
    input_number = int(input(f"Insira o {i+1}º número:"))
    if type(max) == type(None):
        max = input_number
    elif max < input_number:
        max = input_number

print(f"O número máximo é {max}")