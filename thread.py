import threading # работает в разных потоках
import time

t = time.time()
shared_data = list()
event = threading.Event()

def work_thread_one(n=3):
    print(threading.current_thread().name + ' Start!')
    count = n
    while count > 0:
        count-=1
        time.sleep(1)
        lock = threading.Lock()# берем блокировку
        lock.acquire()
        try:
            # Пример обмена флагом Event (event.wait() ждать True)
            print('Event state:',event.is_set(),threading.current_thread().name)
            if event.is_set():
                event.clear()
            else:
                event.set()   
            # Работа с общими данными     
            shared_data.append(threading.current_thread().name)
        finally:
            lock.release()
        
    

def work_thread_two(num=1):
    print(threading.current_thread().name + ' Start!')
    count = num
    while count > 0:
        time.sleep(1)
        count-=1
        lock = threading.Lock() 
        with lock:# аналог try finally
            # Пример обмена флагом Event
            print('Event state:',event.is_set(),threading.current_thread().name)
            if event.is_set():
                event.clear()
            else:
                event.set() 
            # Работа с общими данными     
            shared_data.append(threading.current_thread().name)
    

th1 = threading.Thread(target=work_thread_one,name="thread 1",args=(3,), daemon=False)
th2 = threading.Thread(target=work_thread_two,name="thread 2",kwargs={'num':2,}, daemon=False)

th1.start()
th2.start()

# ожидать завершения потоков не более 10 секунд
th1.join(10.0) # блокировка основного потока пока не звершится th1
th2.join(10.0)

t2 = time.time()   
print("Программа выполнилась за:",t-t2) 
print(shared_data) # ['thread 2', 'thread 1', 'thread 2', 'thread 1', 'thread 1']

# --------------------------------------------------------------------------------------------
# Выполнить задачу через 4 секунды

def myfunc():
    print('tick-tack')
timer = threading.Timer(4, myfunc)
timer.start()


# --------------------------------------------------------------------------------------------
# Передача данных с помощью очередей

# Обработать студентов в два потока
from queue import Queue
import datetime

students= [(99, "Андрей"),
           (76, "Александр"),
           (75, "Никита"),
           (72, "Евгений"),
          ]
def student(q):
    while True:
        # Получаем задание из очереди
        check = q.get()
        # Выводим время начала проверки
        print(check[1], 'сдал работу в', datetime.datetime.now()
            .strftime('%H:%M:%S')) 
        #Время затраченное на проверку, которое зависит от рейтинга
        time.sleep((100-check[0])/5)
        # Время окончания проверки
        print(check[1], 'забрал работу в', datetime.datetime.now()
            .strftime('%H:%M:%S'))
        # Даём сигнал о том, что задание очереди выполнено
        q.task_done()
# Создаем очередь
q = Queue()
# Загружаем в очередь студентов
for x in students:
    q.put(x)
#создаём и запускаем потоки
thread1 = threading.Thread(target=student, args=(q,), daemon=True)
thread2 = threading.Thread(target=student, args=(q,), daemon=True)
thread1.start()
time.sleep(10)
thread2.start()
# Блокируем выполнение до завершения всех заданий
q.join()
print("Этот текст напечатается после окончания блокировки")