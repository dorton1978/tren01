year_pushkin = int(input('Введите год рождения А.С. Пушкина: '))
if year_pushkin == 1799:
    print('Верно!')
    day_pushkin = input('Введите день рождения А.С. Пушкина: ')
    if day_pushkin == '6' or day_pushkin == '6 июня' or day_pushkin == '6.06' or day_pushkin == '6.6':
        print('Верно!')
    else:
        print('Неверный день рождения')
else:
    print('Неверный год')