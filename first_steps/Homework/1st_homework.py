# """
# Задача 2. Найдите сумму цифр трехзначного числа.
# """
#
# a = input('Введите трехзначное число: ')
# b = int(a[0])
# c = int(a[1])
# d = int(a[2])
#
# print(f'Сумма цифр будет равна: {b+c+d}')

# """
# Задача 4. Петя, Катя и Сережа делают из бумаги журавликов.
# Вместе они сделали S журавликов.
# Сколько журавликов сделал каждый ребенок, если известно, что
# Петя и Сережа сделали одинаковое количество журавликов,
# а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
# """
#
# s_all = int(input('Какое количество журавликов сделали Петя,
# Катя и Сережа вместе?: '))
# s_katya = int(s_all / 3 * 2)
# s_petya_or_serezha = int(s_all / 6)
# print(f'Катя сделала {s_katya} журавликов, а Петя и Сережа -
# по {s_petya_or_serezha} журавликов')
#
# """
# Задача 6. Вы пользуетесь общественным транспортом? Вероятно, вы
# расплачивались за проезд и получали билет с номером.
# Счастливым билетом называют такой билет с шестизначным номером,
# где сумма первых трех цифр равна сумме последних трех.
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6.
# Вам требуется написать программу, которая проверяет счастливость билета.
# """
#
# ticket = input('Введите шестизначный номер билета: ')
# a1 = int(ticket[0])
# a2 = int(ticket[1])
# a3 = int(ticket[2])
# a_sum = a1 + a2 + a3
# b1 = int(ticket[3])
# b2 = int(ticket[4])
# b3 = int(ticket[5])
# b_sum = b1 + b2 + b3
#
# if a_sum == b_sum:
#     print('Поздравляем! У вас счастливый билет.')
# if a_sum != b_sum:
#     print('Ваш билет не наделен магической силой :(')
#
# """
# Задача 8. Требуется определить, можно ли от шоколадки размером n × m
# долек отломить k долек, если разрешается сделать один разлом по прямой
# между дольками (то есть разломить шоколадку на два прямоугольника).
# """
#
# length = input('Какая длина у шоколадки?: ')
# width = input('Какая ширина у шоколадки?: ')
# part = input('Сколько долек вы хотите отломить?: ')
# size = int(length) * int(width)
# if int(part) <= int(size) and (int(part) % int(length) == 0
# or int(part) % int(width) == 0):
#     print('Можно')
# else:
#     print('Нельзя')
