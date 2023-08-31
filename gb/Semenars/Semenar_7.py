# """
# Планеты вращаются вокруг звезд по эллиптическим орбитам. Назовем самой далекой
# планетой ту, орбита которой имеет самую большую площадь.
# Напишите функцию find_farthest_orbit(list_of_orbits),
# которая среди списка орбит планет найдет ту, по которой вращается самая
# далекая планета. Круговые орбиты не учитывайте: вы знаете,
# что у вашей звезды таких планет нет, зато искусственные спутники были были
# запущены на круговые орбиты. Результатом функции должен быть кортеж,
# содержащий длины полуосей эллипса орбиты самой далекой планеты.
# Каждая орбита представляет из себя кортеж из пары чисел - полуосей ее эллипса.
# Площадь эллипса вычисляется по формуле S = 3.14*a*b,
# где a и b - длины полуосей эллипса. При решении задачи используйте списочные
# выражения. Подсказка: проще всего будет найти эллипс в два шага:
# сначала вычислить самую большую площадь эллипса, а затем найти и сам эллипс,
# имеющий такую площадь. Гарантируется, что самая далекая планета ровно одна
# """
# import random
#
# list_of_orbits = [(random.randint(10, 20), random.randint(5, 25)) for _ in
#                   range(10)]
#
#
# def find_farthest_orbit(list_of_orbits: list) -> tuple:
#     list_of_orbits = list(filter(lambda x: x[0] != x[1], list_of_orbits))
#     print(list_of_orbits)
#     areas_of_orbits = []
#     for i in range(len(list_of_orbits)):
#         areas_of_orbits.append(list_of_orbits[i][0] * list_of_orbits[i][1])
#     return list_of_orbits[areas_of_orbits.index(max(areas_of_orbits))]
#
#
# print(f'Самая далёкая планета: '
#       f'{find_farthest_orbit(list_of_orbits)}')
