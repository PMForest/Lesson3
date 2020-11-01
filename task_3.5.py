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