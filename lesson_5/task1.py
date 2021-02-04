#1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.

list = []
while True:
    line = input("Введите: ")
    if line == '':
        print(list)
        exit()
    else:
        newline = line + '\n'
        list.append(newline)
    with open("test1.txt", "w") as file_obj:
        file_obj.writelines(list)