x = 2
y = 3
z = 4

xyz = []

for a in range(x):
    xyz.append([])
    for b in range(y):
        xyz[a].append([])
        for c in range(z):
            xyz[a][b].append([(c+1)+(b*z)+(a*y*z)])

print(xyz)            
            
