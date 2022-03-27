import os
import sys
import argparse
import requests
import colorama
from colorama import Fore
from tokenname import load_token_from_file

#
# Определение глобальных переменных и констант
#

# файл содержащий токен для доступа к api
TOKEN_FILE = 'yandex.token'
# файл для загрузки на сервер
UPLOAD_FILE = 'upload.txt'
# имя папки в которую загружаем файл
UPLOAD_FOLDER = 'Upload'
# адрес сервиса
URL = 'https://cloud-api.yandex.net/v1/disk/resources'

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
    parser.add_argument('--upload', default=True, type=lambda x: (str(x).lower() == 'true'))
    parser.add_argument('--file', type=str, default=UPLOAD_FILE)
    parser.add_argument('--url', type=str, default=URL)
    parser.add_argument('--token', type=str, default=TOKEN_FILE)

    return parser

# функция загрузки файла на сервер
def ya_upload_file(file: str, url: str, token_file: str) -> bool:

    # загружаем из файла токен
    token = load_token_from_file(token_file)
    if len(token) == 0:
        print(Fore.RED + f'ERROR: невозможно загрузить токен из файла {token_file}!')
        return False
    
    # подготавливаем параметры подключения
    headers = {'Content-Type': 'application/json', 'Accept': 'application/json', 'Authorization': f'OAuth {token}'}

    # проверяем наличие папки для загрузки
    params = {'path': UPLOAD_FOLDER, 'overwrite': 'true'}
    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 404:
        # если папки не существует, то создаем ее
        response = requests.put(url, headers=headers, params=params)

    # если ошибка при обращении/создании папки на ресурсе 
    if response.status_code != 200:
        print(Fore.RED + f'ERROR: ошибка обращения к {url}!')
        return False

    # формируем ссылку для загрузки файла
    params = {'path': UPLOAD_FOLDER + '/' + file.split('/')[len(file.split('/'))-1], 'overwrite': 'true'}
    response = requests.get(url + '/' + 'upload', headers=headers, params=params)
    # если ошибка при получении линка для загрузки
    if response.status_code != 200:
        print(Fore.RED + f'ERROR: ошибка формирования ссылки для загрузки!')
        return False
    # извлекаем ссылку для загрузки
    href = response.json().get('href', '')
    
    # проверяем наличие файла для загрузки
    if os.path.isfile(file):
        # загружаем файл на ресурс
        response = requests.put(href, data=open(file, 'rb'))
        # если оншибка при загрузке
        if response.status_code != 201:
            print(Fore.RED + f'ERROR: ошибка загрузки файла на yandex.диск!')
            return False
    else:
        print(Fore.RED + f'ERROR: файл {file} для загрузки не найден!')
        return False        

    return True
#
# Главная функция программы
#

def main() -> bool:

    # инициализируем библиотеку цветного вывода в консоль
    colorama.init()
    # создаем объект парсинга командной строки
    parser = createParser()
    namespace = parser.parse_args(sys.argv[1:])
 
    print(Fore.LIGHTBLACK_EX + '')
    print('Программа запущена со следующими параметрами:')
    print(f'--upload {namespace.upload}')
    print(f'--file {namespace.file}')
    print(f'--url {namespace.url}')
    print(f'--token {namespace.token}')
    print('Для изменения параметров запуска задайте параметры в командной строке!')

    if namespace.upload:
        if ya_upload_file(namespace.file, namespace.url, namespace.token):
            print(Fore.YELLOW + f'Файл {namespace.file} успешно загружен по адресу "{namespace.url}"')
        else:
            print(Fore.RED + 'ERROR: в процессе загрузки произошла ошибка!')
    else:
        print(Fore.YELLOW + 'Функция "download" в данной версии программы не реализована!')

    return True

#
# Основная программа
#

if __name__ == '__main__':
    main()
