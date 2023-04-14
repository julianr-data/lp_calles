def paralelas_a_1(num):

    # VERSION ORIGINAL
    # if len(num) in [1, 2, 3]:
    #     x = int(num[0])
    # elif len(num) == 4:
    #     x = int(num[0] + num[1])
    # else:
    #     print("No hay números de casas con tantas cifras")
    # res = (x*2)+32
    # if res > 52:
    #     res += 1
    # return res

    # VERSION CON DIVISION
    x = (int(num)//50)+32
    if x > 51:
        x +=1
        return x
    else:
        return x

def paralelas_a_32(num):
    # VERSION ORIGINAL
    # if len(num) in [1, 2, 3]:
    #     x = int(num[0])
    # elif len(num) == 4:
    #     x = int(num[0] + num[1])
    # else:
    #     print("No hay números de casas con tantas cifras")
    # res = (x*2)-5
    # return res

    # VERSION CON DIVISION (?)
    x = (int(num)//50)-5
    if x > 0:
        return x
    else:
        x = (x*(-1)) + 115
        return x


def diagonales_1(num):
    # VERSION VIEJA
    # if len(num) <= 3:
    #     x = int(num[0]) - 5
    #     if x > 0:
    #         return x
    #     else:
    #         x = (x*(-1)) + 115
    #         return x
    # elif len(num) == 4:
    #       x = int(num[0] + num[1]) - 5
    #       return x

    # VERSION CON DIVISION
    x = (int(num)//100)-5
    if x > 0:
        return x
    else:
        x = (x*(-1)) + 115
        return x

def diagonales_2(num):
    x = (int(num)//100)+14
    if x > 0:
        return x
    else:
        x = (x*(-1)) + 115
        return x

def diagonales_3(num):
    x = (int(num)//100) + 1
    if x > 0:
        return x
    else:
        x = (x*(-1)) + 115
        return x
