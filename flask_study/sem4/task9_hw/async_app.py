"""
� Написать программу, которая скачивает изображения с заданных URL-адресов и
сохраняет их на диск. Каждое изображение должно сохраняться в отдельном
файле, название которого соответствует названию изображения в URL-адресе.
� Например URL-адрес: https://example/images/image1.jpg -> файл на диске:
image1.jpg
� Программа должна использовать многопоточный, многопроцессорный и
асинхронный подходы.
� Программа должна иметь возможность задавать список URL-адресов через
аргументы командной строки.
� Программа должна выводить в консоль информацию о времени скачивания
каждого изображения и общем времени выполнения программы.
"""
import asyncio
import sys
import time
from typing import List
import requests


async def get_urls_from_txt(txt_path: str) -> List[str]:
    with open(txt_path, 'r', encoding='UTF-8') as f:
        return f.readlines()


async def load_image(url: str) -> None:
    try:
        s = time.time()
        image_name, ext = url.strip().split('/')[-1].split('.')
        image_data = requests.get(url).content
        with open(f'{image_name}.{ext}', 'wb') as f:
            f.write(image_data)
        print(f'Image {image_name}.{ext} has been loaded in '
              f'{time.time() - s} s.')
    except ValueError:
        print(f'Could not get image from url: {url}')


async def main():
    try:
        for link in await get_urls_from_txt(sys.argv[1]):
            asyncio.create_task(load_image(link))
    except FileNotFoundError as fnfe:
        print(fnfe)
    except IndexError:
        print('Additional argument has not been provided')


if __name__ == '__main__':
    s = time.time()
    asyncio.run(main())
    print(f'Total time: {time.time() - s}')
