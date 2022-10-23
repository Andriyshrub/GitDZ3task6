import math

def add(var1, var2):
    return var1 + var2


def subtract(var1, var2):
    return var1 - var2


def multiplication(var1, var2):
    return var1 * var2


def division(var1, var2):
    return var1 / var2


def degree(var1, var2):
    return var1 ** var2


def square_root(var1, var2):
    return math.sqrt(var1), math.sqrt(var2)


def cube_root(var1, var2):
    return (var1**(1/3)), (var2**(1/3))


def cosine(var1, var2):
    return math.cos(var1), math.cos(var2)


def sinus(var1, var2):
    return math.sin(var1), math.sin(var2)


def tangent(var1, var2):
    return math.tan(var1), math.tan(var2)


while True:
    var1 = int(input("Введіть перше число :"))
    var2 = int(input("Введіть друге число :"))
    print('Виберіть дію:\n \t1.Додавання\n \t2.Віднімання\n \t3.Множення\n \t4.Ділення\n'
          '\t5.Зведення в ступінь\n \t6.Квадартний корінь\n \t7.Кубічний корінь\n'
          '\t8.Косинус\n \t9.Синус\n \t10.Тангенс\n \t11.Вийти з програми')
    choice = int(input("Ваш вибір :"))
    if choice == 11:
        print('Дякуемо що скористались нашим калькулятором!')
        break
    elif choice == 1:
        print('Сума =', add(var1, var2))
    elif choice == 2:
        print('Різниця =', subtract(var1, var2))
    elif choice == 3:
        print('Добуток =', multiplication(var1, var2))
    elif choice == 4:
        if var2 == 0:
            print('Ділення на нуль неможливе!')
        else:
            print('Частка =', division(var1, var2))
    elif choice == 5:
        print('Ступінь =', degree(var1, var2))
    elif choice == 6:
        print('Квадратний корінь  =', square_root(var1, var2))
    elif choice == 7:
        print('Кубічний корінь  =', cube_root(var1, var2))
    elif choice == 8:
        print('Косинус =', cosine(var1, var2))
    elif choice == 9:
        print('Синус =', sinus(var1, var2))
    elif choice == 10:
        print('Тангенс =', tangent(var1, var2))
    else:
        print('Вибрана неправильна дія')
    pass