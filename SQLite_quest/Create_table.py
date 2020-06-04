import sqlite3

def create():
    choose = 0
    while choose != 2:
        print('У вас создана база данных?')
        print('1. yes')
        print('2. no')
        choose = int(input())
        if choose == 1:
            return
        elif choose == 2:
            conn = sqlite3.connect("uchet.db")  # Передаем название файла
            cursor = conn.cursor()

            # Создаем Таблицу

            cursor.execute("""CREATE TABLE uchet
                          (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, inv_number, name)
                       """)
        else:
            print('Введите корректное число')
