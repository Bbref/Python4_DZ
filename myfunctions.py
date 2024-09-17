def simple_separator():
    """
    Функция создает красивый разделитель из 10-и звездочек (**********)
    :return: **********
    """
    return '*' * 10
print("\nФункция №1")
print(simple_separator())

def long_separator(count):
    """
    Функция создает разделитель из звездочек, число которых можно регулировать параметром count.
    :param count: количество звездочек
    :return: строка разделитель
    """
    return '*' * count
print("\nФункция №2")

print(long_separator(20))
print(long_separator(3))

def separator(symbol, count):
    """
    Функция создает разделитель из любых символов любого количества.
    :param symbol: символ разделителя
    :param count: количество повторений
    :return: строка разделитель
    """
    return symbol * count
print("\nФункция №3")
print(separator('-', 10))  # True
print(separator('#', 5))
print(separator('*', 7))  # *******

def hello_world():
    """
    Функция печатает Hello World в формате:
    **********

    Hello World!

    ##########
    :return: None
    """
    print('**********')  # Верхний разделитель
    print('\nHello World!\n')  # Текст с отступами
    print('##########')  # Нижний разделитель
print("\nФункция №4")
hello_world()

def hello_who(who='World'):
    """
    Функция печатает приветствие в красивом формате.
    **********

    Hello {who}!

    ##########
    :param who: кого мы приветствуем, по умолчанию World
    :return: None
    """
    print('**********')  # Верхний разделитель
    print(f'\nHello {who}!\n')  # Приветствие с переданным именем
    print('##########')  # Нижний разделитель
print("\nФункция №5")
hello_who()        # Приветствие по умолчанию
hello_who('Max')   # Приветствие с именем "Max"
hello_who('Kate')  # Приветствие с именем "Kate"

def pow_many(power, *args):
    """
    Функция складывает любое количество цифр и возводит результат в степень power.
    :param power: степень
    :param args: любое количество цифр
    :return: результат вычисления
    """
    return sum(args) ** power
print("\nФункция №6")
print(pow_many(1, 1, 2) == 3)  # True -> (1 + 2)**1 == 3
print(pow_many(1, 2, 3) == 5)  # True -> (2 + 3)**1 == 5
print(pow_many(2, 1, 1) == 4)  # True -> (1 + 1)**2 == 4
print(pow_many(3, 2) == 8)     # True -> 2**3 == 8
print(pow_many(2, 1, 2, 3, 4) == 100)  # True -> (1 + 2 + 3 + 4)**2 == 10**2 == 100

def print_key_val(**kwargs):
    """
    Функция выводит переданные параметры в виде key --> value
    :param kwargs: любое количество именованных параметров
    :return: None
    """
    for key, value in kwargs.items():
        print(f"{key} --> {value}")
print("\nФункция №7")
# Примеры использования
print_key_val(name='Max', age=21)
# Вывод:
# name --> Max
# age --> 21

print_key_val(animal='Cat', is_animal=True)
# Вывод:
# animal --> Cat
# is_animal --> True

def my_filter(iterable, function):
    """
    Функция фильтрует последовательность iterable и возвращает новую,
    содержащую только те элементы, для которых function возвращает True.
    :param iterable: входная последовательность
    :param function: функция фильтрации
    :return: новая отфильтрованная последовательность
    """
    return [item for item in iterable if function(item)]

print("\nФункция №8")
# Примеры использования
print(my_filter([1, 2, 3, 4, 5], lambda x: x > 3))
print(my_filter([1, 2, 3, 4, 5], lambda x: x > 3) == [4, 5])  # True
print(my_filter([1, 2, 3, 4, 5], lambda x: x == 2) == [2])  # True
print(my_filter([1, 2, 3, 4, 5], lambda x: x != 3) == [1, 2, 4, 5])  # True
print(my_filter(['a', 'b', 'c', 'd'], lambda x: x in 'abba') == ['a', 'b'])  # True
