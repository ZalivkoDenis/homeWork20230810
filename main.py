# ШАГ. Д/з по сроку 10/08/2023 © Денис Заливко

"""
Д/з по сроку 10/08/2023:
Алгоритм быстрой сортировки.
Написать функцию, которая реализует алгоритм "Быстрой сортировки".
Вводятся следующие параметры:
- количество значений (с использованием конструкции try-except)
- ввод чисел с клавиатуры (в список) (с использованием конструкции try-except)
"""
from functions import *
from quicksort import quicksort

count_items = input_int('Введите количество элементов: ')

print('-'*20)

alist = list()
for _ in range(count_items):
    alist.append(input_float(f'Введите элемент list[{_}] (int/float): '))

print('-'*20)

print('Unsorted list:\t\t', alist)
quicksort(alist, 0, len(alist))
print('Sorted list:\t\t', alist)
