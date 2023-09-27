user_num = input("Insira um número: ")

total = 0
for i in user_num:
    total = total + int(i)

print(f"O total dos dígitos do numero é: {total}")