def number_max():
    # Массив для записи всех чисел.
    numbers = list()
    n = int(input("Введите число эллементов: "))
    # Цикл для записи элементов в список.
    for i in range(n):
       # Запись эллементов в список.
        numb = int(input("Введите эллемент: "))
        numbers.append(numb)
    results = (max(numbers))
    # Возвращение переменной results в тело программы.
    return results

maximum = number_max ()
print("Максимальный элемент списка: ",maximum)
