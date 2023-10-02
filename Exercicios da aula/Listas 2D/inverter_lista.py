import random

list = [10,20,7,4,20]
list_len = 25
min_random_number = 0
max_random_number = 100

#for i in range(list_len):
#    list.append(random.randint(min_random_number,max_random_number))

print("Número de casas que está na lista:")
print (len(list))
print ('\n')


print("Sequência de números entre 0 e o número de casas da lista menos 1:")
for x in range(0, len(list)):
    print(x)
print ('\n')

print("Sequência de números entre o número de casas da lista menos 1 e 0:")
for y in reversed(range(0, len(list))):
    print(y)
print ('\n')


print("Lista inversa:")
index = len(list)-1
for y in range(len(list)):
    print(list[index])
    index = index-1
print ('\n')