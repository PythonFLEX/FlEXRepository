def massive_one():
    # Массив для записи всех чисел.
    numbers = list()
    n = int(input("Введите число эллементов: "))
    # Цикл для записи элементов в список.
    for i in range(n):
       # Запись эллементов в список.
        numb = int(input("Введите эллемент: "))
        numbers.append(numb)
    # Нахождение мин. и макс. значений и их сложение.
    numb_max = (max(numbers))
    numb_min = (min(numbers))
    result_one = numb_min + numb_max
    # Возвращение переменной result_one в тело программы.
    return result_one

def massive_two():
    # Массив для записи всех чисел.
    numbers = list()
    n = int(input("Введите число эллементов: "))
    # Цикл для записи элементов в список.
    for i in range(n):
       # Запись эллементов в список.
        numb = int(input("Введите эллемент: "))
        numbers.append(numb)
    # Нахождение мин. и макс. значений и их сложение.
    numb_max = (max(numbers))
    numb_min = (min(numbers))
    result_two = numb_min + numb_max
    # Возвращение переменной result_one в тело программы.
    return result_two

def comparison():
    # Сравнение суммы элементов списка
    if res_one > res_two:
        total = print("Сумма элементов первого списка больше")
    elif res_one == res_two:
        total = print("Сумма элементов обоих списков равна")
    else:
        total = print("Сумма элементов второго списка больше")
    return total

res_one = massive_one()
res_two = massive_two()
result = comparison()

