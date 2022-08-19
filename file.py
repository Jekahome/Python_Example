import os # для работы с каталогами
import sys 

'''
1. open()
2. read()/write()
3. close()

   truncate()
   seek()
   readline()
   readlines()

Flags:
    r - Read открывает существующий
    w - Write создает файл заново затирая старый
    a - Append создаст файл или откроет и допишет в конец
    b - Binary используется вместе с 'w' или 'r'

    r+ - как r но может write
    w+ - как w но может read
    a+ - как a но может read

'''
def file_example(params):
   try:
      if os.path.exists('source') == False:
         os.mkdir('source')

      if os.path.exists('source/file_text'):
         print("Указанный файл существует") 
      else:
         print("Файл не существует") 

      # Open
      resource = open("source/file_text",'a+')
      # изменить размер файла
      resource.truncate(0)
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
# ---------------------------------------------------------------------------------------
def dir_example(params):
   try:
      DIR = r'source'
      DIR_DST = os.path.join(DIR, 'dst')
      if os.path.exists(DIR) == False:
         os.mkdir('source')
         os.mkdir(DIR_DST)
         os.mkdir(os.path.join(DIR, '1'));open(os.path.join(DIR, '1')+ "/aaa.txt",'w') 
         os.mkdir(os.path.join(DIR, '2'));open(os.path.join(DIR, '2')+ "/bbb.txt",'w') 
         os.mkdir(os.path.join(DIR, '3'));open(os.path.join(DIR, '3')+ "/eee.txt",'w') 
      
      dirs = ['1','2','3']   
      for dir_name in dirs:
         path_dir = os.path.join(DIR, dir_name)
         index = dirs.index(dir_name) 
         # Перебрать все файлы из текущей директории  
         for file_name in os.listdir(path_dir):
               file_path = os.path.join(path_dir,file_name)
               # скопировать файлы из текущей папки в аналогичную папку в dst
               dir_dst = os.path.join(DIR_DST,dir_name)
               if os.path.exists(dir_dst) == False:
                  os.mkdir(dir_dst)  
               open(os.path.join(dir_dst, file_name) ,'w') 
   except FileNotFoundError as e:
      print(f"{e}")                
      exc_type, exc_obj, exc_tb = sys.exc_info()
      fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
      print(exc_type, fname, exc_tb.tb_lineno)        
                  
# ---------------------------------------------------------------------------------------
def main(params):  
    if False:
        file_example(params)   
    if True:
        dir_example(params)   
          
        
if __name__ == "__main__":
    main(sys.argv[1:])
    
