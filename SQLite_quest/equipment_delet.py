import sqlite3

def delet():
    conn = sqlite3.connect("uchet.db")
    cursor = conn.cursor()

    # Ввод переменной

    v_poroshok = input('Введите id для удаления строки:')

    # Удаление строки

    cursor.execute("DELETE FROM uchet WHERE id=?", v_poroshok)
    conn.commit()
    return