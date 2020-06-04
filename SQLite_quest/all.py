import select_options
import max_element
import sort_list
import two_lists

choose = 0
while choose != 5:
    print("1. Нахождение максимального элемента в списке")
    print("2. Сортировка только простых элементов в списке")
    print("3. Сравнение суммы максимального и минимального элементов двух списков")
    print("4. Работа с SQLite")
    print("5. Выход")
    choose = int(input("Выберите действие: "))
    if choose == 1:
        print("Максимальный элемент:", max_elem.number_max())
    elif choose == 2:
        print("Отсортированный список:", sort_list.number_sort_odd())
    elif choose == 3:
        print(two_lists.comparison())
    elif choose == 4:
        select_options.Sqlite()
    elif choose == 5:
        print('Выход...')
    else:
        print("Введено неверное значение")