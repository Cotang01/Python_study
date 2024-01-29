"""
✔ Напишите функцию, которая открывает на чтение созданные
в прошлых задачах файлы с числами и именами.
✔ Перемножьте пары чисел. В новый файл сохраните
имя и произведение:
✔ если результат умножения отрицательный, сохраните имя
записанное строчными буквами и произведение по модулю
✔ если результат умножения положительный, сохраните имя
прописными буквами и произведение округлённое до целого.
✔ В результирующем файле должно быть столько же строк,
сколько в более длинном файле.
✔ При достижении конца более короткого файла,
возвращайтесь в его начало.
"""


def solution():
    with open('task1.txt', mode='r', encoding='UTF-8') as file1:
        data1 = file1.readlines()
    with open('task2.txt', mode='r', encoding='UTF-8') as file2:
        data2 = file2.readlines()
    ptr1 = 0
    ptr2 = 0
    n = len(data1)
    m = len(data2)
    size = max(n, m)
    with open('task3.txt', mode='w', encoding='UTF-8') as file3:
        for _ in range(size):
            t1 = data1[ptr1].strip().split('|')
            t1 = int(t1[0]) * float(t1[-1])
            t2 = data2[ptr2].strip()
            ptr1 += 1
            ptr2 += 1
            if not ptr1 < n:
                ptr1 = 0
            if not ptr2 < m:
                ptr2 = 0
            if t1 < 0:
                data_to_write = f'{t2.lower()}|{abs(t1)}\n'
            else:
                data_to_write = f'{t2.upper()}|{round(t1)}\n'
            file3.write(data_to_write)
