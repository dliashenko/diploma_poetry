from sqlite3 import dbapi2 as sqlite

def clean_unwanted_symbols(conn):
    cursor = conn.cursor()
    cursor.execute('DELETE FROM dictionary WHERE stressed_word NOT IN'
                   '(SELECT stressed_word FROM dictionary '
                   'WHERE stressed_word LIKE "%*%")')
    cursor.execute('DELETE FROM dictionary WHERE stressed_word IN'
                   '(SELECT stressed_word FROM dictionary '
                   'WHERE stressed_word LIKE "%[,@ ()123456789]%")')
    cursor.close()




if __name__ == "__main__":
    connection = sqlite.connect("../resources/dictionary.db")
    clean_word_column(connection)
    #clean_stressed_column(connection)
    connection.commit()
    connection.close()
