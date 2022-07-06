# кортеж является неизменяемым (immutable) типом

# создание
tom = ("Tom", 23)
tom = "Tom", 23 
tom = ("Tom",) # из одного елемента
tom = tuple(["Tom", 37, "Google"]) # из списка

print(tom[1])
lenght = len(tom) # размер кортежа

# деструкция
tom = ("Tom", 23)
name,age = tom
name = tom[0]
age = tom[1]

# срез
tom = ("Tom", 37, "Google", "software developer")
tom =tom[1:3] # получем подкортеж с 1 по 3 элемента (не включая)

# кортеж как параметр(с помощью *) и возвращаемое значение функции
def get_user(name,age):
    return 'Hello '+name, age+1
tom = ("Tom", 22)
user = get_user(*tom)
print(user)


# Перебор кортежей
tom = ("Tom", 22, "Google")
for item in tom:
    print(item)

i = 0
while i < len(tom):
    print(tom[i])
    i += 1

# Проверка наличия значения
user = ("Tom", 22, "Google")
name = "Tom"
if name in user:
    print("Пользователя зовут Tom")
else:
    print("Пользователь имеет другое имя")



# Диапазоны -----------------------------------------------------------------------------
# Диапазоны или range представляют неизменяемый последовательный набор чисел.
'''
    range(stop): возвращает все целые числа от 0 до stop
    range(start, stop): возвращает все целые числа в промежутке от start (включая) до stop (не включая).
    range(start, stop, step): возвращает целые числа в промежутке от start (включая) до stop (не включая), которые увеличиваются на значение step
'''

range(5)            # 0, 1, 2, 3, 4
range(1, 5)         # 1, 2, 3, 4
range(2, 10, 2)     # 2, 4, 6, 8
range(10, 2, -2)    # 10 8 6 4 


for i in range(5):
    print(i, end=" ") # 0, 1, 2, 3, 4

# массив из диапазона
numbers = list(range(10))
print(numbers)      # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
numbers = list(range(2, 10))
print(numbers)      # [2, 3, 4, 5, 6, 7, 8, 9]
numbers = list(range(10, 2, -2))
print(numbers)      # [10, 8, 6, 4]




