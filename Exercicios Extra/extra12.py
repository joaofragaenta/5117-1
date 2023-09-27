print("Qual o valor de x")
x = int(input("?"))
print("Qual o valor de n")
n = int(input("?"))


total = 1
last = 1
for i in range(0, n):

    last = last*(x/(i+1))
    total = total + last


print(f"{total}")