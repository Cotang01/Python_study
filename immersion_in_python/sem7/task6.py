"""
✔ Дорабатываем функции из предыдущих задач.
✔ Генерируйте файлы в указанную директорию — отдельный параметр функции.
✔ Отсутствие/наличие директории не должно вызывать ошибок в работе функции
(добавьте проверки).
✔ Существующие файлы не должны удаляться/изменяться в случае совпадения имён.
"""
import os
from task5 import gen_rng_masks_files


def gen_files_in_dir(dir_path: str = '.',
                     masks: list[str] = (),
                     files_count: int = 42):
    real_path = gen_dir(dir_path)
    os.chdir(real_path)
    gen_rng_masks_files(masks, files_count)


def gen_dir(dir_path: str) -> str:
    counter = 1
    while os.path.exists(dir_path):
        dir_path = f'{os.path.abspath(dir_path)}({str(counter)})'
        counter += 1
    os.mkdir(dir_path)
    return dir_path
