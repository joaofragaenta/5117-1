
vendas = [
    #OR CT  OC
    [1, 2,  3],
    [4, 5,  6],
    [7, 8,  9],
    [10,11, 12]
],[
    #OR CT OC
    [13,14,15],
    [16,17,18],
    [19,20,21],
    [22,23,24]
],

print("---------------XYZ-----------------")
total1 = 0
for x in range(len(vendas)):
    total2 = 0
    for y in range(len(vendas[x])):
        total3 = 0
        for z in range(len(vendas[x][y])):
            total1 += vendas[x][y][z]
            total2 += vendas[x][y][z]
            total3 += vendas[x][y][z]
        print(f"total3 = {total3}")
    print(f"total2 = {total2}")
print(f"total1 = {total1}")


print("---------------XZY-----------------")
total1 = 0
for x in range(len(vendas)):
    total2 = 0
    for z in range(len(vendas[x][y])):
        total3 = 0
        for y in range(len(vendas[x])):
            total1 += vendas[x][y][z]
            total2 += vendas[x][y][z]
            total3 += vendas[x][y][z]
        print(f"total3 = {total3}")
    print(f"total2 = {total2}")
print(f"total1 = {total1}")

print("---------------YXZ-----------------")
total1 = 0
for y in range(len(vendas[x])):
    total2 = 0
    for x in range(len(vendas)):
        total3 = 0
        for z in range(len(vendas[x][y])):
            total1 += vendas[x][y][z]
            total2 += vendas[x][y][z]
            total3 += vendas[x][y][z]
        print(f"total3 = {total3}")
    print(f"total2 = {total2}")
print(f"total1 = {total1}")

print("---------------YZX-----------------")
total1 = 0
for y in range(len(vendas[x])):
    total2 = 0
    for z in range(len(vendas[x][y])):
        total3 = 0
        for x in range(len(vendas)):
            total1 += vendas[x][y][z]
            total2 += vendas[x][y][z]
            total3 += vendas[x][y][z]
        print(f"total3 = {total3}")
    print(f"total2 = {total2}")
print(f"total1 = {total1}")

print("---------------ZXY-----------------")
total1 = 0
for z in range(len(vendas[x][y])):
    total2 = 0
    for x in range(len(vendas)):
        total3 = 0
        for y in range(len(vendas[x])):
            total1 += vendas[x][y][z]
            total2 += vendas[x][y][z]
            total3 += vendas[x][y][z]
        print(f"total3 = {total3}")
    print(f"total2 = {total2}")
print(f"total1 = {total1}")

print("---------------ZYX-----------------")
total1 = 0
for z in range(len(vendas[x][y])):
    total2 = 0
    for y in range(len(vendas[x])):
        total3 = 0
        for x in range(len(vendas)):
            total1 += vendas[x][y][z]
            total2 += vendas[x][y][z]
            total3 += vendas[x][y][z]
        print(f"total3 = {total3}")
    print(f"total2 = {total2}")
print(f"total1 = {total1}")