class Person:  
     static_attr = 'static attr'
     private_static_attr = 'private attr'
     def __init__(self, name): # constructor
       self.name = name    # public
       self.__age = 1      # private   

     @staticmethod
     def print_atatic_attr():
        print(Person.private_static_attr)    
     def say_hello(self):
        print("Hello",self.name,self.__age) #  print(f"Hello {self.name}")
     def say_msg(self,msg='hi'):
        print(msg) 
     def hello(self):
        self.say_hello()
     # getter для private свойств   
     @property
     def age(self):
         return self.__age
     # setter для private свойств   
     @age.setter
     def age(self, age):
         if 1 < age < 110:
             self.__age = age
         else:
             print("Недопустимый возраст")
     def __str__(self):
      return f"Name: {self.name}  Age: {self.__age}"        
 
Person.static_attr_bla = 'new value' 
Person.print_atatic_attr() # private attr
print(Person.static_attr_bla) # new value 
 
tom = Person('Tom')
tom.age = 8
tom.say_hello()    # Hello Tom 8
tom.say_msg('TOM')  # TOM
tom.name = 'JEKA'
tom.hello()  # Hello TOM 8
print(tom) # Name: JEKA  Age: 8 (__str__)

# Наследование
class Employee(Person):
    # можно и без конструктора передать параметры в базовый класс
    def __init__(self, name):
        super().__init__(name)
    def work(self):
        print(f"{self.name} works")
    def hello(self):
        super().hello() 
        print(')))')

employee = Employee('Jeka')
employee.hello() # Hello Jeka 1 )))