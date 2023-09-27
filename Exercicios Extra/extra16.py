user_num = input("Escreva um número para formar uma capicua: ")
capicua = user_num
for i in range(len(user_num)):
    capicua = capicua + user_num[len(user_num)-1-i]
print(f"Capicua: {capicua}")