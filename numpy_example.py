#!/usr/bin/python
# -*- coding: utf-8 -*-
import numpy as np
# https://numpy.org/doc/stable/reference/generated/numpy.set_printoptions.html
# https://machinelearningmastery.ru/the-ultimate-beginners-guide-to-numpy-f5a2f99aef54/

'''
[ [[0 ,0 ,0],[0 ,0 ,0]], [[0 ,0 ,0],[0 ,0 ,0]] ]

'''

'''
Create narray

np.array - массив
np.zeros - матрица из нулей
np.ones -  матрица из единиц
np.eye  -  единичная матрица (двумерный массив)
np.empty - матрица 3 из случайных чисел
np.arange - массив диапазон
np.linspace - массив фиксированный диапазон  
np.fromfunction - массив из ф-ции заполнителя
'''
def create_narray():
    
    # img = np.zeros((2,2,3),np.uint8)
    # print(type(img),type(img[0]),type(img[0][0])) # numpy.ndarray

    a = np.array([[1, 2, 3], [4, 5, 6]], dtype=np.int8)
    print(f"ndarray.ndim={a.ndim}==2") # число измерений (чаще их называют "оси") массива.
    print(f"ndarray.shape={a.shape}==(2, 3)") # размеры массива, его форма. Кортеж показывающий длину массива по каждой оси
    print(f"ndarray.size={a.size}==6") # количество элементов массива. Равно произведению всех элементов атрибута shape.
    print(f"ndarray.dtype={a.dtype}==int8") # тип элементов массива (bool_, character, uint8, int8, int16, int32, int64, float8, float16, float32, float64, complex64, object_, ...)
    print(f"ndarray.itemsize={a.itemsize}==1") # размер каждого элемента массива в байтах.
    print(f"ndarray.data={a.data}") # буфер, содержащий фактические элементы массива. 

    # матрица m*n
    # m = количество массивов
    # n = количество елементов в массиве

    _ = np.zeros((2, 3), dtype=np.uint8) # двумерный массив [[0 0 0] [0 0 0]]
    _ = np.zeros((2, 3, 3), dtype=np.int8) # две матрици 3x3 [ [[0 0 0][0 0 0][0 0 0]] [[0 0 0][0 0 0][0 0 0]] ]
    _ = np.ones((2, 2, 3), dtype=np.int8) # матрица 2 на 2 из 3 единиц [ [[1 1 1],[1 1 1]], [[1 1 1],[1 1 1]] ]
    _ = np.eye(5, dtype=np.int8) # единичная матрица (двумерный массив) 5 на 5
    _ = np.empty((3, 3), dtype=np.int8) # матрица 3 на 3 из случайных чисел  [[ 32  12  61] [101  90 127] [  0   0  32]]
    _ = np.arange(10, 30, 5, dtype=np.int8) # массив диапазон от 10 до 30 не включая с шагом 5  [10, 15, 20, 25]
    _ = np.linspace(0, 2, 9, dtype=np.float16)  # массив диапазон с фиксированным количеством 9 чисел от 0 до 2 включительно [0.   0.25 0.5  0.75 1.   1.25 1.5  1.75 2.  ]

    # fromfunction(): применяет функцию ко всем комбинациям индексов
    def f1(m_arr, n_arr_item):
        return  m_arr+n_arr_item 
    a = np.fromfunction(f1, (3, 4), dtype=np.int8) #  матрица 3 на 4 из значений ф-ции
    print(a)

'''
Базовые операции
сложение вычетания деление минимум максимум ...

np.append() - вставка в конец
np.delete() - удаление по индексу
np.sort() - сортировка
    
img.copy() - копия

img.sum
img.min
img.max

Разбиение массива:
np.hstack
np.row_stack
np.column_stack
np.column_stack

Объединение массивов:
np.hstack
np.row_stack
np.column_stack
np.column_stack

'''
def base_perations_narray():
    
    '''
    ndarray.ndim() - количество осей или размеров массива
    ndarray.size() - общее количество элементов массива
    ndarray.shape() - количество элементов, хранящихся вдоль каждого измерения массива
    '''
    a = np.array([20, 30, 40, 50])
    _ = a.ndim # 1
   
    
    # размеры массивов при этом должны быть равны
    a = np.array([20, 30, 40, 50])
    b = np.arange(4) # [0,  1, 2, 3]
    res = a + b      # [20 31 42 53]
    res = res - b    # [20,30,40 50]
    res = res * np.array([2, 2, 2, 2]) # [40,60,80,100]
    res = res / np.array([2, 2, 2, 2]) # [20. 30. 40. 50.]  type(res[0]) == numpy.float64
    
    '''
    np.append()
    np.delete()
    np.sort()    
    
    Еще сортировки:
    argsort - непрямая сортировка по указанной оси
    lexsort - непрямая стабильная сортировка по нескольким ключам
    searchsorted - будет найти элементы в отсортированном массиве
    '''
    a = np.array([20, 30, 40, 50])
    a = np.append(a, [1,2]) # [20 30 40 50 1 2]
    a = np.delete(a,0) # [30 40 50 1 2]
    a = np.sort(a) # [1 2 30 40 50]
    
    # Поверностная копия -----------------------------------------------------------
    a = np.ones((2, 2, 3), dtype=np.uint8)
    b = a.copy()
    # ndarray.view() метод не создает копию он только позволяет создать другую формы тех же данных
    
    # Глубокая копия -----------------------------------------------------------
    # https://pythonworld.ru/moduli/modul-copy.html
    import copy
    a = np.ones((2, 2, 3), dtype=np.uint8)
    b = copy.deepcopy(a)
 
    # массив и число -----------------------------------------------------------
    '''
        sum
        min
        max
    '''
    a = np.array([20, 30, 40, 50])
    a = a + 5 # [25  35  45  55]
    a = a - 5 # [20 30 40 50]
    a = a * 2 # [40 60 80 100]
    a = a / 2 # [20. 30. 40. 50.] type(res[0]) == numpy.float64
    a = np.array([2, 3, 4, 5]) ** 2 # [4 9 16 25] [2^2,3^2,4^2,5^2] возведение в степень
    a = a > 10 # [False False  True  True] Фильтрация
     
    _ = np.array([2, 3, 4, 5]).sum() # Сумма елементов = 14
    _ = np.array([20, 3, 14, 5]).min() # Минимальный елемент = 3
    _ = np.array([20, 3, 14, 5]).max() # Максимальный елемент = 20
    
    '''
        np.hsplit
        np.vsplit
    '''
    # Разбиение массива --------------------------------------------------------
    img = np.array( [
        [np.array([1,  2,  3]),  
        np.array([4,  5,  6]), 
        np.array([7,  8,  9])],
        
        [np.array([11, 12, 13]), 
        np.array([14, 15, 16]),
        np.array([17, 18, 19])],
    ])   
    res = np.hsplit(img, (1,2))   
    '''
    [array([[[ 1,  2,  3]], [[11, 12, 13]]]), 
    array([[[ 4,  5,  6]],  [[14, 15, 16]]]), 
    array([[[ 7,  8,  9]],  [[17, 18, 19]]])]
    '''
    res = np.vsplit(img, (1,2)) 
    '''
    [array([[[1, 2, 3], [4, 5, 6], [7, 8, 9]]]), 
    array([[[11, 12, 13], [14, 15, 16], [17, 18, 19]]]), 
    array([], shape=(0, 3, 3), dtype=int64)]

    '''
    # Объединение массивов ------------------------------------------------------
    '''
        np.hstack
        np.row_stack
        np.column_stack
        np.column_stack
    '''
    img1 = np.array( [
        [np.array([1,  2,  3]),  
         np.array([4,  5,  6]), 
         np.array([7,  8,  9])],
        
        [np.array([11, 12, 13]), 
         np.array([14, 15, 16]),
         np.array([17, 18, 19])],
    ], dtype=np.uint8)
    img2 = np.ones(img1.shape, dtype=np.uint8)
    #res = np.vstack((img1, img2)) # добавит в конец img2 матрици
    res = np.hstack((img1, img2)) # изменит размерность матрици 3x6
    print(res)
    
    # обьединение row
    a = np.array([1, 2, 3], dtype=np.uint8)
    b = np.array([4, 5, 6], dtype=np.uint8)
    c = np.array([7, 8, 9], dtype=np.uint8)
    res = np.row_stack((a, b, c))
    '''
    [[1 2 3]
    [4 5 6]
    [7 8 9]]
    '''
    # обьединение cow 
    res = np.column_stack((a, b, c))
    '''
    [[1 4 7]
    [2 5 8]
    [3 6 9]]
    '''


    # Для изображений ------------------------------------------------------------
    _ = np.zeros((2, 3, 4),dtype=np.uint8) # две матрици 3x4 [ [[0 0 0 0][0 0 0 0][0 0 0 0]] [[0 0 0 0][0 0 0 0][0 0 0 0]] ]
    m = 2
    n = 3
    _ = np.zeros((m, n, 3),dtype=np.uint8) #  две матрици 3x3 [ [[0 0 0][0 0 0][0 0 0]] [[0 0 0][0 0 0][0 0 0]] ]
    img = np.array( [
        [np.array([1,  2,  3]),  
         np.array([4,  0,  6]), 
         np.array([7,  8,  9])],
        
        [np.array([11, 12, 13]), 
         np.array([14, 5, 16]),
         np.array([17, 18, 19])],
        
        [np.array([1, 0, 1]), 
         np.array([14, 5, 16]),
         np.array([17, 18, 19])]
    ])
    # Фильтрация по ряду
    _ = img.min(axis=0) # соберет матрицу 3x3 из всех матриц по каждому уровню row целиком из матрици
    '''
    [[1 0 1]
     [4 0 6]
     [7 8 9]]
    '''
    _ = img.min(axis=1)  # соберет матрицу 3x3 из всех матриц по каждому уровню cow (по одному значению в каждом cow)
    '''
    [[ 1  0  3]
     [11  5 13]
     [ 1  0  1]]
    '''
    _ = img.min(axis=2) # соберет матрицу 3x3 из всех матриц по каждому уровню row (по одному значению в каждом row)
    '''
    [[ 1  0  7]
     [11  5 17]
     [ 0  5 17]]
    '''
    _ = img.max(axis=0)
    _ = img.max(axis=1)
    _ = img.max(axis=1)
    _ = img.sum(axis=0) # Сложить матрици
    #np.set_printoptions(precision=2,threshold=100,edgeitems=3,linewidth=75) # настройка форматирования массивов
    #print( img)
    


def create_slice():
    # https://pythonworld.ru/numpy/2.html
    
    # Получение срезов из матриц (многомерных массивов)
    img = np.array( [
        [np.array([1,  2,  3]),  
         np.array([4,  0,  6]), 
         np.array([7,  8,  9])],
        
        [np.array([11, 12, 13]), 
         np.array([14, 5, 16]),
         np.array([17, 18, 19])],
        
        [np.array([1,  0, 1]), 
         np.array([14, 5, 16]),
         np.array([17, 21, 19])]
    ])
    # Размерность матрици
    print(img.shape) # (m=3, n=3, count_elem=3) Для изменения формы img.reshape((3, 4)), Транспонирование img.transpose()   
    print('\nИсходный:\n',img[:],'\n')
    
    # доступ к елементу
    _ = img[1][2][1] # 18
    _ = img[1,2,1]   # 18
    _ = img[(1,2,1)] # 18
    
    # slice
    # три индекса 1-й это матрица, 2-й это row ряд, 3-й это индекс 0,1,2 элемента в row 
    # : - это диапазон [:, 2:, 1] => [_:_,2:_,1] ,а 1 тут индекс
    # 1:2 - это диапазон от индекса 1 до 2 не включая
    # 1:, - это диапазон от индекса 1 до конца/начала
    _ = img[:, 2,  0] # взять во всех матрицах по номеру ряда 2 первое знаяение [7,17,17]
    _ = img[:, 1:, 0] # взять во всех матрицах начиная с ряда по индексу 1 все первые знаяения этих рядов [[4,7],[14,17],[14,17]]
     
    _ = img[:, 1:, 1:] # взять во всех матрицах начиная с ряда по индексу 1 все знаяения ряда с индекса 1 [[[0,6],[8,9]], [[5,16],[18,19]], [[5,16],[21,19]]]
    
    _ = img[... , 2] # взять во всех матрица и рядах последние знаяения [[3,6,9],[13,16,19],[1,16,19]]
    _ = img[0, 2, ...] # взять в первой матрице ряд по индексу 2 все знаяения [7 8 9]
   
    # Перебор многомерного narray линейно или преобразовать в плоский массив img.ravel()   
    for el in img.flat:pass
      
    # Присвоение пикселю значения на основе выражения  
    img_dest = np.array([[100, 102, 130], [104, 150, 160],[170,180,190]], dtype=np.uint8)
    img = np.array([[1, 2, 3], [4, 5, 6],[7,8,9]], dtype=np.uint8)
    # построить индексы на основе выражения
    indexes = img_dest > 19 * 7
    # всем индексам(пикселям) присвоить значение 255
    img[indexes] = 255

  
    # Манипуляции с формой ---------------------------------------------------------
    '''
        img.shape
        img.ravel
        img.transpose
        img.reshape
    '''
    img = np.array( [
        [np.array([1,  2,  3]),  
         np.array([4,  5,  6]), 
         np.array([7,  8,  9])],
        
        [np.array([11, 12, 13]), 
         np.array([14, 15, 16]),
         np.array([17, 18, 19])],
    ])  
    _ = img.shape # Размерность матрици (m=2, n=3, count_elem=3) 
    _ = img.ravel() # Делает массив плоским
    _ = img.transpose() # Транспонирование
    '''
      [[[ 1 11]
        [ 4 14]
        [ 7 17]]

        [[ 2 12]
        [ 5 15]
        [ 8 18]]

        [[ 3 13]
        [ 6 16]
        [ 9 19]]]

    '''
    # Изменение формы
    img = img.reshape((3, 3, 2)) # (3, 3, -1) -1 - это расчитать автоматически
    '''
     [[[ 1  2]
        [ 3  4]
        [ 5  6]]

        [[ 7  8]
        [ 9 11]
        [12 13]]

        [[14 15]
        [16 17]
        [18 19]]]
    '''
    
'''
np.random.sample
np.random.randint
np.random.uniform
np.random.shuffle
'''    
def random_example():
    # https://pythonworld.ru/numpy/3.html
    a = np.random.sample((3,3))# Создать матрицу 3x3 рандомные числа numpy.float64
    a = np.random.randint(0, 255, (3,3)) # numpy.int64
    '''
    [[121 136  47]
    [ 79  66 228]
    [ 44  11 127]]
    '''
    a = np.random.uniform(0, 1, (3,3),) # равномерное распределение  numpy.float64
    np.random.shuffle(a) # перемешивание
    print(a)
        
# ---------------------------------------------------------------------------------        
 base_perations_narray()
# create_slice()
# random_example()



 
