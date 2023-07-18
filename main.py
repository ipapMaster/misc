import time
from datetime import datetime


def dish(num, prepare, wait):
    """
    num: номер блюда по порядку
    prepare: время на подготовку
    wait: ожидание готовности
    """
    print(f'{datetime.now().strftime("%H:%S")} - подготовка к приготовлению блюда {num} - {prepare} мин.')
    time.sleep(prepare)
    print(f'Начало приготовления блюда {num} - {datetime.now().strftime("%H:%S")}. Ожидание блюда {num} {wait} мин.')
    time.sleep(wait)
    print(f'В {datetime.now().strftime("%H:%S")}. блюдо {num} готово.')


t0 = time.time()  # время начало работы
dish(1, 2, 3)
dish(2, 5, 10)
dish(3, 3, 5)
delta = int(time.time() - t0)  # затраченное время
print(f'В {datetime.now().strftime("%H:%S")} мы закончили')
print(f'Затрачено времени - {delta}')