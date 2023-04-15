from funcs import *
from street_types import casos

## INPUTS ##
# calle = int(input("Número de calle: "))
# casa = input("Número de casa: ")

def Decision(calle, casa):
    result = False
    print("entre en la funcion decision")
    print(calle)
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
    # print(f"El domicilio o edificio en cuestión se encuentra entre las calles {result} y {result+1}")
    return result
