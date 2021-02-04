#2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.


list = ['boom\n', 'bim\n']
with open("test2.txt", 'w+') as file_obj:
    file_obj.writelines(list)
with open("test2.txt") as file_obj:
    lines = 0
    letters = 0
    for line in file_obj:
        lines += line.count("\n")
        letters = len(line)-1
        print(f"{letters} букв в строке")
    print(f"Итог {lines}")