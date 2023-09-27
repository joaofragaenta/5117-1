first_value = ""

for i in range(1,10):
    first_value = first_value + str(i)
    print(f"{first_value} x 8 + {i} = {int(first_value)*8+i}")