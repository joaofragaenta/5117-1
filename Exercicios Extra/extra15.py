print("Insira uma série de números")
print("-1 para terminar")

user_num = 0
total = ""
while user_num != "-1":
    user_num = (input("->"))
    if int(user_num) != -1:
        total = total + user_num

print(f"{total}")