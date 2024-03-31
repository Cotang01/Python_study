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
import threading
import sys
import time
from typing import List
import requests


def get_urls_from_txt(txt_path: str) -> List[str]:
    try:
        with open(txt_path, 'r', encoding='UTF-8') as f:
            return f.readlines()
    except FileNotFoundError as fnfe:
        print(fnfe)


def download(url):
    s = time.time()
    response = requests.get(url)
    image_name, ext = url.strip().split('/')[-1].split('.')
    with open(f'{image_name}.{ext}', "wb") as f:
        f.write(bytes(response.content))
    print(f"Downloaded {url} in {time.time() - s: .2f} s.")


if __name__ == '__main__':
    start = time.time()
    threads = []

    for url in get_urls_from_txt(sys.argv[1]):
        thread = threading.Thread(target=download, args=(url,))
        threads.append(thread)
        thread.start()

    for t in threads:
        t.join()

    print(f'Total time: {time.time() - start}')
