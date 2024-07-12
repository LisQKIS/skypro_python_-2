import math
def square(side):
    area = side * side
    area = math.ceil(area)
    return area

print(square(5.5)) # Ожидаемый результат: 31