#2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.



def my_inform (name, surname, year, city, email, telephone):
    return ' '.join([name, surname, year, city, email, telephone])
print(my_inform(surname = 'Kartashova', name = 'Jul', year = '1993', city = 'Moscow', email = 'australu@yandex.ru', telephone = '89540954944'))