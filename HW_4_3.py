# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной 
# последовательности.(Вывод тех элементов, которые были без повторов)
# Ввод: 1 2 3 2 4 4
# Вывод: 1 3

numbers = [int(i) for i in input('Введите числа через пробел: ').split()]
result = []
for i in numbers:
    if numbers.count(i) == 1:
        result.append(i)
print('Список чисел, встречающихся один раз: ', *result)

