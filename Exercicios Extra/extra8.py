input_number = 0
while input_number >= 0:
    input_number = int(input("Escreva um número de segundos: "))
    try:
        input_number -1
    except Exception as e:
        print(e)
    
    print(f"O número de dias correspondente é {input_number /60 /60 / 24}")

