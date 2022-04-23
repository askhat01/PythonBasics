#1. Создать программный файл в текстовом формате, записать в него построчно данные, вводимые пользователем. 
#Об окончании ввода данных будет свидетельствовать пустая строка.

my_file = open("file_1.txt", 'w', encoding='utf-8')

line = " "
while line:
    line = input('Введите данные для записи в файл. \n Для окончания ввода введите пустую строку')
    my_file.write(f"{line}\n") if line != '' else my_file.close()

# 2. Создать текстовый файл (не программно), сохранить в нём несколько строк, выполнить подсчёт строк и слов в каждой строке.

with open("file_2.txt", "r", encoding='utf-8') as f_obj:
    my_line = [f'{line}. {count.strip()} - {len(count.split())} слов'
                for line, count in enumerate(f_obj, 1)]
    print(*my_line, f"Всего строк - {len(my_line)}.", sep="\n")

# 3. Создать текстовый файл (не программно). Построчно записать фамилии сотрудников и величину их окладов (не менее 10 строк). 
# Определить, кто из сотрудников имеет оклад менее 20 тысяч, вывести фамилии этих сотрудников. 
# Выполнить подсчёт средней величины дохода сотрудников.

with open('file_3.txt', 'r', encoding='utf-8') as f:
    employees_dict = {line.split()[0]: float(line.split()[1]) for line in f}
    print(f'Average salary = {round(sum(employees_dict.values()) / len(employees_dict), 3)}\n'
          f'Employees with salary less than 20k {[e[0] for e in employees_dict.items() if e[1] < 20000]}')

# 4. Создать (не программно) текстовый файл со следующим содержимым: One — 1, Two — 2, Three — 3, Four — 4.
# Напишите программу, открывающую файл на чтение и считывающую построчно данные. 
# При этом английские числительные должны заменяться на русские. Новый блок строк должен записываться в новый текстовый файл.

my_dict = {"One": "Один", "Two": "Два", "Three": "Три", "Four":"Четыре"}

with open("file_4_1.txt", "w", encoding='utf-8') as new_file:
    with open("file_4.txt", encoding='utf-8') as my_file:
        new_file.writelines([line.replace(line.split()[0], my_dict.get(line.split()[0])) for line in my_file])

# 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделённых пробелами. 
# Программа должна подсчитывать сумму чисел в файле и выводить её на экран.

from random import randint
from textwrap import wrap

with open("file.txt", "w", encoding="utf-8") as my_file:
    my_list = [randint(1,100) for _ in range(100)]
    my_file.write(" ".join(map(str, my_list)))

print(f"Sum of elements - {sum(my_list)}")
 
# 6. Сформировать (не программно) текстовый файл. В нём каждая строка должна описывать учебный предмет и наличие лекционных, 
# практических и лабораторных занятий по предмету. Сюда должно входить и количество занятий. 
# Необязательно, чтобы для каждого предмета были все типы занятий.
# Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести его на экран.

my_dict = {}
with open("file_6.txt", encoding="utf-8") as fobj:
    for line in fobj:
        name, stats = line.split(':')
        name_sum = sum(map(int, "".join([i for i in stats if i == ' ' or '9' >= i >= '0']).split()))
        my_dict[name] = name_sum
print(f"{my_dict}")

# 7. Создать вручную и заполнить несколькими строками текстовый файл, в котором каждая строка будет содержать данные о фирме: 
# название, форма собственности, выручка, издержки. 
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль. 
# Если фирма получила убытки, в расчёт средней прибыли её не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью. 
# Если фирма получила убытки, также добавить её в словарь (со значением убытков).

import json

with open("my_ex_f.json", "w", encoding="utf-8") as write_f, open("file_7.txt", encoding="utf-8") as f_obj:
    profit = {line.split()[0]: int(line.split()[2]) - int(line.split()[3]) for line in f_obj}
    result = [profit, {"average_profitn": round(sum([int(i) for i in profit.values() if int(i) > 0]) /
                                                len([int(i) for i in profit.values() if int(i) >0]))}]
    json.dump(result, write_f, ensure_ascii=False, indent=4)