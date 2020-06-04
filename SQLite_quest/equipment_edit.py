import sqlite3

def edit():
    conn = sqlite3.connect("uchet.db")
    chislo = 0
    while chislo != 3:
        print('1. Редактировать инв номер')
        print('2. Редактировать наименование')
        print('3. Выход')
        chislo = int(input('Введите номер нужного пункта'))
        # Редактирование инв номера
        if chislo == 1:
            edit_id = input('Введите id:')
            edit_invNumber = input('Введите инв номер:')
            with conn:
                cursor = conn.cursor()
                cursor.execute("UPDATE uchet SET inv_number=? WHERE id=?", (edit_invNumber, edit_id))
                conn.commit()
        # Редактирование наименования
        elif chislo == 2:
            edit_id = input('Введите id:')
            edit_name = input('Введите наименование:')
            with conn:
                cursor = conn.cursor()
                cursor.execute("UPDATE uchet SET name=? WHERE id=?", (edit_name, edit_id))
                conn.commit()
        # Выход из функции
        elif chislo == 3:
            return
        # Ввод некорректного числа
        else:
            print('Введите корректное число')
    return
