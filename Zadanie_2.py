def number_sort_odd():
    # Массив для записи всех чисел.
    numbers = list()
    n = int(input("Введите число эллементов: "))
    # Цикл для записи элементов в список.
    for i in range(n):
       # Запись эллементов в список.
        numb = int(input("Введите эллемент: "))
        numbers.append(numb)
    # Сортировка нечетных элементов
    number_sort = sorted([i for i in numbers if i % 2 != 0])
    odd_int = 0
    for i in range(len(numbers)):
        if numbers[i] % 2 != 0:
            numbers[i] = number_sort[odd_int]
            odd_int += 1
    # Возвращение отсортированного массива в тело программы.
    return numbers

print("Отсортированный список:", number_sort_odd ())
