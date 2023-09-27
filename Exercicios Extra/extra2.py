d = input("Qual a distância percorrida (em Km)")
t = input("Qual o tempo que demorou a percorrer (em minutos)")

d_metros = d * 1000
t_segundos = t *60
t_horas = t/60

print("A velocidade média é de:")
print(f"{d/t_horas} Km/h")
print(f"{d_metros/t_segundos} m/s")
