import random

a, b, c = 'hola', 'hola', 'hola'
#print(a, b, c)  # Output: 'h'
a1 = 'hola'
b1 = 'hola'
c1 = 'hola'
#print(a1, b1, c1)
a2, b2, c2, d = 'hola'
#print(a2, b2, c2, d)

lista = [11, 20, 3, 3, 4]
for value in lista:
    print(value)

tupla = (10, 20, 300, 4, 5, 6, 7, 8, 9)
for value in tupla:
    print(value)

conjunto = {"blue", "orange", "brown"}
for value in conjunto:
    print(value)

diccionario = {"Petru": 14, "Ana": 9, "Maria": 5}
for value in diccionario:
    contenido = diccionario[value]
    print(contenido)

numar = 1_000_000_000
print(f"{numar:,}".replace(",", "_"))

numar = random.randint(-99, 99)
print(numar)
