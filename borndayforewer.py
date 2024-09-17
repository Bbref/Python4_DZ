def check_answer(prompt, correct_answer):
    """
    Функция для проверки ответа пользователя.
    :param prompt: Текст запроса к пользователю
    :param correct_answer: Правильный ответ
    :return: Правильный ответ пользователя
    """
    answer = input(prompt)
    while answer != correct_answer:
        print("Не верно")
        answer = input(prompt)
    return answer


check_answer('Введите год рождения А.С.Пушкина: ', '1799')

# Проверка дня рождения
check_answer('В какой день июня родился Пушкин? ', '6')

print('Верно')
