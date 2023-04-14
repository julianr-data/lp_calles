print()

## FUNCIONES ##
from funcs import *

## CASOS ##
from tipos_de_calle import casos

## INPUTS ##
calle = int(input("Número de calle: "))
casa = input("Número de casa: ")

## DECISION ##
# error: casa entre 12 y 13 la ve como entre 11 y 12, pero casa entre 11 y 12 ok. 10 y 11 error, 9 y 10 ok, etc.
# mismo problema en par1
# diag 73 n 1065 da numeros negativos!

if calle in casos.par1:
    result = paralelas_a_1(casa)
elif calle in casos.par32:
    result = paralelas_a_32(casa)
elif calle in casos.diag1:
    result = diagonales_1(casa)
elif calle in casos.diag2:
    result = diagonales_2(casa)
elif calle in casos.diag3:
    result = diagonales_3(casa)
else:
    print("Calle no contenida dentro del algoritmo")

print(f"El domicilio o edificio en cuestión se encuentra entre las calles {result} y {result+1}")
