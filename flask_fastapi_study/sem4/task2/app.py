"""
� Написать программу, которая считывает список из 10 URL адресов и
одновременно загружает данные с каждого адреса.
� После загрузки данных нужно записать их в отдельные файлы.
� Используйте процессы.
"""
import multiprocessing
import requests
from bs4 import BeautifulSoup

urls = ["http://www.finmarket.ru/currency/USD/",
        "http://www.finmarket.ru/currency/EUR/",
        "http://www.finmarket.ru/currency/GBP/",
        "http://www.finmarket.ru/currency/JPY/",
        "http://www.finmarket.ru/currency/USD/",
        "http://www.finmarket.ru/currency/EUR/",
        "http://www.finmarket.ru/currency/GBP/",
        "http://www.finmarket.ru/currency/JPY/",
        "http://www.finmarket.ru/currency/USD/",
        "http://www.finmarket.ru/currency/EUR/"]


def get_exchange_rate(url: str) -> float:
    try:
        full_page = requests.request('GET', url)
        soup = BeautifulSoup(full_page.content, 'html.parser')
        return float(
            soup.findAll('div', {'class': 'valvalue'})[0].text.replace(',', '.'))
    except ValueError:
        print(f'Could not get exchange rate from url: {url}')


def load_exchange_rate_in_txt(url: str) -> None:
    with open(f'{url.split("/")[-2]}.txt', 'a', encoding='UTF-8') as f:
        f.write(str(get_exchange_rate(url)) + '\n')


if __name__ == '__main__':
    processes = []
    for link in urls:
        process = multiprocessing.Process(target=load_exchange_rate_in_txt,
                                          args=(link,))
        processes.append(process)
        process.start()

    for p in processes:
        p.join()
