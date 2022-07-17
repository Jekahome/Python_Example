import os # для работы с каталогами

'''
1. open
2. read/write
3. close

Flags:
    r - Read открывает существующий
    w - Write создает файл заново затирая старый
    a - Append создаст файл или откроет и допишет в конец
    b - Binary используется вместе с 'w' или 'r'

    r+ - как r но может write
    w+ - как w но может read
    a+ - как a но может read

'''

try:
   if os.path.exists('source') == False:
       os.mkdir('source')

   if os.path.exists('source/file_text'):
      print("Указанный файл существует") 
   else:
      print("Файл не существует") 

   # Open
   resource = open("source/file_text",'a+')
  
   # или так (сам закроет файл)
   #with open("file_text",'ar',encoding="utf8") as resource:
   #  text = resource.read()

   # Write
   resource.write("hello world")
   print("hello world", file=resource,end="\n") # или так
   # Read
   '''
      readline(): считывает одну строку из файла
      read(): считывает все содержимое файла в одну строку
      readlines(): считывает все строки файла в список
   '''
   # read 
   content = resource.read()
   
   resource.seek(0)

   # readlines
   contents = resource.readlines()
   print(contents[0])

   # readline
   str1 = resource.readline()
   print(str1, end="")
   str2 = resource.readline()
   print(str2)

   # while + readline
   line = resource.readline()
   while line:
      print(line, end="")
      line = resource.readline()

   # по строчно
   for line in resource:
        print(line, end="")

   resource.close() 
   # Переименовать файл
   os.rename('source/file_text','source/file_text_two')
   # Удаление файла
   os.remove("source/file_text_two")
   # Удалить папку
   os.rmdir("source")
except FileNotFoundError as e:
   print(f"{e}")  
