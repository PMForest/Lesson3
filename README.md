# Lesson3
""" Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль. """


def my_del(*args):

    try:
        arg1 = int(input("Введите делимое: "))
        arg2 = int(input("Введите делитель: "))
        rez = arg1 // arg2
    except ValueError:
        return 'ОШИБКА!'
    except ZeroDivisionError:
        return "НА НОЛЬ ДЕЛИТЬ НЕЛЬЗЯ!"

    return rez

print(f'result {my_del()}')

""" Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
 имя, фамилия, год рождения, город проживания, email, телефон.
 Функция должна принимать параметры как именованные аргументы.
 Реализовать вывод данных о пользователе одной строкой. """

def my_user(name, surname, age, city,email, phone):
    return ' '.join([name, surname, age, city,email, phone])
print(my_user(name = 'Нафаня', surname = 'Гаврилов', age = '30', city = 'Мозамбик', email = 'GNafana@email.com',
              phone = '+1-333-222-77-88'))




""" Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов. """

def my_func(var_1, var_2, var_3):
    if var_1 >= var_2 and var_2 >= var_3:
        return var_1 + var_2
    elif var_1 > var_2 and var_1 < var_3:
        return  var_1 + var_3
    else:
        return var_2 + var_3

print(f'Result - {my_func(int(input("Введите 1 число: ")), int(input("Введите 2 число: ")), int(input("Введите 3 число: ")))}')



""" Программа принимает действительное положительное число x и целое отрицательное число y.
Необходимо выполнить возведение числа x в степень y. Задание необходимо реализовать в виде функции my_func(x, y).
При решении задания необходимо обойтись без встроенной функции возведения числа в степень.
     Подсказка: попробуйте решить задачу двумя способами. Первый — возведение в степень с помощью оператора **.
Второй — более сложная реализация без оператора **, предусматривающая использование цикла.
"""


def my_num (*args):

    try:
        x = int(input("Введите число: "))
        y = int(input("Введите степень: "))
        rez = x ** -y
    except ValueError:
        return 'ОШИБКА!'
    except ZeroDivisionError:
        return "НА НОЛЬ ДЕЛИТЬ НЕЛЬЗЯ!"

    return rez


print(f'результат {my_num()}')

# var 2
def my_num2 (*args):

    try:
        x = int(input("Введите число: "))
        y = int(input("Введите степень: "))
        rez = pow(x, -y)
    except ValueError:
        return 'ОШИБКА!'
    except ZeroDivisionError:
        return "НА НОЛЬ ДЕЛИТЬ НЕЛЬЗЯ!"

    return rez


print(f'результат {my_num2()}')

# var 3

def my_num3 (*args):

    try:
        x = int(input("Введите число: "))
        y = int(input("Введите степень: "))
        x, y = float(x), int(y)
        rez = x
        for i in range(abs(y) - 1):
            rez *= x
        return 1 / rez
    except ValueError:
        return 'Check value'
    except ZeroDivisionError:
        return "YOU CAN'T USE ZERO!"

print(f'результат {my_num3()}')


""" Программа запрашивает у пользователя строку чисел, разделенных пробелом.
При нажатии Enter должна выводиться сумма чисел. Пользователь может продолжить ввод чисел,
разделенных пробелом и снова нажать Enter. Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
Но если вместо числа вводится специальный символ, выполнение программы завершается.
Если специальный символ введен после нескольких чисел,
то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу. """

def my_summ (*args):
    exit = False
    result = 0
    while exit == False:
        numbers = input("Enter numbers or q to exit: ").split()
        rez_line = 0
        for num in numbers:
            if 'q' in num:
                exit = True
                break
            rez_line += int(num)
        result = result + rez_line
        print(f'Current sum is {result}')
    print(f'Final sum is {result}')

my_summ()


""" Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же,
но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.
Продолжить работу над заданием. В программу должна попадать строка из слов, разделенных пробелом.
Каждое слово состоит из латинских букв в нижнем регистре. Сделать вывод исходной строки,
но каждое слово должно начинаться с заглавной буквы.
Необходимо использовать написанную ранее функцию int_func(). """

def int_func(*args):
    text = input("Input words: ")
    print(text.title())
    return
int_func()
