work_hours = int(input("Quantas horas trabalhou? "))
hourly_pay = int(input("Quanto recebe à hora? "))
payment = 0
if work_hours <= 40:
    payment = work_hours * hourly_pay
else:
    extra_hours = work_hours - 40
    payment = 40 * hourly_pay + (extra_hours * hourly_pay * 2)

print(f"Recebeu {payment} euros")