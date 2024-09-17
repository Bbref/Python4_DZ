def print_menu():
    print('1. Пополнение счета')
    print('2. Покупка')
    print('3. История покупок')
    print('4. Выход')


def deposit(balance):
    amount = float(input('Введите сумму для пополнения счета: '))
    balance += amount
    print(f'Счет пополнен на {amount}. Текущий баланс: {balance}')
    return balance


def make_purchase(balance, history):
    amount = float(input('Введите сумму покупки: '))
    if amount > balance:
        print('Недостаточно средств на счете.')
    else:
        description = input('Введите название покупки: ')
        balance -= amount
        history.append((description, amount))
        print(f'Покупка "{description}" на сумму {amount} выполнена. Текущий баланс: {balance}')
    return balance, history


def show_history(history):
    if not history:
        print('История покупок пуста.')
    else:
        print('История покупок:')
        for description, amount in history:
            print(f'Название: {description}, Сумма: {amount}')


# Инициализация переменных
balance = 0
history = []

while True:
    # Печать меню
    print_menu()

    # Получение выбора пользователя
    choice = input('Выберите пункт меню: ')

    if choice == '1':
        # Пополнение счета
        balance = deposit(balance)

    elif choice == '2':
        # Покупка
        balance, history = make_purchase(balance, history)

    elif choice == '3':
        # История покупок
        show_history(history)

    elif choice == '4':
        # Выход из программы
        print('Выход из программы.')
        break

    else:
        print('Неверный пункт меню. Попробуйте снова.')
