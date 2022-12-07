# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена 
# и записать в файл (или вывести в терминал) многочлен степени k.
# Пример:
# - k = 2  => 2*x² + 4*x + 5
# - k = 3  => 41*x^3 + 6*x² + 2*x + 98

from random import randint

k = int(input('Введите степень k: '))
for i in range(k, 0, -1):
    koef = randint(0, 100)
    if koef == 0:
        continue
    elif koef == 1:
        koef = ''
    else:
        koef = f'{koef}*x^{i} +' if i != 1 else f'{koef}*x +'
    print(koef, end=' ')
print(f'{randint(0, 100)} = 0')