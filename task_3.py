# 3-Задайте список из вещественных чисел. Напишите программу, 
# которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

print('Введите количество чисел в списке')
import random
n = int(input())
some_list = [round(random.randint(1,19) + random.random(),2) for _ in range(n)]
print(some_list, end = '')
list2 = [i%1 for i in some_list if i%1 != 0]
print('\n Ответ =>', round((max(list2) - min(list2)), 2))