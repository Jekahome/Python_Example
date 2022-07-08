import datetime
from datetime import date
from datetime import time
from datetime import datetime as data_time
from datetime import timedelta

# Дата и время сейчас
now = data_time.now()
print(now) # 2022-07-08 12:19:29.866407
print(now.strftime("%d/%m/%y %I:%M")) # 08/07/22 12:39
print("{}.{}.{}  {}:{}".format(now.day, now.month, now.year, now.hour, now.minute))  # 8.7.2022  12:22
print(now.date()) # 2022-07-08
print(now.time()) # 12:22:44.741900

# Дата сейчас
today = date.today()
print(today) # 2022-07-08     
print("{}.{}.{}".format(today.day, today.month, today.year)) # 8.7.2022 

# Конкретная дата
yesterday = datetime.date(2017,5, 2)
print(yesterday)      # 2017-05-02


# Текущее время
current_time = time()
print(current_time)     # 00:00:00

# Конкретное время  
current_time = time(16, 25, 45)
print(current_time)     # 16:25:45    


# Из str в дату
deadline = data_time.strptime("22/05/2017 12:30", "%d/%m/%Y %H:%M")
print(deadline)     # 2017-05-22 12:30:00


# Засечь время работы
start = data_time.now()
# ... wait
wait = timedelta(microseconds=330)
end = data_time.now() + wait
period = end - start
print("{} дней  {} секунд   {} микросекунд".format(period.days, period.seconds, period.microseconds))
# 0 дней  0 секунд   342 микросекунд
print("Всего: {} секунд".format(period.total_seconds())) # Всего: 0.000342 секунд