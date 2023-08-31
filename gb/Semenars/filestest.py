# file = open('C:\\Users\\Sasha\\PycharmProjects\\pythonProject'
#             '\\Semenars\\phone_numbers.txt', 'r', encoding='UTF-8')
# contacts = file.read()
# if contacts.endswith(';'):
#     contacts = contacts.rstrip(contacts[-1])
# contacts_structured = contacts.split(';')
# dict1 = {}
# index1 = 1
# index2 = 2
# for i in range(0, len(contacts_structured), 3):
#     dict1.setdefault(contacts_structured[i], (contacts_structured[index1],
#                       contacts_structured[index2]))
#     i += 3
#     index1 += 3
#     index2 += 3
# print(dict1)
# index3 = 1
# # for k, v in dict1.items():
# #     print(f"\t\nПользователь №{index3} {k}")
# #     print(f"\tНомер телефона: {v[0]}")
# #     print(f"\tДоп. информация: {v[1]}")
# #     index3 += 1
# file.close()

# file = open('C:\\Users\\Sasha\\PycharmProjects\\pythonProject'
#              '\\Semenars\\phone_numbers.txt', 'r+', encoding='UTF-8')
# lines = file.read().split('\n')
# remove_contact = input('Введите ФИО контакта: ')
# file.seek(0)
# file.truncate()
# for i in lines:
#     if remove_contact not in i:
#         file.write(f'{i}\n')
# lines.pop()
# file.close()



#
# file = open('C:\\Users\\Sasha\\PycharmProjects\\pythonProject'
#              '\\Semenars\\phone_numbers.txt', 'r+', encoding='UTF-8')
# contacts = file.read()
# if contacts.endswith(';'):
#     contacts = contacts.rstrip(contacts[-1])
# contacts_structured = contacts.split(';')
# contacts_structured_new = contacts.split('\n')
# while contacts_structured_new[0] == '':
#     contacts_structured_new.remove('')
# dict1 = {}
# index1 = 1
# index2 = 2
#
# for i in range(0, len(contacts_structured), 3):
#     dict1.setdefault(contacts_structured[i],
#                     (contacts_structured[index1],
#                      contacts_structured[index2]))
#     i += 3
#     index1 += 3
#     index2 += 3
# print(dict1)
# print(contacts_structured)
# print(contacts_structured_new)
# file.close()
#
# file1 = open('C:\\Users\\Sasha\\PycharmProjects\\pythonProject'
#                 '\\Semenars\\phone_numbers.txt', 'r+', encoding='UTF-8')
#
# lines = file1.read().split('\n')
# remove_contact = input('\nВведите ФИО редактируемого контакта: ')
# file1.seek(0)
# file1.truncate()
# for i in lines:
#     if remove_contact not in i:
#         file1.write(f'\n{i}')
# for line in file1:
#     if not line.isspace():
#         file1.write(line)
#
# info_to_change = input('\nКакие данные будем менять? (ФИО, номер, инфа): ')
# if info_to_change.upper() == 'ФИО':
#     new_name = input('\nКакими будут новые ФИО?: ')
#     file1.write(f'\n{new_name}; ')
#     print(contacts_structured)
#     print(contacts_structured_new)
#     for k, v in dict1.items():
#         if remove_contact in k:
#             ph_inf = dict1.get(k)
#             file1.write(f'{ph_inf[0]}; {ph_inf[1]};')
# elif info_to_change.upper() == 'НОМЕР':
#     new_phone = input('Напишите новый номер: ')
#     file1.write(f'\n{remove_contact}; {new_phone};')
#     for k, v in dict1.items():
#         if remove_contact in k:
#             inf_write = dict1.get(k)[1]
#             file1.write(f'{inf_write};')
# elif info_to_change.upper() == 'ИНФА':
#     new_info = input('Напишите новые данные: ')
#     file1.write(f'\n{remove_contact}')
#     for k, v in dict1.items():
#         if remove_contact in k:
#             phone_write = dict1.get(k)[0]
#             file1.write(f'{phone_write}; {new_info};')
#
# file1.close()


# file = open('C:\\Users\\Sasha\\PycharmProjects\\pythonProject'
#              '\\Semenars\\phone_numbers.txt', 'r+', encoding='UTF-8')
# contacts = file.read()
# if contacts.endswith(';'):
#     contacts = contacts.rstrip(contacts[-1])
# contacts_structured = contacts.split(';')
#
# dict1 = {}
# index1 = 1
# index2 = 2
#
# for i in range(0, len(contacts_structured), 3):
#     dict1.setdefault(contacts_structured[i],
#                     (contacts_structured[index1],
#                      contacts_structured[index2]))
#     i += 3
#     index1 += 3
#     index2 += 3
#
# print(dict1)
#
# user_search = input('Введите ФИО искомого контакта: ')
# for k, v in dict1.items():
#     if user_search in k:
#         print(f'Данные этого пользователя следующие: '
#               f'\nТелефон: {dict1.get(k)[0]}'
#               f'\nДоп. инфа: {dict1.get(k)[1]}')
#
# file.close()


