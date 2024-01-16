print(f'\n{"ТАБЛИЦА УМНОЖЕНИЯ" : ^70}')
for i in range(2, 11):
    for j in range(2, 6):
        print(f'{j :^3} x {i :^3} ={i*j :^5}', end='   ')
    print()
print()
for i in range(2, 11):
    for j in range(6, 10):
        print(f'{j : ^3} x {i :^3} ={i*j :^5}', end='   ')
    print()
