user_num = float(input("Insira uma quantia: "))
money_quants = [50,20,10,5,2,1,0.50,0.20,0.10,0.05,0.02,0.01]
money = [0,0,0,0,0,0,0,0,0,0,0,0]

while user_num > 0:
    for i in range(len(money_quants)):
        while user_num >= money_quants[i]:
            money[i] +=1
            print(f"{user_num} - {money_quants[i]} = {user_num - money_quants[i]} ")
            user_num = round(user_num - money_quants[i],2) # É necessário usar a função de python round() para evitar point percision errors

print("Serão necessários(as):")
for i in range(len(money)):
    if money[i] > 0:
        if money_quants[i] >= 5: #Notas
            print(f"{money[i]} nota(s) de {money_quants[i]} euros")
        elif money_quants[i] >= 1: 
            print(f"{money[i]} moeda(s) de {money_quants[i]} euro(s)")
        else: #Moedas de centimos
            print(f"{money[i]} moeda(s) de {int(money_quants[i]*100)} cêntimo(s)")