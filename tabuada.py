
elemento1 = 1
elemento2 = 1
while elemento2 < 10:
    print(f"----- Tabuada dos {elemento2} -----")
    elemento1 = 1
    while elemento1 < 10:
        print(f"{elemento2} x {elemento1} = {elemento1*elemento2}")
        elemento1 += 1
    elemento2 += 1