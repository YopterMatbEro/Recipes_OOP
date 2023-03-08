# f = open('hello.txt', encoding='utf-8')
# res = f.read()
# print(res)
# print(type(res))
# print()
# f.close()

# f = open('hello.txt', encoding='utf-8')
# r1 = f.readline().strip()
# r2 = f.readline().strip()
# print(r2, r1, sep='\t\t')
# print(f.readline())
# f.close()

# f = open('hello.txt', encoding='utf-8')
# result = f.readlines()
# print(result)
# second_string = result[1]
# print(second_string)
# f.close()

# Запись в файл
# w - перезапись
#запись по одной строке (write())
# f = open('file2.txt', 'w', encoding='utf-8')
# f.write('Привет, Лунатикам! Стоп. Опять?\n')
# f.write('Желаю всем хорошего вечера!\n')
# f.close()

#запись нескольких строк списком (writelines())
# f = open('file2.txt', 'w')
# f.writelines(['Hello world!\n', 'Today is a good day\n'])
# f.close()

# a - дозапись
# lines = ['Wish you all the best!\n', 'Goodbye\n']
# f = open('file3.txt', 'a')
# f.writelines(lines)
# f.close()

# f = open('file3.txt', 'r+')
# f.write('Test data\n')
# f.close()

# f = open('file3.txt', 'a+')
# f.seek(0)
# content = f.read()
# print(content)
# f.write('End!')
# f.close()

# пути
#относительный путь
# f = open('test_folder/File5', 'w')
# f.write('Hello world!')
# f.close()

#абсолютный путь
# f = open(r'C:\Users\Uzver\PycharmProjects\HomeWorks\OOP_Paradigm_2\file4.txt', 'w', encoding='utf-8')
# f.write('Всем привет!')
# f.close()

# import os
# current = os.getcwd()
# # print(current)
# # split_path = os.path.split(current)
# folder = 'OOP_Paradigm_2'
# file_name = 'file4.txt'
# full_path = os.path.join(current, folder, file_name)
# # print('\n\t\t\t\t', full_path)
#
# f = open(full_path, 'w')
# f.write(('Test data for path!'))
# f.close()

# URL = 'https://www.industrialempathy.com/img/remote/ZiClJf-1920w.jpg'
# import requests
#
# with open('sunrise.jpg', 'wb') as f:
#     response = requests.get(URL)
#     f.write(response.content)
#
# try:
#     f = open('image.jpg', 'wb')
#     response = requests.get(URL)
#     f.write(response.content)
# except Exception:
#     f.close()

# __enter__
# __exit__

# from pprint import pprint
# with open('recipe.txt', 'rt', encoding='utf-8') as file:
#     recipes = {}
#     for line in file:
#         recipe_name = line.strip()
#         ingredients_count = int(file.readline())
#         ingredients = []
#         for _ in range(ingredients_count):
#             name, count, elem = file.readline().strip().split(' | ')
#             ingredients.append({
#                 'name': name,
#                 'count': count,
#                 'elem': elem
#             })
#             recipes[recipe_name] = ingredients
#         file.readline()
#     pprint(recipes, sort_dicts=False)