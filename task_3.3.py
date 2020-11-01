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