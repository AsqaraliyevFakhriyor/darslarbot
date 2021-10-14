import sqlite3

db = sqlite3.connect('file_ids.db', check_same_thread=False)
sql = db.cursor()
sql.execute('''CREATE TABLE IF NOT EXISTS file_ids(
            file_name VARCHAR, 
            file_id VARCHAR)''')
# sqlite3.connect(":memory:", check_same_thread=False)
# user_command = 'start'
# while user_command == 'start':
#     file_name = input("name-> ")
#     file_id = input("id-> ")

# sql.execute("INSERT INTO file_ids VALUES(?,?)", (file_name, file_id))
db.commit()

def dars(file_name_from_main):
    file_name = file_name_from_main
    return str(sql.execute("SELECT file_id FROM file_ids WHERE file_name = ?", (file_name,)).fetchone()[0])



