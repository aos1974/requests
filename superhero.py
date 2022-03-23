import requests
import json
from tokenname import get_connetion_str

#
# Определение глобальных переменных и констант
#

# коды HTTP ошибок и статусов запросов
HTTP_OK = 200
# файл содержащий токен для доступа к api
TOKEN_FILE = 'superhero.token'
# адрес сервиса
URL = 'https://superheroapi.com/api'
# Супегерои
SUPERHEROES = ['Hulk', 'Captain America', 'Thanos']

#
# Глобальные функции модуля
#

# функция получения информации о супергерое
def get_superhero_stats(superhero: str) -> int:

    intelligence = -1
    # формируем строку подключения к сервису
    url = get_connetion_str(TOKEN_FILE, URL) + '/search/' + superhero
    # запрашиваем информацию о супергерое
    response = requests.get(url)
    # определяем уровень интелекта супергероя
    if response.status_code == HTTP_OK:
        js = json.loads(response.text)
        intelligence = js['results'][0]['powerstats']['intelligence']

    return intelligence
#
# Главная функция программы
#

def main() -> str:

    # код завершения работы программы
    error_code = 'ERROR: работа программы завершена с ошибкой'
    superhero_dict = {}
    # запрашиваем уровень интелекта супергероя
    for superhero in SUPERHEROES:
        superhero_level = get_superhero_stats(superhero)
        if superhero_level == -1:
            return error_code
        else:
            superhero_dict[int(superhero_level)] = superhero
    # определяем самого умного супергероя
    error_code = superhero_dict.get(max(superhero_dict.keys()))

    return 'Самый умный супергерой это - ' + error_code
#
# Основная программа
#

if __name__ == '__main__':
    print(main())
