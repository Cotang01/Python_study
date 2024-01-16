"""
Создайте вручную список с повторяющимися элементами.
✔ Удалите из него все элементы, которые встречаются дважды.
"""
import random
from collections import Counter

# Если все числа кроме одного встречаются дважды
data = [4, 4, 0, 3, 12, 41, 2, 322, 3, 12, 41, 322, 0]
num = 0

# Использование побитового XOR
for i in data:
    num ^= i

print(data)
print([num])

data_2 = [random.randint(0, 10) for _ in range(25)]
print(data_2)

# Если числа должны повторяться больше 2 раз или не повторяться вовсе
print([k for k, v in Counter(data_2).items() if v != 2])
