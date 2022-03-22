import requests
from tokenname import get_connetion_str

#
# Определение глобальных переменных и констант
#

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
def get_superhero_stats(url: str) -> dict:

    # запрашиваем информацию о супергерое
    response = requests.get(url)

    return response
#
# Главная функция программы
#

def main() -> bool:

    for superhero in SUPERHEROES:
        x = get_superhero_stats(get_connetion_str(TOKEN_FILE, URL) + '/' + superhero)
        print(x)

    return True
#
# Основная программа
#

if __name__ == '__main__':
    main()
