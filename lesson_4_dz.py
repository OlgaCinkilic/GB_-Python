# -*- coding: utf-8 -*-

"""
1. Реализовать скрипт, в котором должна быть предусмотрена функция расчёта 
заработной платы сотрудника. Используйте в нём формулу: 
(выработка в часах*ставка в час) + премия. 
Во время выполнения расчёта для конкретных значений 
необходимо запускать скрипт с параметрами.
"""
from sys import argv

script_name, first_param, second_param, third_param = argv

print("File name: ", script_name)
print("Param 1: ", first_param)
print("Param 2: ", second_param)
print("Param 3: ", third_param)

def pay_calc():
    x = float(input('Введите количество отработанных часов : '))
    y = float(input('Введите суммы оплаты труда за 1 час : '))
    c = float(input('Укажите размер премии - '))
    pay = x * y
    return pay + c
print(f'Размер заработной платы составил: {pay_calc() }')



"""
2. Представлен список чисел. Необходимо вывести элементы исходного списка, 
значения которых больше предыдущего элемента.
Подсказка: элементы, удовлетворяющие условию, оформить в виде списка. 
Для его формирования используйте генератор.
Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
Результат: [12, 44, 4, 10, 78, 123].
"""
result_list = []
my_list = [int(i) for i in input("Введите список чисел: ").split()]
for i in range(1, len(my_list)):
    if my_list[i] > my_list[i-1]:
        (result_list.append(list[i]))
print("Исходный список: ", my_list)
print("Список, элементы которого больше предыдущего: ", result_list)





"""
3. Для чисел в пределах от 20 до 240 найти числа, кратные 20 или 21.
Решите задание в одну строку.
Подсказка: используйте функцию range() и генератор.
"""

list = [i for i in range(20, 241) if i % 20 == 0 or i % 21 == 0]

print("Список чисел кратных 20 или 21 в диапазоне (20..240): ", list)


"""
4. Представлен список чисел. Определите элементы списка, не имеющие повторений.
Сформируйте итоговый массив чисел, соответствующих требованию. 
Элементы выведите в порядке их следования в исходном списке.
Для выполнения задания обязательно используйте генератор.
Пример исходного списка: [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11].
Результат: [23, 1, 3, 10, 4, 11]
"""
my_list = [2, 4, 5, 5, 5, 5, 6, 7, 8, 8, 8, 9]
print("Исходные элементы списка:", my_list)
new_list = [i for i in my_list if my_list.count(i) == 1]
print("Элементы списка, не имеющие повторений:", new_list)



"""
5. Реализовать формирование списка, используя функцию range() и 
возможности генератора.
В список должны войти чётные числа от 100 до 1000 (включая границы). 
Нужно получить результат вычисления произведения всех элементов списка.
Подсказка: использовать функцию reduce().
"""
from functools import reduce

list = [el for el in range(100, 1001) if el % 2 == 0]
print("Список чётных чисел в диапазоне [100..1000]:", list) 

def my_func(el_p, el):
    return el_p * el
print("Произведение всех элементов списка:", reduce(my_func, list))





"""
6. Реализовать два небольших скрипта:
итератор, генерирующий целые числа, начиная с указанного;
итератор, повторяющий элементы некоторого списка, определённого заранее.
Подсказка: используйте функцию count() и cycle() модуля itertools.
Обратите внимание, что создаваемый цикл не должен быть бесконечным. 
Предусмотрите условие его завершения. #### Например, 
в первом задании выводим целые числа, начиная с 3. 
При достижении числа 10 — завершаем цикл. 
Вторым пунктом необходимо предусмотреть условие, 
при котором повторение элементов списка прекратится.
"""

#1

from itertools import count

n = int(input("Введите целое число:"))

for el in count(n):
    if el > 10:
        break
    else:
        print(el)

#2

from itertools import cycle

b = 0
for el in cycle("ABC"):
    if b > 10:
        break
    print(el)
    b += 1






"""
7. Реализовать генератор с помощью функции с ключевым словом yield, 
создающим очередное значение. 
При вызове функции должен создаваться объект-генератор. 
Функция вызывается следующим образом: for el in fact(n). 
Она отвечает за получение факториала числа. 
В цикле нужно выводить только первые n чисел, начиная с 1! и до n!.
Подсказка: факториал числа n — произведение чисел от 1 до n. 
Например, факториал четырёх 4! = 1 * 2 * 3 * 4 = 24.
"""



from math import factorial

def factorial_gen(n):
    for i in range(n):
        print(i, end='! = ')
        yield factorial(i)

print("Программа вычисления факториала числа")
for el in factorial_gen(6):
    print(el)


