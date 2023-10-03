first_value = ""
tabuada = 8

for i in range(1,10):
    first_value = first_value + str(i)
    print(f"{first_value} x {tabuada} + {i} = {int(first_value)*tabuada+i}")