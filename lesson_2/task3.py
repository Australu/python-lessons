#Пользователь вводит месяц в виде целого числа от 1 до 12.
#Сообщить к какому времени года относится месяц (зима, весна, лето, осень). Напишите решения через list и через dict.

vremenagoda_list = ['Зима' , 'Весна', 'Лето', 'Осень']
vremenagoda_dict = {1:'Зима', 2:'Весна', 3:'Лето', 4:'Осень'}
month = int(input('Введите месяц от 1 до 12 и узнайте время года, которому он принадлежит'))
if month == 1 or month== 12 or month ==2 :
    print(f'Время года {vremenagoda_dict.get(1)}')
    print(f'Время года {vremenagoda_list[0]}')
elif month ==3 or month==4 or month ==5:
    print(f'Время года {vremenagoda_dict.get(2)}')
    print(f'Время года {vremenagoda_list[1]}')
elif month ==6 or month ==7 or month ==8:
    print(f'Время года {vremenagoda_dict.get(3)}')
    print(f'Время года {vremenagoda_list[2]}')
elif month ==9 or month ==10 or month ==11:
    print(f'Время года {vremenagoda_dict.get(4)}')
    print(f'Время года {vremenagoda_list[3]}')

#тут тоже не особо поняла условие задачи.