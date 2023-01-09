# А.С. Пушкин 1799
# Д.И. Менделеев 1834
# Никола Тесла 1856
# Зигмунд Фрейд 1856
# Генри Форд 1863
people = ['А.С. Пушкин', 'Д.И. Менделеев', 'Никола Тесла', 'Зигмунд Фрейд', 'Генри Форд']
years = [1799, 1834, 1856, 1856, 1863]
all_answer = len(people)
print('ИГРА -ВИКТОРИНА-')
while True:
    print()
    correct_answer = 0
    for i in range(all_answer):
        inp_year = int(input('В каком году родился ' + people[i] + ': '))
        if inp_year == years[i]:
            correct_answer += 1
    print()
    error_answer = all_answer - correct_answer
    print('Количество правильных ответов:', correct_answer)
    print('Количество ошибок:', error_answer)
    print('Процент правильных ответов, %:', correct_answer * 100 / all_answer)
    print('Процент неправильных ответов, %:', error_answer * 100 / all_answer)
    print()

    ask = input('Хотите начать игру сначала (да / нет) :')
    if ask == 'нет':
        break
