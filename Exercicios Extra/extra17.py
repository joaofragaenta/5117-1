notas = [2,14,16,4,10,15,6,8,9,2,4]

positivas = 0
for i in notas:
    if i >= 10:
        positivas +=1
    
percentagem = positivas/len(notas) * 100

print(f"Houve {positivas} positivas")
print(f"Percentagem de positivas: {percentagem}%")