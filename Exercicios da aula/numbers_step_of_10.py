
import random

list = []
list_len = 30
min_random_number = 0
max_random_number = 100

for i in range(list_len):
    list.append(random.randint(min_random_number,max_random_number))

print(list)

final_list = ([],[],[],[],[],[])

for i in list:
    if i <= 10:
        final_list[0].append(i)
    elif i <= 20:
        final_list[1].append(i)
    elif i <= 30:
        final_list[2].append(i)
    elif i <= 40:
        final_list[3].append(i)
    elif i <= 50:
        final_list[4].append(i)
    else:
        final_list[5].append(i)

print(f"Há {len(final_list[0])} números entre 0 e 10")
print(f"Há {len(final_list[1])} números entre 10 e 20")
print(f"Há {len(final_list[2])} números entre 20 e 30")
print(f"Há {len(final_list[3])} números entre 30 e 40")
print(f"Há {len(final_list[4])} números entre 40 e 50")
print(f"Há {len(final_list[5])} números maiores que 50")