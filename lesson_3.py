# 1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление. 
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

def func_div(a, b):
    try:
        div_result = a / b
        return round(div_result, 3)
    except ZeroDivisionError:
        return "Division by zero isn't allowed, enter a non-zero number, please!"
    except ValueError:
        return "Enter number, please!"

print(func_div(int(input("Enter 1st number: ")), int(input("Enter 2nd number: "))))

# 2. Выполнить функцию, которая принимает несколько параметров, описывающих данные пользователя: 
# имя, фамилия, год рождения, город проживания, email, телефон. 
# Функция должна принимать параметры как именованные аргументы. 
# Осуществить вывод данных о пользователе одной строкой.

def func_info(name, surname, birthday, city, email, phone):
    return(f"Name - {name}; Surname - {surname}; birthday - {birthday}; city - {city}; email - {email}; phone - {phone}")

print(func_info(name=input("Enter your name: "), surname=input("Enter your surname: "), birthday=input("Enter your birthday: "),
    city=input("Enter your city: "), email=input("Enter your email: "), phone=input("Enter your phone: ")))

#3. Реализовать функцию my_func(), которая принимает три позиционных аргумента и возвращает сумму наибольших двух аргументов.

def my_func(a, b, c):
    my_list = [a, b, c]
    try:
        my_list.remove(min(my_list))
        return sum(my_list)
    except TypeError:
        return "Enter number, please!"

print(my_func(1, 2, 3))

# 4. Программа принимает действительное положительное число x и целое отрицательное число y. 
# Выполните возведение числа x в степень y. Задание реализуйте в виде функции my_func(x, y). 
# При решении задания нужно обойтись без встроенной функции возведения числа в степень.

def func_pow(a, b):
    try:
        result = a**b
    except TypeError:
        return "Enter a float number and a negative power"
    return result

print(func_pow(2, -2))

# 5. Программа запрашивает у пользователя строку чисел, разделённых пробелом. 
# При нажатии Enter должна выводиться сумма чисел. Пользователь может продолжить ввод чисел, разделённых пробелом и снова нажать Enter. 
# Сумма вновь введённых чисел будет добавляться к уже подсчитанной сумме.
# Но если вместо числа вводится специальный символ, выполнение программы завершается. 
# Если специальный символ введён после нескольких чисел, то вначале нужно добавить сумму этих чисел к полученной ранее сумме и 
# после этого завершить программу.

def my_sum():
    sum_res = 0
    while True:
        number_list = input("Enter numbers, input 'q' to exit: ").split()
        for num in number_list:
            if num.lower() == "q":
                return sum_res
            else:
                try:
                    sum_res += int(num)
                except ValueError:
                    print("To exit enter - 'q'.")
        print(f'Current sum is {sum_res}')

print(my_sum())

# 6. Реализовать функцию int_func(), принимающую слова из маленьких латинских букв и возвращающую их же, но с прописной первой буквой. 
# Например, print(int_func(‘text’)) -> Text.
# 7. Продолжить работу над заданием. В программу должна попадать строка из слов, разделённых пробелом. 
# Каждое слово состоит из латинских букв в нижнем регистре. 
# Нужно сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы. 
# Используйте написанную ранее функцию int_func().

def func_int(word):
    latin_char = 'fsdfgfdgdfg'
    return word.title() if not set(word).difference(latin_char) else False

words = input('Enter a string of words separated by a space: ').split()
for w in words:
    result = func_int(w)
    if result:
        print(result, '')
