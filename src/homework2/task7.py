# Даны: три стороны треугольника. Требуется: проверить, действительно ли это стороны треугольника.
# Если стороны определяют треугольник, найти его площадь. Если нет, вывести сообщение о
# неверных данных.

a = float(input('Сторона треугольника, см'))
b = float(input('Сторона треугольника, см'))
c = float(input('Сторона треугольника, см'))
if a + b > c and b + c > a and c + a > b:
    if a > 0 and b > 0 and c > 0:
        p = (a + b + c) / 2
        square = (p * (p - a) * (p - b) * (p - c)) ** 0.5
        print('triangle,', 'square =', square)
else:
    print('invalid data, not triangle')
