from datetime import date, datetime, timedelta
from urllib import response
import requests
import colorama
from colorama import Fore

#
# Определение глобальных переменных и констант
#

# кол-во дней за которое запрашиваются данные
DAYS_BEFORE = 1

#
# Глобальные функции модуля
#

class StackApi:

    # переменные класса
    url = 'https://api.stackexchange.com/2.3'
    site = 'stackoverflow'

    # /questions?fromdate=1648166400&todate=1648339200&order=desc&sort=activity&tagged=Python&site=stackoverflow

    # функция инициализация класса
    def __init__(self, site = '') -> None:

        # инициализация параметров поиска
        if len(site) > 0:
            self.site = site
        
        return None
    
    # функция преобразования даты в unix формат
    def _unixtime(self, dt: datetime) -> str:

        uxdate = datetime.timestamp(dt)
        strdate = str(uxdate).split('.')[0]

        return strdate
    
    # функция получения всех "вопросов"
    def _get_questions(self, fromdate : str, todate: str, tagged: str, site: str) -> dict:

        # формируем папарметры запроса
        params = {'fromdate' : fromdate, 'todate' : todate, 'order' : 'desc', 'sort' : 'activity', 'tagged' : tagged, 'site' : site}
        url = self.url + '/' + 'questions'
        # запрашиваем данные 
        response = requests.get(url, params = params)
        # проверяем результат запроса
        if response.status_code == 200:
            return_dict = response.json()
        else:
            return_dict = {}

        return return_dict

    # функция запроса данных
    def get(self, query: str, fromdate : date, todate : date, tagged: str) -> dict:

        # преобразуем даты в unix формат
        ufromdate = self._unixtime(datetime.combine(fromdate,datetime.max.time()))
        utodate = self._unixtime(datetime.combine(todate,datetime.max.time()))

        # запросы могут быть разного типа: answers, questions, articles ...
        # в рамках домашнего задания обрабатываются только запросты типа "questions"
        if query == 'questions':
            # создаем запрос
            return_dict = self._get_questions(ufromdate, utodate, tagged, self.site)
        
        return return_dict
# end class

#
# Главная функция программы
#

def main():

    # инициализируем библиотеку цветного вывода в консоль
    colorama.init()
    # инициализиреум объект класса StackApi
    stack = StackApi()

    # получаем текущую дату
    todate = date.today()
    fromdate = todate - timedelta(days=DAYS_BEFORE)

    # запрашиваем список вопросов с сайта stackoverflow за последние два дня с тэгом Python
    questions = stack.get('questions', fromdate, todate, 'Python')

    # выводим основную информацию о запросах
    if len(questions) > 0:
        print(Fore.YELLOW + f'Результаты поиска вопросов с {fromdate} по {todate} с тэгом "Python:"')
        print(Fore.WHITE)
        for question in list(questions['items']):
            display_name = question[]
            print('Дата: ', , 'Автор: ', , 'Тема: ', )
    else:
        print(Fore.RED + f'ERROR: результаты с {fromdate} по {todate} не найдены!')

    return True

#
# Основная программа
#

if __name__ == '__main__':
    main()
