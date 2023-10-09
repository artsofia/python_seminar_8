from return_data_file import data_file


def copy_file():
    data, nf = data_file()
    with open(f'db/copy_data_{nf}.txt', 'a', encoding='utf-8') as file:
        file.writelines(data)
    print("Данные файла успешно скопированы!")