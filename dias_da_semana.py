semanas = [1,2,3,4]
dias = ["Segunda","Terça","Quarta","Quinta","Sexta"]

print(len(dias))

x=0
y=0
while y < len(semanas):
    print(f"---------Semana {semanas[y]}---------")
    x = 0
    while x < len(dias):
        print(f"Semana {semanas[y]} - {dias[x]}")
        x += 1
    y += 1
#for x in range(len(dias)):
#    print(dias[x])