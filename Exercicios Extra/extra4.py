seconds = float(input("Escreva o número de segundos:"))

days = int(seconds/60/60/24)
hours = int((seconds/60/60) - (days*24))
minutes = int(seconds/60 - (days*24*60) - (hours*60))
leftover_seconds = int((seconds - (days*24*60*60) - (hours*60*60) - (minutes*60)))


print(f"dias: {days} horas: {hours} mins: {minutes} segs: {18}")