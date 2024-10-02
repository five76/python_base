import math

def triangle(*args):
    """
    Вычисление площади треугольника
    """

    if len(args) == 3:
        a, b, c = args 
        p = (a + b + c) / 2
        s = math.sqrt(p * (p - a) * (p - b) * (p - c))
        return s
    elif len(args) == 2:
         a, b = args
         return 1 / 2 * a * b
    else:
        print('Некорректный ввод данных')

def  сircle(r):
    """
    Вычисление площади круга
    """

    return math.pi * r * r