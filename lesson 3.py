# 1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

def my_division(a,b):
    try:
        res = a/b
        print('Результат:', round(res,3))
        return res
    except ZeroDivisionError:
        print('Деление на ноль невозможно')

result = my_division(a=int(input('Деление a/b, введите a:')),b=int(input('Деление a/b, введите b:')))


# 2. Выполнить функцию, которая принимает несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон. Функция должна принимать параметры
# как именованные аргументы. Осуществить вывод данных о пользователе одной строкой.

def data_str(name,lastname,dob,city,email,phone):
    li =[name, lastname, dob, city, email, phone]
    res_str = " ".join(map(str,li))
    return res_str
print(data_str(name='hghg', phone=12544788,lastname='hhh', dob=2000, email='hhh@bbb.ty', city='spb'))

# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента
# и возвращает сумму наибольших двух аргументов.

def my_func(a,b,c):
    li = [a, b, c]
    li.sort(reverse=True)
    res = int(li[0]) + int(li[1])
    return res

print(my_func(3,8,2))


# 4. Программа принимает действительное положительное число x и целое отрицательное число y.
# Выполните возведение числа x в степень y. Задание реализуйте в виде функции my_func(x, y).
# При решении задания нужно обойтись без встроенной функции возведения числа в степень.
# Подсказка: попробуйте решить задачу двумя способами. Первый — возведение в степень с помощью оператора **.
# Второй — более сложная реализация без оператора **, предусматривающая использование цикла.

def my_func(x, y):
    s = abs(y)
    i = 1
    f = 1
    while i <= s:
       i= i+1
       f = f/1/x
    print(f)

my_func(x=3,y=-3)


# 5. Программа запрашивает у пользователя строку чисел, разделённых пробелом. При нажатии Enter должна выводиться
# сумма чисел. Пользователь может продолжить ввод чисел, разделённых пробелом и снова нажать Enter.
# Сумма вновь введённых чисел будет добавляться к уже подсчитанной сумме.
# Но если вместо числа вводится специальный символ, выполнение программы завершается.
# Если специальный символ введён после нескольких чисел, то вначале нужно добавить сумму этих чисел
# к полученной ранее сумме и после этого завершить программу.
def my_print():
    num = 0
    while True:
        sum_str = input('sum_str:').split()
        try:
            for el in sum_str:
                    if el == '%':
                        print('Остановка по знаку %')
                        return
                    else:
                        num = num + int(el)
        except ValueError:
            print('Введите цифры или %')
        print(num)

my_print()


# 6. Реализовать функцию int_func(), принимающую слова из маленьких латинских букв и возвращающую их же,
# но с прописной первой буквой.
# Например, print(int_func(‘text’)) -> Text.

def int_func(text):
    li = list(text)
    for el in li:
        if ord(el) > 122 or ord(el) < 97:
            print('введены не маленькие латинские буквы')
        else:
            capi = str(text).capitalize()
            return capi



# 7. Продолжить работу над заданием. В программу должна попадать строка из слов, разделённых пробелом.
# Каждое слово состоит из латинских букв в нижнем регистре.
# Нужно сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы.
# Используйте написанную ранее функцию int_func()./

def int_func(text):
    li = list(text)
    for el in li:
        if ord(el) > 122 or ord(el) < 97:
            print('введены не маленькие латинские буквы')
        else:
            capi = str(text).capitalize()
            return capi

row_= input("Введите строку на английском языке: ").split()
new_row = []
try:
    for el in row_:
       new_row.append(int_func(el))
    str_new = ' '.join(new_row)
    print(str_new)
except TypeError:
    print("Введите англиийские буквы")

