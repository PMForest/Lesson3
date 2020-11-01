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