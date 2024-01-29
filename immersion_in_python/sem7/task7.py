"""
✔ Создайте функцию для сортировки файлов по директориям: видео, изображения,
текст и т.п.
✔ Каждая группа включает файлы с несколькими расширениями.
✔ В исходной папке должны остаться только те файлы, которые не подошли для
сортировки.
"""
import os
from task6 import gen_dir


def sort_files(dir_to_sort: str = '.') -> None:
    masks = {'Music': {'mp4'},
             'Video': {'png', 'jpg', 'jpeg'},
             'Text': {'txt', 'doc', 'docx'}}
    cur_files = [os.path.abspath(f) for f in os.listdir(dir_to_sort)]
    for k in masks.keys():
        gen_dir(k)
    for f in cur_files:
        for k, v in masks.items():
            cur_mask = f.split('.')[-1]
            if cur_mask in v:
                os.replace(os.path.abspath(f), os.path.abspath(k) + f)
