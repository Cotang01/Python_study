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
import aiohttp


async def get_urls_from_txt(txt_path: str) -> List[str]:
    with open(txt_path, 'r', encoding='UTF-8') as f:
        return f.readlines()


async def download(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            text = await response.content.read()
            image_name, ext = url.strip().split('/')[-1].split('.')
            with open(f'{image_name}.{ext}', "wb") as f:
                f.write(bytes(text))
            print(f"Downloaded {url} in {time.time() - start: .2f} s.")


async def main():
    tasks = []
    for url in await get_urls_from_txt(sys.argv[1]):
        task = asyncio.ensure_future(download(url))
        tasks.append(task)
    await asyncio.gather(*tasks)

start = time.time()

if __name__ == '__main__':
    start = time.time()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    print(f'Total time: {time.time() - start}')
