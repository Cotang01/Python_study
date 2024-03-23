"""
� Написать программу, которая считывает список из 10 URL адресов и
одновременно загружает данные с каждого адреса.
� После загрузки данных нужно записать их в отдельные файлы.
� Используйте асинхронный подход.
"""
import asyncio
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


async def get_exchange_rate(url: str) -> float:
    try:
        full_page = requests.request('GET', url)
        soup = BeautifulSoup(full_page.content, 'html.parser')
        return float(
            soup.findAll('div', {'class': 'valvalue'})[0].text.replace(',', '.'))
    except ValueError:
        print(f'Could not get exchange rate from url: {url}')


async def load_exchange_rate_in_txt(url: str) -> None:
    with open(f'{url.split("/")[-2]}.txt', 'a', encoding='UTF-8') as f:
        f.write(str(await get_exchange_rate(url)) + '\n')


async def main():
    for link in urls:
        asyncio.create_task(load_exchange_rate_in_txt(link))


if __name__ == '__main__':
    asyncio.run(main())
