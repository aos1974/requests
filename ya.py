import sys
import argparse

#
# Определение глобальных переменных и констант
#

#
# Глобальные функции модуля
#

# функция инициализации объекта парсинга командной строки
def createParser():

    return parser
#
# Главная функция программы
#

def main() -> bool:

    # создаем объект парсинга командной строки
    parser = createParser()
    namespace = parser.parse_args(sys.argv[1:])

    return True

#
# Основная программа
#

if __name__ == '__main__':
    main()

# https://jenyay.net/Programming/Argparse#intro