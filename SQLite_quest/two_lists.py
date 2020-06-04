def massive_one():
    # Массив для записи всех чисел.
    numbers = list()
    n = int(input("Введите число эллементов: "))
    # Цикл для записи элементов в список.
    for i in range(n):
       # Запись эллементов в список.
        numb = int(input("Введите эллемент: "))
        numbers.append(numb)
    # Возвращение переменной result_one в тело программы.
    return numbers

def massive_two():
    # Массив для записи всех чисел.
    numbers = list()
    n = int(input("Введите число эллементов: "))
    # Цикл для записи элементов в список.
    for i in range(n):
       # Запись эллементов в список.
        numb = int(input("Введите эллемент: "))
        numbers.append(numb)
    # Возвращение переменной result_one в тело программы.
    return numbers

def comparison():
    res_one = massive_one()
    res_two = massive_two()
    # Нахождение мин. и макс. значений у первого списка и их сложение.
    numb_max = (max(res_one))
    numb_min = (min(res_one))
    result_one = numb_min + numb_max
    # Нахождение мин. и макс. значений у второго списка и их сложение.
    numb_max = (max(res_two))
    numb_min = (min(res_two))
    result_two = numb_min + numb_max
    # Сравнение суммы элементов списка
    if result_one > result_two:
        finish = res_one
    elif result_one == result_two:
        finish = res_two
    else:
        finish = res_two
    return finish
