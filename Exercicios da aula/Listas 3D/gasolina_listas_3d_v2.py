
vendas = [
    [
        #PR VE  OU  IN
        [1, 4,  7,  10],
        [2, 5,  8,  11],
        [3, 6,  9,  12],
    ],
    [
        #PR VE  OU  IN
        [13,16, 19, 22],
        [14,17, 20, 23],
        [15,18, 21, 24],
    ]
]


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