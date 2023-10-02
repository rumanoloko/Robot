import time

#tiempo_inicio = time.time()
#for x in range(100):
#    if x % 15 == 0:
#        print(x, " es multiplo de 3, 5 y 15")
#    elif x % 3 == 0:
#        print(x, " es multiplo de 3")
#    elif x % 5 == 0:
#        print(x, " es multiplo de 5")
tiempo_inicio = time.time()
for x in range(101):
    if x % 3 == 0:
        print(x, " es multiplo de 3")
    if x % 5 == 0:
        print(x, " es multiplo de 5")
    if x % 15 == 0:
        print(x, " es multiplo de 3, 5 y 15")

tiempo_final = time.time()

tiempo_total = time.time() - tiempo_inicio
print(f"{tiempo_inicio} \n {tiempo_final}")
print(tiempo_total)
alpha = 0.0010151863098144531
betha = tiempo_total