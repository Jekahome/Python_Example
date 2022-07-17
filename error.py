'''
В Python есть следующие базовые типы исключений:

    BaseException: базовый тип для всех встроенных исключений
    Exception: базовый тип, который обычно применяется для создания своих типов исключений
    ArithmeticError: базовый тип для исключений, связанных с арифметическими операциями (OverflowError, ZeroDivisionError, FloatingPointError).
    BufferError: тип исключения, которое возникает при невозможности выполнить операцию с буффером
    LookupError: базовый тип для исключений, которое возникают при обращении в коллекциях по некорректному ключу или индексу (например, IndexError, KeyError)


От этих классов наследуются конкретные типы исключений: 
    IndexError: исключение возникает, если индекс при обращении к элементу коллекции находится вне допустимого диапазона
    KeyError: возникает, если в словаре отсутствует ключ, по которому происходит обращение к элементу словаря.
    OverflowError: возникает, если результат арифметической операции не может быть представлен текущим числовым типом (обычно типом float).
    RecursionError: возникает, если превышена допустимая глубина рекурсии.
    TypeError: возникает, если операция или функция применяется к значению недопустимого типа.
    ValueError: возникает, если операция или функция получают объект корректного типа с некорректным значением.
    ZeroDivisionError: возникает при делении на ноль.
    NotImplementedError: тип исключения для указания, что какие-то методы класса не реализованы
    ModuleNotFoundError: возникает при при невозможности найти модуль при его импорте директивой import
    OSError: тип исключений, которые генерируются при возникновении ошибок системы (например, невозможно найти файл, память диска заполнена и т.д.)
   
    и.т.д ...

'''
import sys, os

try:
    raise NotImplementedError("No error")
except Exception as e:
    exc_type, exc_obj, exc_tb = sys.exc_info()
    fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
    print(exc_type, fname, exc_tb.tb_lineno) # <class 'NotImplementedError'> error.py 29


try:
    number = int("tyy")
    if number == 0:
        raise Exception("Число не должно быть равно 0")
except ZeroDivisionError:
   print('Ошибка: произошло деление на 0')
except (ZeroDivisionError, ValueError):    #  обработка двух типов исключений - ZeroDivisionError и ValueError
    print("Попытка деления числа на ноль или некорректный ввод")   
except BaseException:
    print("Общее исключение")       
except:
    print("Преобразование прошло неудачно")
finally:
    print("можно освободить ресурсы")    
print("Завершение программы")

try:
   n = 1/0
except ZeroDivisionError as e:
   print('Ошибка: произошло деление на 0:',e) # division by zero
else:
   print("Завершение программы")


# Свой класс исключений ---------------------------------------------------------------------------------------
class PersonAgeException(Exception):
    def __init__(self, age, minage, maxage):
        self.age = age
        self.minage = minage
        self.maxage = maxage
 
    def __str__(self):
        return f"Недопустимое значение: {self.age}. " \
               f"Возраст должен быть в диапазоне от {self.minage} до {self.maxage}"

try:
    raise PersonAgeException(-23, 1, 110)
except PersonAgeException as e:
    print(e)    # Недопустимое значение: -23. Возраст должен быть в диапазоне от 1 до 110       
