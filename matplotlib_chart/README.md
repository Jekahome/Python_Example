# Виртуальная среда virtualenv 
https://wiki.archlinux.org/title/Python_(%D0%A0%D1%83%D1%81%D1%81%D0%BA%D0%B8%D0%B9)/Virtual_environment_(%D0%A0%D1%83%D1%81%D1%81%D0%BA%D0%B8%D0%B9)#:~:text=%D0%92%D0%B8%D1%80%D1%82%D1%83%D0%B0%D0%BB%D1%8C%D0%BD%D0%BE%D0%B5%20%D0%BE%D0%BA%D1%80%D1%83%D0%B6%D0%B5%D0%BD%D0%B8%D0%B5%20(virtual%20environment)%20%E2%80%94,%D1%83%D1%81%D1%82%D0%B0%D0%BD%D0%BE%D0%B2%D0%BA%D0%B8%20%D0%B4%D1%80%D1%83%D0%B3%D0%B8%D1%85%20%D0%BC%D0%BE%D0%B4%D1%83%D0%BB%D0%B5%D0%B9%20%D0%B2%20%D0%BE%D0%BA%D1%80%D1%83%D0%B6%D0%B5%D0%BD%D0%B8%D0%B8.

 virtualenv — это инструмент, используемый для создания изолированного рабочего пространства для приложения Python. Он даёт некоторые преимущества: например, возможность локальной установки модулей, экспорта рабочей среды и выполнения программы Python внутри этого окружения.
Виртуальное окружение (virtual environment) — это каталог, в который устанавливаются некоторые исполняемые файлы и скрипты. Среди файлов есть python для выполнения скриптов и pip для установки других модулей в окружении. 
По сути, виртуальное окружение имитирует полную системную установку Python и всех необходимых модулей, не вмешиваясь в работу системы, на которой будет запускаться приложение.

```bash
Install:
$ python3 -m pip install --user virtualenv
```

Создание:
Используйте venv или virtualenv для создания виртуального окружения в каталоге вашего проекта. 
Не забудьте исключить каталог venv из вашей системы контроля версий — для его восстановления достаточно копии pip freeze

```bash
$ cd project_dir
$ virtualenv envname
```

# Активация:
```bash
 $ source ../envname/bin/activate
 (envname) jeka@jeka:~/Projects/Python$
```

Теперь команды python и pip будут запускаться и управлять пакетами только внутри виртуального окружения, не затрагивая систему.
Для выхода из виртуального окружения выполните функцию, которую создал скрипт активации:
# Деактивация:
```bash
(envname) $ deactivate
```

# Построение графиков в Python при помощи Matplotlib
https://python-scripts.com/matplotlib и https://matplotlib.org/stable/gallery/index.html

Matplotlib Install:
```bash
(envname) $ pip3 install matplotlib
sudo apt-get install -y python3-tk
```
