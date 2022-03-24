import sys
import argparse
from tokenname import get_connetion_str

#
# Определение глобальных переменных и констант
#

# файл содержащий токен для доступа к api
TOKEN_FILE = 'yandex.token'
# файл для загрузки на сервер
UPLOAD_FILE = 'upload.txt'
# адрес сервиса
URL = 'https://superheroapi.com/api'

#
# Глобальные функции модуля
#

# функция инициализации объекта парсинга командной строки
def createParser():

    # создаем объект парсинга командной строки
    parser = argparse.ArgumentParser()
    # добавляем аргументы командной строки
    # --upload, параметр загрузки файла на удаленный сервер
    # --file, имя файла загружаемого на сервер  
    # --url, адрес сервера
    # --token, имя файла с токеном для подключения к серверу
    parser.add_argument('--upload', type=bool, default=True)
    parser.add_argument('--file', type=str, default=UPLOAD_FILE)
    parser.add_argument('--url', type=str, default=URL)
    parser.add_argument('--token', type=str, default=TOKEN_FILE)

    return parser

# функция загрузки файла на сервер
def ya_upload_file(file: str, url: str) -> bool:

    return True
#
# Главная функция программы
#

def main() -> bool:

    # создаем объект парсинга командной строки
    parser = createParser()
    namespace = parser.parse_args(sys.argv[1:])

    print('Программа запущена со следующими параметрами:')
    print(f'--upload {namespace.upload}')
    print(f'--file {namespace.file}')
    print(f'--url {namespace.url}')
    print(f'--token {namespace.token}')
    print('Для изменения параметров запуска задайте параметры в командной строке!')

    if namespace.upload:
        if ya_upload_file(namespace.file, namespace.url):
            print(f'Файл {namespace.file} успешно загружен по адресу "{namespace.url}"')
        else:
            print('ERROR: в процессе загрузки произошла ошибка!')
    else:
        print('Функция "download" в данной версии программы не ркализована!')

    return True

#
# Основная программа
#

if __name__ == '__main__':
    main()
