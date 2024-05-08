# первая функция: создаю кортеж, состоящий из количества строк в файле и имени файла

def count_lines(file_name):
    with open(file_name, encoding='utf-8') as f:
        lines = f.readlines()
        num = len(lines)
    return (num, file_name)


# вторая функция: на входе список из названий файлов, создается отсортированный список кортежей из предыдущей функции
def sorting(files_list):
    new_files_list = []
    for fi in files_list:
        counted = count_lines(fi)
        new_files_list.append(counted)
    return sorted(new_files_list)


# третья функция: создает файл
def create_new_file(files_list):
    files_list = sorting(files_list) # сортировка файлов с помощью предыдущей функции
    for file in files_list:  # проходимся по файлам
        with open('sorted_files.txt', 'a', encoding='utf-8') as new_file:
            with open(file[1], encoding='utf-8') as old_file:  # открываем каждый файл и записываем в новый файл
                text = old_file.read()
                new_file.write(f'{file[1]}\n{file[0]}\n{text}\n')


# исполняем :)
create_new_file(['1.txt', '2.txt', '3.txt'])