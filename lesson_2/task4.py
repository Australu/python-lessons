#4. Пользователь вводит строку из нескольких слов, разделённых пробелами. Вывести каждое слово с новой строки.
# Строки необходимо пронумеровать. Если в слово длинное, выводить только первые 10 букв в слове.

stroka = input("Введите строку  из нескольких слов, разделенных пробелами ")
probel = stroka.split(' ')
for a, slovo in enumerate(probel, 1):
    if len(slovo) > 10:
        slovo = slovo[0:9]
    print(f"{a} - {slovo}")