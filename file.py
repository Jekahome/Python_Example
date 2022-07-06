'''
1. open
2. read/write
3. close

Flags:
    r - Read открывает существующий
    w - Write создает файл заново затирая старый
    a - Append создаст файл или откроет и допишет в конец
    b - Binary используется вместе с 'w' или 'r'
'''

try:
   resource = open("file_text",'a')
   resource.write("hello world")
except FileNotFoundError as e:
   print(f"{e}")
finally:
    resource.close()   
