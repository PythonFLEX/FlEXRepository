import sqlite3
import json # импортируем json ибо без него никуда

def export():
    conn = sqlite3.connect("uchet.db")
    conn.row_factory = lambda c, r: dict([(col[0], r[idx]) for idx, col in enumerate(c.description)])
    c = conn.cursor()

    # Выбираем наш db файл

    c.execute('select * from uchet')

    # Сохраняем весь лист в result

    result = c.fetchall()
    print(list(result))

    # Экспорт в JSON

    with open('uchet.json', 'w') as outfile:
        json.dump(list(result), outfile)

    return

