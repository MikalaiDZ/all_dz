# 1. Выяснить тип результата выражений
# a = 15 * 3
# b = 15 / 3
# c = 15 // 2
# d = 15 ** 2
# print(a, "-", type(a), b, "-", type(b), c, "-", type(c), d, "-", type(d))

# 2. Дан список:
# ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
# Необходимо его обработать — обособить каждое целое число
# ['в', '"', '05', '"', 'часов', '"', '17', '"', 'минут', 'температура', 'воздуха', 'была', '"', '+05', '"', 'градусов']
# Сформировать из обработанного списка строку:
# в "05" часов "17" минут температура воздуха была "+05" градусов


# def get_sign(x):
#     if x[0] in "+-":
#         return x[0]
#
#
# my_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
# print(dir(my_list))
#
# i = 0
# while i < len(my_list):
#     sign = get_sign(my_list[i])
#     if my_list[i].isdigit() or (sign and my_list[i][1:].isdigit()):
#         if sign:
#             my_list[i] = sign + my_list[i][1:].zfill(2)
#         else:
#             my_list[i] = my_list[i].zfill(2)
#         my_list.insert(i, '"')
#         my_list.insert(i + 2, '"')
#         i += 2
#     i += 1
# print(my_list)
# print(" ".join(my_list))

# 4. Дан список, содержащий искажённые данные с должностями и именами сотрудников:
import copy
import math
from typing import List

# name_job = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА',
# 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
#
# for people in name_job:
#      i = people.split(',')
#      for name in i:
#          n = name.split(' ')
#      print(f'Привет, {n[-1].title()} !')

# 5.Создать вручную список, содержащий цены на товары (10–20 товаров)
prices = [5.88, 26, 17.5, 77, 115.3, 83.12, 31.2, 54.1, 6.52, 3]    # Пункт А., B.
prices.sort()
prices_copy = copy.deepcopy(prices)
i = 0
# for price in prices:
#     x = prices[i] * 100
#     r = math.floor(x // 100)
#     kk = math.floor(x % 100)
#     i += 1
#
#     print(f'{r} руб {kk} коп.', end=";")
prices_copy.reverse()                          # Пункт C.
for price in prices_copy:
    c = prices_copy[i] * 100
    r_c = math.floor(c // 100)
    kk_c = math.floor(c % 100)
    i += 1

    print(f'{r_c} руб {kk_c} коп.', end=";")
print(prices_copy[:5])
