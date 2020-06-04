import sqlite3

def add():
    conn = sqlite3.connect("uchet.db") # Передаем название файла
    cursor = conn.cursor()

    # Добавление переменных

    inv_number = input('Введите инв номер:')
    name = input('Введите наименование:')

    # Непосредственное добавление строки

    cursor.execute('''INSERT INTO uchet(inv_number, name) VALUES (?,?)''', (inv_number, name))
    conn.commit()
    print('Операция завершена')
    return