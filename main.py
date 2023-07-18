import threading


def print_cube(num):
    """
    Вычиcляет куб от заданного числа num
    """
    print(f'Куб {num} -> {num * num * num}')


def print_square(num):
    """
    Вычиcляет квадрат от заданного числа num
    """
    print(f'Квадрат {num} -> {num ** 2}')


if __name__ == '__main__':
    # создаём два потока
    thread1 = threading.Thread(target=print_square, args=(10,))
    thread2 = threading.Thread(target=print_cube, args=(10,))

    thread1.start()  # запуск первого потока
    thread2.start()  # запуск первого потока

    thread1.join()  # ожидание пока поток 1 завершится
    thread2.join()  # ожидание пока поток 2 завершится

    print('Процессы завершены')