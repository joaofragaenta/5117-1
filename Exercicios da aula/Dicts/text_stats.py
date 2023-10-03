texto = input("Escreava um pequeno texto para calculo de estatisticas: \n")

letter_occurence = {}
for letra in texto:
    if letra in letter_occurence:
        letter_occurence[str(letra).lower()] += 1
    elif not letra == ' ':
        letter_occurence[str(letra).lower()] = 1




#Quantas vezes aparece cada letra?
print("Ocorrência de letras:\n")
for i in letter_occurence:
    print(f"{i}: {letter_occurence[i]}")

#Quantas vezes aparece cada letra do maior para menor?

sorted_dict = {}
keys_to_ignore = []

for i in letter_occurence:
    highest_key = ""
    highest_value = 0
    for x in letter_occurence.keys():
        if letter_occurence[x] > highest_value and not (x in keys_to_ignore):
            highest_value = letter_occurence[x]
            highest_key = x
    sorted_dict[highest_key] = highest_value
    keys_to_ignore.append(highest_key)
print("------------------")
print("Quantas vezes aparece cada letra do maior para menor, utilizando um segundo dict?")
print(sorted_dict)

#[2 listas] Quantas vezes aparece cada letra do maior para menor?

letters = letter_occurence.keys()
occurences = letter_occurence.values()

while swapped == True:
    swapped = False
    if occurences[i] > occurences[i+1]:
        temp_occurence = occurences[i]
        temp_letter = letters[i]
        occurences[i] = occurences[i+1]
        letters[i] = letters[i+1]
        occurences[i+1] = temp_occurence
        letters[i+1] = temp_letter
        swapped = True

print("------------------")
print("Quantas vezes do maior para o menor, utilizando .keys() e .values()")
for i in range(len(letter_occurence)):
    print(f"{letters[i]}:{occurences[i]}")

#[lambda] Quantas vezes aparece cada letra do maior para menor?

sorted_dict = sorted(letter_occurence, reverse= True, key= lambda letter : letter_occurence[letter])
print("------------------")
print("Quantas vezes do maior para o menor, utilizando .sorted() e lambda")
for i in sorted_dict:
    print(f"{i}: {letter_occurence[i]}")