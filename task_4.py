# 4- Напишите программу, которая будет преобразовывать десятичное число в двоичное. 
# Подумайте, как это можно решить с помощью рекурсии.

n_str = ""
n_input = int(input("Введите число: "))
while n_input != 0:
    n_str = str(n_input%2) + n_str
    n_input //=2
print(n_str)