def comparison():
    # Первый массив для записи всех чисел.
    numbers_one = list()
    n = int(input("Введите число эллементов: "))
    # Цикл для записи элементов в первый список.
    for i in range(n):
       # Запись эллементов в первый список.
        numb = int(input("Введите эллемент: "))
        numbers_one.append(numb)
    # Второй массив для записи всех чисел.
    numbers_two = list()
    n = int(input("Введите число эллементов: "))
    # Цикл для записи элементов во второй список.
    for i in range(n):
       # Запись эллементов во второй список.
        numb = int(input("Введите эллемент: "))
        numbers_two.append(numb)
    # Нахождение мин. и макс. значений у первого списка и их сложение.
    result_one = (max(numbers_one)) + (min(numbers_one))
    # Нахождение мин. и макс. значений у второго списка и их сложение.
    result_two = (max(numbers_two)) + (min(numbers_two))
    # Сравнение суммы элементов списка
    if result_one > result_two:
        finish = numbers_one
    elif result_one == result_two:
        finish = numbers_two, numbers_one
    else:
        finish = numbers_two 
    return finish

print(comparison())
