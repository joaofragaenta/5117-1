nome = input("Qual o seu nome? ")
numero_original= int(input("Insira um numero para calcular o fatorial: "))


#
# While loop
#
numero = numero_original
resultado = 1
while numero > 0:
    resultado = resultado * numero
    numero -=1

print(f"Caro(a), {nome} o fatorial de {numero_original} é {resultado}")



#
# Recursivo
#

def fatorial(numero):
    if numero-1 > 0:
        return numero * fatorial(numero-1)
    else:
        return 1
    
print(f"Caro(a), {nome} o fatorial de {numero_original} é {fatorial(numero_original)}")

