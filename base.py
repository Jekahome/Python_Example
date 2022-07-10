# комментарий
'''
   1 Функции
   2 Логические операции and,or,not 
   3 Оператор in
   4 Цикл while, for
   5 Видимость глобальная и локальная 
   6 match


'''

'''
Список ключевых слов:

    False      await      else       import     pass
    None       break      except     in         raise
    True       class      finally    is         return
    and        continue   for        lambda     try
    as         def        from       nonlocal   while
    assert     del        global     not        with
    async      elif       if         or         yield

'''

def input_exam():
    # input
    name = input("Введите имя: ")

    # console output 
    print("Hello",name, sep=": ",end="\n")

    # ввод int
    age = int(input("Введите age: "))
    print(type(age))

# Функции -----------------------------------------------------------------------------------------------------------------------
def add(a, b):
    return a + b;

# Функции возвращают кортеж
def a1(*xx):
    x = "Вася"
    y = "Петя"
    z = 2
    k ="алкоголика"
    return x, y, z, k
a, b, c, d = a1()
print("А вы знаете, что", a, "и", b,c,d,"?!")

# Значения по умолчанию
def print_person(name, age = 18):
    print(f"Name: {name}  Age: {age}")
print_person("Bob")
# Передача значений параметрам по имени
print_person(age = 22, name = "Tom")

# Все параметры, которые располагаются справа от символа *, получают значения только по имени
def print_person(name, *,  age, company):
    print(f"Name: {name}  Age: {age}  Company: {company}")
print_person("Bob", age = 41, company ="Microsoft")    # Name: Bob  Age: 41  company: Microsoft

# Все параметры, которые идут до символа / , являются позиционными и могут получать значения только по позиции
def print_person(name, /, age, company="Microsoft"):
    print(f"Name: {name}  Age: {age}  Company: {company}")
print_person("Tom", company="JetBrains", age = 24)     # Name: Tom  Age: 24  company: JetBrains
print_person("Bob", 41)                 # Name: Bob  Age: 41  company: Microsoft

# все параметры именнованные
def print_person(*,  name, age, company):
    print(f"Name: {name}  Age: {age}  Company: {company}")
print_person(name="Bob", age = 41, company ="Microsoft")     
    
# Неопределенное количество параметров
def sum(*numbers):
    result = 0
    for n in numbers:
        result += n
    print(f"sum = {result}")
sum(1, 2, 3, 4, 5)      # sum = 15
sum(3, 4, 5, 6)         # sum = 18

# Функция как тип
def say_hello(): print("Hello")
message = say_hello
message()       # Hello

# Функция как параметр функции
def do_operation(a, b, operation):
    result = operation(a, b)
    print(f"result = {result}")
def sum(a, b): return a + b
def multiply(a, b): return a * b
do_operation(5, 4, sum)         # result = 9
do_operation(5, 4, multiply)   # result = 20

# Функция как результат функции
def sum(a, b): return a + b
def subtract(a, b): return a - b
def multiply(a, b): return a * b
 
def select_operation(choice):
    if choice == 1:
        return sum
    elif choice == 2:
        return subtract
    else:
        return multiply
 
operation = select_operation(1)     # operation = sum
print(operation(10, 6))             # 16
 
operation = select_operation(2)     # operation = subtract
print(operation(10, 6))             # 4

# Лямбда-выражения (они ограничены тем, что они могут выполнять только одну инструкцию)
message = lambda: print("hello") # аналогично def message(): print("hello")
message()   # hello

# Лямбда с параметрами
sum = lambda a, b: a + b # аналогично  def sum(n,m): return n * m
print(sum(4, 5))    # 9

def multiply(n): return lambda m: n * m
fn = multiply(5)
print(fn(5))        # 25
print(fn(6))        # 30


# Лямбда в качестве параметра
def do_operation(a, b, operation):
    result = operation(a, b)
    print(f"result = {result}")
do_operation(5, 4, lambda a, b: a + b)  # result = 9

# Лямбда в качестве возвращаемого значения
def select_operation(choice):
    if choice == 1:
        return lambda a, b: a + b
    elif choice == 2:
        return lambda a, b: a - b
    else:
        return lambda a, b: a * b
operation = select_operation(1)  # operation = sum
print(operation(10, 6))  # 16


# Логические операции and,or,not --------------------------------------------------------------------------------------------------
bool_result = 10 > 21 and 10 == 58
bool_result = 10 > 21 or 10 == 58
bool_result = not 10 > 21

# Оператор in ---------------------------------------------------------------------------------------------------------------------
# (True если в некотором наборе значений есть определенное значение)
message = "hello world!"
hello = "hello"
print(hello in message)  # True - подстрока hello есть в строке "hello world!"
print(hello not in message)  # False  
gold = "gold"
print(gold not in message)  # True

# Условная конструкция if
language = "german"
if language == "english":
    print("Hello")
    print("World")
elif language == "german":
    print("Hallo")
    print("Welt")
else:
    print("Привет")
    print("мир")


# Цикл while -----------------------------------------------------------------------------------------------------------------------
number = 1
while number < 5:
    print(f"number = {number}")
    number += 1
print("Работа программы завершена")    
# Блок else может быть полезен, если условие изначально равно False
number = 6
while number < 5:
    print(f"number = {number}")
    number += 1
else:
    number = 4
print("Работа программы завершена")

# Цикл for -------------------------------------------------------------------------------------------------------------------------
message = "Hello"
for c in message:
    print(c)
    if c == 'l':
        break
    else:
        continue

# Видимость глобальная и локальная -------------------------------------------------------------------------------------------------
# nonlocal идентификатор видимости от уровня выше
name = "Tom"
def say_hi():
    global  name
    name = "Bob"        # изменяем значение глобальной переменной
    print("Hello", name)    

# Замыкания
def outer():        # внешняя функция
    n = 5           # лексическое окружение - локальная переменная
    def inner():      # локальная функция
        nonlocal n
        n += 1        # операции с лексическим окружением
        print(n)
    return inner
 
fn = outer()   # fn = inner, так как функция outer возвращает функцию inner
# вызываем внутреннюю функцию inner
fn()    # 6
fn()    # 7
fn()    # 8    

# Конструкция match ---------------------------------------------------------------------------------------------------------------
def print_hello(language):
    match language:
        case "russian":
            print("Привет")
        case "english":
            print("Hello")
        case "german":
            print("Hallo")
        case _:
             print("default")
print_hello("english")      # Hello

# Ограничение if
def check_data(data):
    match data:
        case name, age if name == "admin" or age not in range(1, 101):
            print("Некорректные значения")
        case name, age:
            print(f"Данные проверены. Name: {name}  Age: {age}")
check_data(("admin", -45))      # Некорректные значения
check_data(("Tom", 37))         # Данные проверены. Name: Tom  Age: 37

# псевдоним as
def print_person(person):
    match person:
        case ("Tom" | "Tomas" as name, 37 | 38 as age):   # псевдонимы для отдельных значений
            print(f"Tom| Name: {name}  Age: {age}")
        case ("Bob" | "Robert", 41 | 42) as bob:          # псевдоним для всего шаблона
            print(f"Bob| Name: {bob[0]}  Age: {bob[1]}")
        case _:
            print("Undefined")
print_person(("Tomas", 38))     # Tom| Name: Tomas  Age: 38


# turple в качестве значений
def print_data(user):
    match user:
        case ("Tom" | "Tomas" | "Tommy", 37) | ("Sam", 22):
            print("default user")
        case ("Tom", age):
            print(f"Age: {age}")
        case (name, 22):
            print(f"Name: {name}")
        case (name, age):
            print(f"Name: {name}  Age: {age}")
        case (name, _):     # второй элемент не важен
            print(f"Name: {name}")
        case (_, _):
            print("Undefined user")    
print_data(("Tom", 37))     # default user

# Кортеж с неопределенным количеством элементов
def print_data(user):
    match user:
        case ("Tom", 37, *rest):
            print(f"Rest: {rest}")
        case (name, age, *rest):
            print(f"{name} ({age}): {rest}")
print_data(("Tom", 37))               # Rest: []
print_data(("Tom", 37, "Google"))     # Rest: ["Google"]

# Если нам этот параметр (rest) не важен, но мы по прежнему хотим, чтобы шаблон соответствовал кортежу с неопределенным количеством элементов, мы можем использовать подшаблон *_:
def print_data(user):
    match user:
        case ("Tom", 37, *_):
            print("Default user")
        case (name, age, *_):
            print(f"{name} ({age})")
print_data(("Tom", 37))               # Default user
print_data(("Tom", 37, "Google"))     # Default user
print_data(("Bob", 41, "Microsoft", "english"))     # Bob (41)


# Массивы неопределенной длины
def print_people(people):
    match people:
        case [first, *other]:
            print(f"First: {first}  Other: {other}")
print_people(["Tom"])                   # First: Tom  Other: []
print_people(["Tom", "Sam"])            # First: Tom  Other: ["Sam"]

# Массивы Альтернативные значения 
def print_people(people):
    match people:
        case ["Tom" | "Tomas" | "Tommy", "Sam", "Bob"] | ["Tomas", "Sam", "Bob"]:
            print("default people")
        case [first, second, third]:
            print(f"{first}, {second}, {third}")
print_people(["Tom", "Sam", "Bob"])         # default people

# Словари dictionary
def look(words):
    match words:
        case {"red": "красный" | "алый" | "червонный"} | {"blue": "синий"}:  # если значение "красный", "алый" или "червонный"
            print("Слово red есть в словаре")
        case {"red": red, "blue": blue}:
            print(f"red: {red}  blue: {blue}")            
        case {"red": _, "blue": _}:
            print("Слова red и blue есть в словаре")  
        case {"red": red, **rest}: # Получение всех значений
            print(f"red: {red}")
            for key in rest:        # rest - тоже словарь
                print(f"{key}: {rest[key]}")                      
        case {}:
            print("Слово red в словаре отсутствует или имеет некорректное значение")
look({"red": "красный", "green": "зеленый"})        # Слово red есть в словаре
look({"red": "алый", "green": "зеленый"})           # Слово red есть в словаре
look({"green": "зеленый"})    # Слово red в словаре отсутствует или имеет некорректное значение




