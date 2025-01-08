#zadanie 1
def write_text_to_file():
    with open('user_input.txt', 'a') as file:
        text = input('Введите текст для добавления в файл: ')
        file.write(text + '\n')

    with open('user_input.txt', 'r') as file:
        content = file.read()
    return content


file_input = write_text_to_file()
print(file_input)

#zadanie 2
def read_file():
    print('Выберите одну из кнопок:')
    print('1. Чтение всего файла сразу')
    print('2. Построчное чтение файла')
    number = input('Введите 1 или 2: ')

    if number == '1':
        try:
            with open('example.txt', 'r') as file:
                content = file.read()
            return content
        except FileNotFoundError:
            return ('Файл не найден')

    elif number == '2':
        try:
            with open('example.txt', 'r') as file:
                strings_list = []
                for line in file:
                    strings_list.append(line)
                return ''.join(strings_list)
        except FileNotFoundError:
            return ('Файл не найден')

    else:
        print('Некорректный выбор')
        read_file()


file_content = read_file()
print(file_content)
