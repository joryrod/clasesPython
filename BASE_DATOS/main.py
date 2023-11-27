from sqlite3 import *
conn=connect("./BASE_DATOS/tecnologico.db")
conn.commit()
conn.close()