def print_name(prefix):
    print(f'Ищем префикс {prefix}')
    try:
        while True:
            name = (yield)
            if prefix in name:
                print(name)
    except GeneratorExit:
        print('Корутина (coroutine) завершена')

corou = print_name('Уважаемый')
corou.__next__()
corou.send('товарищ')
corou.send('Уважаемый товарищ')
corou.close()