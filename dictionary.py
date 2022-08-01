# Словарь (dictionary) в языке Python хранит коллекцию элементов, где каждый элемент имеет уникальный ключ и ассоциированое с ним некоторое значение.
'''
dict
pop
copy
items
keys
values
'''
from operator import itemgetter


objects = dict()
objects = {}
objects = {1: "Tom", 2: "Bob", 3: "Bill"}
objects = {"tom@gmail.com": "Tom", "bob@gmai.com": "Bob", "sam@gmail.com": "Sam"}
objects = {1: "Tom", "2": True, 3: 100.6}

# Присвоение по ключу
objects["2"] = not objects["2"]
objects[3] = objects[3] // 2
objects["new key"] = True
print('Set dic',objects[3],objects["2"],objects["new key"]) # 50.0 False True


objects = {'age':9,'name':'Vano'}
age,name = itemgetter('age', 'name')(objects)
print('Destruction:',age,name)
 
# создание из списка
users_list = [
    ["+111123455", "Tom"],
    ["+384767557", "Bob"],
    ["+958758767", "Alice"]
]
users_dict = dict(users_list)


# доступ к значению
objects = {"key1": "Tom", "key2": "Bob", "key3": "Bill"}
objects["key1"] = "New Tom"
value = objects["key1"]
value = objects.get("key1", "Unknown user")
value = objects.get("key1")

def show_value(key):
    if key in objects:
        user = objects[key]
        print(user)
    else:
        print("Key not found")

def get_value(key):
    try:
       return objects[key]
    except KeyError:
        print("Key not found")
        
show_value("_")
print(get_value("_"))    

# Удаление
key = "key1"
if key in objects:
    del objects[key]
    print(f"Элемент с ключом {key} удален")
else:
    print("Элемент не найден")
# или так
if "key1" in objects:
    user = objects.pop("key1")
if "key1" in objects:
    user = objects.pop("key1", "Unknown user")


# копирование словаря
users = {"+1111111": "Tom", "+3333333": "Bob", "+5555555": "Alice"}
students = users.copy()

# Метод update() объединяет два словаря:
users = {"+1111111": "Tom", "+3333333": "Bob"}
users2 = {"+2222222": "Sam", "+3333333": "Kate"}
users.update(users2) # {'+1111111': 'Tom', '+3333333': 'Kate', '+2222222': 'Sam'}
 
# Перебор словаря
users = {
    "+11111111": "Tom",
    "+33333333": "Bob",
    "+55555555": "Alice"
}
for key in users:
    print(f"Phone: {key}  User: {users[key]} ") 

for key, value in users.items():
    print(f"Phone: {key}  User: {value} ")    

# Перебор ключей
for key in users.keys():
    print(key)    
# Перебор значений
for value in users.values():
    print(value)    

# Комплексные словари
users = {
    "Tom": {
        "phone": "+971478745",
        "email": "tom12@gmail.com"
    },
    "Bob": {
        "phone": "+876390444",
        "email": "bob@gmail.com",
        "skype": "bob123"
    }
}
old_email = users["Tom"]["email"]
users["Tom"]["email"] = "supertom@gmail.com"
key = "skype"
if key in users["Tom"]:
    print(users["Tom"]["skype"])
else:
    print("skype is not found")    
