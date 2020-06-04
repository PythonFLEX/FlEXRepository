def Sqlite():
    import sqlite3
    import equipment_edit
    import equipment_add
    import equipment_delet
    import equipment_export
    import Create_table

    Create_table.create()
# Работа с базой данных
    chislo = 0
    while chislo != 5:
        print('1. Добавление данных в строку')
        print('2. Редактирование данных строки')
        print('3. Удаление строки с данными')
        print('4. Экспорт в JSON')
        print('5. Выход')
        chislo = int(input('Введите номер пункта:'))
        if chislo == 1:
            equipment_add.add()
        elif chislo == 2:
            equipment_edit.edit()
        elif chislo == 3:
            equipment_delet.delet()
        elif chislo == 4:
            equipment_export.export()
        elif chislo == 5:
            return
        else:
            print('Неверный номер')
    return
