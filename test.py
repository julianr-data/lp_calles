# corre la funcion varias veces
# lista de inputs
# lista de outputs esperados
# lista vacia que se va llenando de outputs reales
# comparacion
# extraccion del caso en que


import os
from funcs import *
from tipos_de_calle import casos

class bcolors:
    OK = '\033[92m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

def bigtest(calle_user, numeros_user, ideal_user):
    street = calle_user
    inputs = numeros_user
    ideal_list = ideal_user
    real_list = []
    failed_positions = []


    def which_test(inps, street):
        test_id = False
        real = []
        if len(inps) != 0:
            for inp in inps:              # Llenar lista de resultados reales
                if street in casos.par1:
                    real.append(paralelas_a_1(str(inp)))
                    test_id = "paralelas_a_1"
                elif street in casos.par32:
                    real.append(paralelas_a_32(str(inp)))
                    test_id = "paralelas_a_32"
                elif street in casos.diag1:
                    real.append(diagonales_1(str(inp)))
                    test_id = "diagonales_1 [73, 74, 79, 80]"
                elif street in casos.diag2:
                    real.append(diagonales_2(str(inp)))
                    test_id = "diagonales_2 [75, 76]"
                elif street in casos.diag3:
                    real.append(diagonales_3(str(inp)))
                    test_id = "diagonales_3 [77, 78]"
        else:
            print(f"NO TESTS FOR {street}")
        return real, test_id

    def real_vs_ideal(real, ideal, inps):
        for i, inp in enumerate(inps):
            if real[i] == ideal[i]:
                print(f"{i}\t| num\t{inp}\t| expected\t{ideal[i]}\t| got\t{real[i]}\t--> "+bcolors.OK+"OK"+bcolors.ENDC)
            else:
                print(f"{i}\t| num\t{inp}\t| expected\t{ideal[i]}\t| got\t{real[i]}\t--> "+bcolors.FAIL+"FAIL"+bcolors.ENDC)
                failed_positions.append(i)
        if len(failed_positions) != 0:
            print(f"\nFailed at attemps no. {failed_positions}")

    real_list, testid = which_test(inputs, street)

    print(f"RUNNING TESTS FOR {street} | Test ID: {testid}\n")
    real_vs_ideal(real_list, ideal_list, inputs)
    print()


### RUN TESTS! ###

test_path = "test_cases/current_test.txt"

print("\nReading street, numbers and expected lower boundary from 'current_test.txt'")

for filename in os.listdir("test_cases"):
    filepath = os.path.join("test_cases", filename)
    # checking if it is a file
    if os.path.isfile(filepath):
        with open(filepath) as f:
            content = f.read().splitlines()

        calle = int(content[1])
        numeros = content[2].split(",")
        numeros = [int(i) for i in numeros]
        inferior_entre = content[3].split(",")
        inferior_entre = [int(i) for i in inferior_entre]

        bigtest(calle, numeros, inferior_entre)




##############################################################
# TO READ MANUALLY FROM TERMINAL:
# switch = True
# initialize calle, numeros and inferior_entre variables
# calle = int(input("Calle sobre la que probar la aplicación: "))
# while switch == True:
#     x = input(f"Ingrese un número en calle {calle}: ")
#     numeros.append(x)
#     y = input(f"Calle inferior entre las que se encuentra el número: ")
#     inferior_entre.append(y)
#     z = input("Type 's' and press Enter to start test, or any other key to continue adding numbers: ")
#     if z == "s":
#         switch = False
