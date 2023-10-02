import sys
import os
from Avus import Avus
from Fillium import Fillium
from Pater import Pater
#from Animal import Animal

#abus_obiectum = Avus()
#pater_obiectum = Pater()
#fillius_obiectum = Fillium()


if len(sys.argv) > 2:
    print("Excessus argumentum")
    sys.exit(0)
elif len(sys.argv) == 2:
    print('Hello ', sys.argv[1])
else:
    print('Sin argumento')

abus_obiectum = Avus()

pater_obiectum = Pater()

fillius_obiectum = Fillium()

#abus_obiectum.methodus_pro_populo()
#pater_obiectum.methodus_pro_populo()
#fillius_obiectum.methodus_pro_populo()

#ramus_avunguli = []
#ramus_avunguli.append(abus_obiectum)
#ramus_avunguli.append(pater_obiectum)
#ramus_avunguli.append(fillius_obiectum)

#for menbra in ramus_avunguli:
    #print(menbra.methodus_pro_populo())

fichero = os.path.abspath(sys.argv[0])
directorio_actual = os.path.dirname(fichero)
contenido_directorio = os.listdir(directorio_actual)
print('Contenido del directorio:')
for x in contenido_directorio:
    print(x)

x1 = os.path.splitdrive(fichero)
x2 = x1[0]
print("Ruta completa: ", x1)
print("Directorio raíz: ", x2)
print()

for x in x1:
    print("=>")
    print(x)

print("Final=>")









