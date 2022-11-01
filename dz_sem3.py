#Задача №22. Задайте список из нескольких чисел. Напишите программу,
#которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# import random
# sum = 0
# list = []
# for _ in range(2,random.randint(3,11)):
#     list.append(random.randint(1,10))
# print(list)
# for i in range(len(list)):
#     if i % 2 != 0:
#         sum += list[i]
# print(sum)

#Задача №23. Напишите программу, которая найдёт произведение пар чисел списка.
#Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# import random
# list = []
# for _ in range(2,random.randint(3,11)):
#     list.append(random.randint(1,10))
# print(list)
# compozition = []
# while len(list) != 0:
#     if len(list) == 1:
#         compozition.append(list[0]*list[0])
#         list.pop(0)
#     else:
#         compozition.append(list[0]*list[-1])
#         list.pop(0)
#         list.pop(-1)
# print(compozition)

#Задача №24 Задайте список из вещественных чисел. Напишите программу, 
# которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# import random
# list = []
# for _ in range(2,random.randint(3,11)):
#     list.append(round(random.uniform(1,10),2))
# print(list)
# max = list[0]-int(list[0])
# min = list[1]-int(list[1])
# for i in range(len(list)):
#     if list[i]-int(list[i]) > max:
#         max = list[i]-int(list[i])
#     elif list[i]-int(list[i]) < min:
#         min = list[i]-int(list[i])
# print(round(max, 2))
# print(round(min, 2))
# print(round((max - min), 2))

#Задача №25. Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# print(bin(int(input('Введите число: '))))