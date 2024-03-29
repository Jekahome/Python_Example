# базовые типы: bool, int, float, complex и str.
# сложные типы: tuple,range,dictionary,list

from decimal import Decimal # Для корректной работы с дробной частью
import locale # модуль локализации
locale.setlocale(locale.LC_ALL, "")

'''
    bool
    int
    float
    complex
    str
'''

# bool --------------------------------------------------------------------------------------------------
isMarried = False # False True
isMarried = not 10 > 21 and 10 == 10 or 10 > 9

# int --------------------------------------------------------------------------------------------------
age = int(False)    # False = 0, True = 1
age = 21
age = int('21')
print(type(age)) # <class 'int'>

print(0o11)    # формат восьмеричной системы, 0o11 => 9 в десятичной системе (print выводит в 10-й системе)
print(0xFF)    # формат шестнадцатеричной системы, 0xFF => 255 в десятичной системе (print выводит в 10-й системе)
number = 0b101  # определяем число в двоичной форме
print(f"number = {number:0b}")  # number = 101


'''
** Справо налево
* / // % Слева направо
+ - Слева направо

number = 3 + 4 * 5 ** 2 + 7
number = (3 + 4) * (5 ** 2 + 7)
'''

'''
+= Присвоение результата сложения
-= Присвоение результата вычитания
*= Присвоение результата умножения
/= Присвоение результата от деления
//= Присвоение результата целочисленного деления
**= Присвоение степени числа
%= Присвоение остатка от деления

number *= 4 # 48
'''
# деление
print(7 / 2)  # 3.5
# деление целочисленное
print(7 // 2)  # 3
print(6 ** 2)  # Возводим число 6 в степень 2. Результат - 36
# Получение остатка от деления
print(7 % 2)  # Получение остатка от деления числа 7 на 2. Результат - 1

# Округление round
print(2.0001 + 0.1)  # 2.1001000000000003
round(2.0001 + 0.1)  # 2
round(2.0001 + 0.1, 4)  # 2.1001
# округление до целого числа
print(round(2.49))  # 2 - округление до ближайшего целого 2
print(round(2.51))  # 3
# ближайшее четное
print(round(2.5))   # 2 - ближайшее четное
print(round(3.5))   # 4 - ближайшее четное

print(round(2.655, 2))   # 2.65 - округление не до четного
print(round(2.665, 2))   # 2.67
print(round(2.675, 2))   # 2.67

# float ----------------------------------------------------------------------------------------------------
height = 1.68
x = 3.9e3 # экспоненциальная запись
x = float('1.5')
x = float(True)    # 1.0


number = 12345.6789
formatted = locale.format_string("%f", number)
print(formatted)    # 12345,678900
formatted = locale.format_string("%.2f", number)
print(formatted)    # 12345,68
formatted = locale.format_string("%d", number)
print(formatted)    # 12345
formatted = locale.format_string("%e", number)
print(formatted)    # 1,234568e+04
money = 234.678
formatted = locale.currency(money)
print(formatted)    # 234,68 €

# Для корректной работы с дробной частью
number = Decimal("0.1")
number = number + number + number
print(number)       # 0.3

# complex --------------------------------------------------------------------------------------------------
complexNumber = 1+2j # (1+2j)

# str ------------------------------------------------------------------------------------------------------
# строка - это неизменяемый (immutable) тип
'''
    isalpha(): возвращает True, если строка состоит только из алфавитных символов
    islower(): возвращает True, если строка состоит только из символов в нижнем регистре
    isupper(): возвращает True, если все символы строки в верхнем регистре
    isdigit(): возвращает True, если все символы строки - цифры
    isnumeric(): возвращает True, если строка представляет собой число
    startswith(str): возвращает True, если строка начинается с подстроки str
    endswith(str): возвращает True, если строка заканчивается на подстроку str
    lower(): переводит строку в нижний регистр
    upper(): переводит строку в вехний регистр
    title(): начальные символы всех слов в строке переводятся в верхний регистр
    capitalize(): переводит в верхний регистр первую букву только самого первого слова строки
    lstrip(): удаляет начальные пробелы из строки
    rstrip(): удаляет конечные пробелы из строки
    strip(): удаляет начальные и конечные пробелы из строки
    ljust(width): если длина строки меньше параметра width, то справа от строки добавляются пробелы, чтобы дополнить значение width, а сама строка выравнивается по левому краю
    rjust(width): если длина строки меньше параметра width, то слева от строки добавляются пробелы, чтобы дополнить значение width, а сама строка выравнивается по правому краю
    center(width): если длина строки меньше параметра width, то слева и справа от строки равномерно добавляются пробелы, чтобы дополнить значение width, а сама строка выравнивается по центру
    find(str[, start [, end]): возвращает индекс подстроки в строке. Если подстрока не найдена, возвращается число -1
    replace(old, new[, num]): заменяет в строке одну подстроку на другую
    split([delimeter[, num]]): разбивает строку на подстроки в зависимости от разделителя
    join(strs): объединяет строки в одну строку, вставляя между ними определенный разделитель
'''
message = str(1.555)
message = str(False) # message="False"
message = "Message:\n\"Hello World\""

print(type(message)) # <class 'str'>

text = '''Laudate omnes gentes laudate
Magnificat in secula
Et anima mea laudate
Magnificat in secula 
'''

path = r"C:\python\name.txt" # невелировать спецсимволы

# Вставка значений в строку
userName = "Tom"
userAge = 37
user = f"name: {userName}  age: {userAge}"
# именованные параметры форматирования
info = "Name: {name}\t Age: {age}".format(name="Bob", age=23)
print(info)     # Name: Bob  Age: 23
# позиционное форматирование
info = "Name: {0}\t Age: {1}".format("Bob", 23)
print(info)     # Name: Bob  Age: 23
number = .12345
print(f"{number:%}")        # 12.345000%

# форматирование Подстановки
'''
    s: для вставки строк
    d: для вставки целых чисел
    f: для вставки дробных чисел. Для этого типа также можно определить через точку количество знаков в дробной части.
    %: умножает значение на 100 и добавляет знак процента
    e: выводит число в экспоненциальной записи
'''
formatted_welcome = "Hello {:s}".format("Jeka")
target = "{:d} символов".format(int(5))
print("{:.2f}".format(23.8589578))   # 23.86
print("{:.4f}".format(23.8589578))   # 23.8590
print("{:,.2f}".format(10001.23554))    # 10,001.24
print("{:10.2f}".format(23.8589578))    #     23.86
print("{:8d}".format(25))               #      25
print("Имя: %s \t Возраст: %d" % ("Tom", 35))   # Имя: Tom     Возраст: 35

# доступ
string = "hello world"
c1 = string[-1]  # d

# concat
full_name = str('Petr')+str(' ')+str('Petrov')
print('fullname',full_name,sep=':')
# повтор
print("he" * 4)  # hehehehe

# Функции ord и len
print(ord("A"))     # 65
length = len("string")

# перебор
string = "hello world"
for char in string:
    print(char)

# поиск в строке
string = "hello world"
exist = "hello" in string
print(exist)    # True

# Получение подстроки
'''
    string[:end]: извлекается последовательность символов начиная с 0-го индекса по индекс end (не включая)
    string[start:end]: извлекается последовательность символов начиная с индекса start по индекс end (не включая)
    string[start:end:step]: извлекается последовательность символов начиная с индекса start по индекс end (не включая) через шаг step
'''
string = "hello world"
# с 0 до 5 индекса
sub_string1 = string[:5]
print(sub_string1)      # hello
# со 2 до 5 индекса
sub_string2 = string[2:5]
print(sub_string2)      # llo
# с 2 по 9 индекса через один символ
sub_string3 = string[2:9:2]
print(sub_string3)      # lowr


# replace
txt = "... ... was a race horse, two two was ... too."
x = txt.replace("...", "***",2)
print(x) # *** *** was a race horse, two two was ... too.

# Неявные преобразования  --------------------------------------------------------------------------------------------------
# 1 complex
# 2 float
# 3 int

# Функции --------------------------------------------------------------------------------------------------
def types_add(a, b):
    return a + b;
 
