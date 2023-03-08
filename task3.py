import os


def merge_txt_files():
    txt_list = [i for i in os.listdir() if i.endswith('.txt') and i.split('.')[0].isdigit()]
    merge_txt = {}

    for file in txt_list:  # создание нового словаря из ключей и подставка к нему значений (сортировка)
        merge_txt[file] = open(file, encoding='utf-8').readlines()

    sorted_dict = {}
    sorted_keys = sorted(merge_txt, key=merge_txt.get)
    print(sorted_keys.reverse())
    for w in sorted_keys:
        sorted_dict[w] = merge_txt[w]
    print(sorted_dict)

    with open('all_data.txt', 'w+', encoding='utf-8') as f:
        for key, value in sorted_dict.items():
            f.write(f'{key}\n')
            f.write(f'{len(value)}\n')
            f.writelines(' '.join(value))
            f.write('\n\n')


merge_txt_files()