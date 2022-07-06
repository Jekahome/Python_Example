# Множество (set) представляют вид набора, который хранит только уникальные элементы.
'''
add
len
set
remove
discard
clear
copy
union
intersection
difference
symmetric_difference
issubset
frozenset

'''
users = set()
users.add("Sam")

users = {"Tom", "Bob", "Alice", "Tom"}
print(users)    # {"Alice", "Bob", "Tom"}

users = set(["Mike", "Bill", "Ted"])
count = len(users)

# Проверка и удаление
user = "Tom"
if user in users: 
    users.remove(user)
# или так
users.discard("Tim")   
# удаление всех елементов
users.clear()

# перебор
for user in users:
    print(user)

# копирование
users = {"Tom", "Bob", "Alice"}
students = users.copy()    

# union() объединяет два множества 
users = {"Tom", "Bob", "Alice"}
users2 = {"Sam", "Kate", "Bob"}
users3 = users.union(users2)

# Пересечение множеств  элементы, которые есть одновременно в обоих множествах
users = {"Tom", "Bob", "Alice"}
users2 = {"Sam", "Kate", "Bob"}
users3 = users.intersection(users2)
# или так
users3 = users & users2

# разность множеств возвращает те элементы, которые есть в первом множестве, но отсутствуют во втором
users = {"Tom", "Bob", "Alice"}
users2 = {"Sam", "Kate", "Bob"}
users3 = users.difference(users2)
print(users3)           # {"Tom", "Alice"}
print(users - users2)   # {"Tom", "Alice"}

# Она возвращает все элементы обоих множеств за исключением общих:
users = {"Tom", "Bob", "Alice"}
users2 = {"Sam", "Kate", "Bob"}
users3 = users.symmetric_difference(users2)
print(users3)   # {"Tom", "Alice", "Sam", "Kate"}


# Отношения между множествами
# Метод issubset позволяет выяснить, является ли текущее множество подмножеством (то есть частью) другого множества:
users = {"Tom", "Bob", "Alice"}
superusers = {"Sam", "Tom", "Bob", "Alice", "Greg"}
print(users.issubset(superusers))   # True
print(superusers.issubset(users))   # False


# frozen set является видом множеств, которое не может быть изменено. 
# В такое множество мы не можем добавить новые элементы, как и удалить из него уже имеющиеся.
users = frozenset({"Tom", "Bob", "Alice"})







