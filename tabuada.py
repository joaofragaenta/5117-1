
for elemento2 in range(10):
    print(f"----- Tabuada dos {elemento2} -----")
    elemento1 = 1
    for elemento1 in range(10):
        print(f"{elemento2} x {elemento1} = {elemento1*elemento2}")
        elemento1 += 1
    elemento2 += 1