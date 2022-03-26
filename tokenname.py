import os.path

#
# Глобальные функции модуля
#

# функция загрузки токена из файла
def load_token_from_file(fname: str) -> str:

    # строка с токеном
    tokenname = ''
    # проверяем наличие файла для загрузки токена
    if os.path.isfile(fname):
        # открываем файл и считываем токен
        with open(fname, 'r', encoding='utf-8') as token_file:
            tokenname = token_file.readline().strip()

    return tokenname
# конец функции загрузки токена

# функция формирования строки подключения
def get_connetion_str(token_file: str, url: str) -> str:

    # загружаем токен из файла
    token_str = load_token_from_file(token_file)
    # формируем строку подключения если токен загрузился
    if len(token_str) > 0:
        connection_str = url + '/' + token_str + '/'
    else:
        # возвращаем пустую строку если токен не загрузился
        connection_str = ''

    return connection_str
# конец функции формирования строки подключения
