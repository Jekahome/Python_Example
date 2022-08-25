#!/usr/bin/python
# -*- coding: utf-8 -*-
import multiprocessing as mp  # https://docs.python.org/3/library/multiprocessing.html
import os

'''
# Пример с Pool
def f(x):
    return x*x

with mp.Pool(5) as p:
    print(p.map(f, [1, 2, 3]))
'''

'''
def f(name):
    print('hello', name)
    print('module name:', __name__)
    print('parent process:', os.getppid())
    print('process id:', os.getpid())


# Порождение процесса
p = mp.Process(target=f, args=('bob',))
p.start()
p.join()
'''

import time
 

t = time.time()
shared_data = mp.Queue()
lock = mp.Lock() 

def work_thread_one(l,q,n=3):
    print('Start process id:', os.getpid(),n)
    count = n
    while count > 0:
        count-=1
        time.sleep(1)
        l.acquire() # берем блокировку
        try:
            # Работа с общими данными   
            q.put(os.getpid())    
        finally:
            l.release()

        
def work_thread_two(l,q,num=1):
    print('Start process id:', os.getpid(),num)
    count = num
    while count > 0:
        count-=1
        time.sleep(1)
        l.acquire() # берем блокировку
        try:
            # Работа с общими данными     
            q.put(os.getpid())    
        finally:
            l.release()
    
p1 = mp.Process(target=work_thread_one,name="process 1", args=(lock,shared_data,3), daemon=False)
p2 = mp.Process(target=work_thread_two,name="process 2", kwargs={'l':lock,'q':shared_data,'num':2}, daemon=False)

p1.start()
p2.start()
# ожидать завершения потоков не более 10 секунд
p1.join(10.0)
p2.join(10.0)

size = shared_data.qsize()
while size > 0:
    size-=1
    print(shared_data.get())    

