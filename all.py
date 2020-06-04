import max_elem
import sort_list
import two_lists

print("1. Нахождение максимального элемента в списке")
print("2. Сортировка только простых элементов в списке")
print("3. Сравнение суммы максимального и минимального элементов двух списков")
print()
choose = int(input("Выберите действие: "))
if choose == 1:
    print("Максимальный элемент:", max_elem.number_max())
elif choose == 2:
    print("Отсортированный список:", sort_list.number_sort_odd())
elif choose == 3:
    print(two_lists.comparison())
else:
    print("Введено неверное значение")
