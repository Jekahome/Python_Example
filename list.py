
# Список (массив)
numbers = [] # len(numbers) == 0
numbers = list()  # len(numbers) == 0
numbers.append(1)
numbers[0]+=1  # 2
 
numbers = [1, 2, 3, 4, 5]
people = ["Tom", "Sam", "Bob"]
objects = [1, 2.6, "Hello", True]
letters = list("Hello")  # ['H', 'e', 'l', 'l', 'o']
numbers = [5] * 6   # [5, 5, 5, 5, 5, 5]
numbers[0]=1  
print(numbers[-1]) # последний елемент

# деструкция
people = ["Tom", "Sam", "Bob"]
name1,name2,name3 = people
print(f"{name1} {name2} {name3}")

# Перебор элементов
people = ["Tom", "Sam", "Bob"]
for person in people:
    print(person)

people = ["Tom", "Sam", "Bob"]
i = 0
while i < len(people):
    print(people[i])    # применяем индекс для получения элемента
    i += 1


# Методы
'''
    append(item): добавляет элемент item в конец списка
    insert(index, item): добавляет элемент item в список по индексу index
    extend(items): добавляет набор элементов items в конец списка
    remove(item): удаляет элемент item. Удаляется только первое вхождение элемента. Если элемент не найден, генерирует исключение ValueError
    clear(): удаление всех элементов из списка
    index(item): возвращает индекс элемента item. Если элемент не найден, генерирует исключение ValueError
    pop([index]): удаляет и возвращает элемент по индексу index. Если индекс не передан, то просто удаляет последний элемент.
    count(item): возвращает количество вхождений элемента item в список
    sort([key]): сортирует элементы. По умолчанию сортирует по возрастанию. Но с помощью параметра key мы можем передать функцию сортировки.
    reverse(): расставляет все элементы в списке в обратном порядке
    copy(): копирует список

    len(list): возвращает длину списка
    sorted(list, [key]): возвращает отсортированный список
    min(list): возвращает наименьший элемент списка
    max(list): возвращает наибольший элемент списка
'''    

# Добавление и удаление элементов
people = ["Tom", "Bob"]
# добавляем в конец списка
people.append("Alice")  # ["Tom", "Bob", "Alice"]
# добавляем на вторую позицию
people.insert(1, "Bill")  # ["Tom", "Bill", "Bob", "Alice"]
# добавляем набор элементов ["Mike", "Sam"]
people.extend(["Mike", "Sam"])      # ["Tom", "Bill", "Bob", "Alice", "Mike", "Sam"]
# получаем индекс элемента
index_of_tom = people.index("Tom")
# удаляем по этому индексу
removed_item = people.pop(index_of_tom)     # ["Bill", "Bob", "Alice", "Mike", "Sam"]
# удаляем последний элемент
last_item = people.pop()     # ["Bill", "Bob", "Alice", "Mike"]
# удаляем элемент "Alice"
people.remove("Alice")      # ["Bill", "Bob", "Mike"]
print(people)       # ["Bill", "Bob", "Mike"]
# удаляем все элементы
people.clear()


# Проверка наличия элемента
people = ["Tom", "Bob", "Alice", "Sam"]
if "Alice" in people:
    people.remove("Alice")
print(people)       # ["Tom", "Bob", "Sam"]


# Удаление с помощью del
'''
del variable удаление переменной
del obj.attr удаление атрибута
del data[k] удаление элемента по индексу
del data[i:j] удаление элементов по срезу
'''
people = ["Tom", "Bob", "Alice", "Sam", "Bill", "Kate", "Mike"]
del people[1]   # удаляем второй элемент
print(people)   # ["Tom", "Alice", "Sam", "Bill", "Kate", "Mike"]
del people[:3]   # удаляем  по четвертый элемент не включая
print(people)   # ["Bill", "Kate", "Mike"]
del people[1:]   # удаляем  со второго элемента
print(people)   # ["Bill"]

 

# Подсчет вхождений
people = ["Tom", "Bob", "Alice", "Tom", "Bill", "Tom"]
people_count = people.count("Tom")
print(people_count)      # 3

# Сортировка
people = ["Tom", "Bob", "Alice", "Sam", "Bill"]
people.sort() # people.reverse()
people.sort(key=str.lower)  # сортировка без учета регистра
people = sorted(people, key=str.lower) # еще один способ сортировки
print(people)      # ["Alice", "Bill", "Bob", "Sam", "Tom"]

# Минимальное и максимальное значения
numbers = [9, 21, 12, 1, 3, 15, 18]
print(min(numbers))     # 1
print(max(numbers))     # 21

# Копирование списков
people = ["Tom", "Bob", "Alice", "Sam", "Tim", "Bill"]
people2 = people.copy()    # копируем элементы из people в people2
slice_people1 = people[:3]   # копируем с 0 по 3
slice_people2 = people[1:3]   # копируем с 1 по 3
slice_people3 = people[1:6:2]   # с 1 по 6 с шагом 2

# Соединение списков
people1 = ["Tom", "Bob", "Alice"]
people2 = ["Tom", "Sam", "Tim", "Bill"]
people3 = people1 + people2

# Списки списков
people = [
    ["Tom", 29],
    ["Alice", 33],
    ["Bob", 27]
]
person = list()
person.append("Bill")
person.append(41)
people.append(person) # добавление вложенного списка
print(people[0])         # ["Tom", 29]
print(people[0][0])      # Tom
for person in people:
    for item in person:
        print(item, end=" | ")


