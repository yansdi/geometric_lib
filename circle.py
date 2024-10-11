import math


def area(r):
    '''
    Возвращает площадь круга с радиусом r:

    Параметры:
             r (float) - радиус круга

    Возвращаемое значение:
             area (float) - площадь круга
    '''
    return math.pi * r * r


def perimeter(r):
    '''
    Возвращает периметр круга с радиусом r:

    Параметры:
             r (float) - радиус круга

    Возвращаемое значение:
             perimeter (float) - периметр круга
    '''

    return 2 * math.pi * r
