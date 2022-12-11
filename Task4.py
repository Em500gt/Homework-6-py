# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Уже при решении в ДЗ использовался list comprehension

# Пример:

# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

from random import randint as rnd

def random_list(count):
    return [rnd(0, 10) for _ in range(int(count))]

def multiplication_pair(lst):
    st = len(lst) // 2 if len(lst) % 2 == 0 else len(lst) // 2 + 1
    s = [lst[i] * lst[len(lst) - i - 1] for i in range(st)]
    return s

lst = random_list(input("Введите длину массива: "))
print(f"{lst} -> {multiplication_pair(lst)}")