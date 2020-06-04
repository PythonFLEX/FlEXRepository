def number_sort_odd():
    # Массив для записи всех чисел.
    numbers_compos = list()
    numbers_simple = list()
    n = int(input("Введите число эллементов: "))
    # Цикл для записи элементов в список.
    for i in range(n):
       # Запись эллементов в список.
        numb = int(input("Введите эллемент: "))
        i = 2 
        limit = int(numb ** 0.5)
        d = 1
        # Проверка на простое или составное число
        while i <= limit:
            if numb % i == 0:
                d += 1
            i += 1
        # Запись элементов в список с простыми или составными числами
        if d >= 2:
            numbers_compos.append(numb)
        else:
            numbers_simple.append(numb)
    # Сортировка списка с простыми числами и его склеивание с "составным" списком
    finish = (sorted(numbers_simple)+numbers_compos)
    # Возвращение готового списка в тело программы
    return finish

