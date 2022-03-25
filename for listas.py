import random

frutas=["Mora","Fresa","Sandia","Piña","Uva"]
#          0      1        2       3      4
precioxlb=[0.50, 1.0, 1.55, 1.20, 2.0]
print("Lista de frutas con precio menor a 1.50")
for i in range(len(frutas)):
    fruta=frutas[i]
    precio=precioxlb[i]
    if precio < 1.50:
        print(fruta)

premios=["lapiz","computadora","carro","pluma","televisor"]
aleatorio=random.choice(premios)
print(aleatorio)
ingreso=input("Ingrese un premio: ")
cond= aleatorio == ingreso
print("¿Gano?",cond)
