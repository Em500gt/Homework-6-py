# -------------------------------------------------------------------------------------------------------------
# Уже при решении в ДЗ использовался list comprehension

# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

# Пример:

# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
from random import randint as rnd

def random_list(count):
    return [rnd(0, 10) for _ in range(int(count))]

def sum_odd(ls):
    result = 0
    for i in range(len(ls)):
        if i % 2 != 0:
            result += ls[i]
    return result

lst = random_list(input("Введите длину массива: "))
print(f"{lst} -> {sum_odd(lst)}")
