from sqlite3 import *
conn=connect("./BASE_DATOS/tecnologico.db")
conn.commit()
conn.close()

def crearTablaAlumno():
    conn=connect("./BASE_DATOS/tecnologico.db")
    cursor=conn.cursor()
    sentencia="""
        CREATE TABLE IF NOT EXISTS Alumnos(
            id INTEGER PRIMARY KEY AUTOINCREMENT, 
            nombre TEXT(250), 
            edad INTEGER
        )
    """

    cursor.execute(sentencia)
    conn.commit()
    conn.close()

def crearTablaCurso():
    conn=connect("./BASE_DATOS/tecnologico.db")
    cursor=conn.cursor()
    sentencia="""
        CREATE TABLE IF NOT EXISTS Cursos(
            id INTEGER PRIMARY KEY AUTOINCREMENT, 
            nombre TEXT(250), 
            id_alumno INTEGER,
            FOREIGN KEY(id_alumno)REFERENCES Alumnos(id)
        )
    """

    cursor.execute(sentencia)
    conn.commit()
    conn.close()

if __name__=="__main__":
    crearTablaAlumno()
    crearTablaCurso()

def crearTablaAlumno():
    conn=connect("./BASE_DATOS/tecnologico.db")
    cursor=conn.cursor()
    sentencia="""
        CREATE TABLE IF NOT EXISTS Alumnos(
            id INTEGER PRIMARY KEY AUTOINCREMENT, 
            nombre TEXT(250), 
            edad INTEGER
        )
    """

    cursor.execute(sentencia)
    conn.commit()
    conn.close()

def insertAlumno(nombre,edad):
    conn=connect("./BASE_DATOS/tecnologico.db")
    cursor=conn.cursor()
    sentencia=f"INSERT INTO Alumnos(nombre,edad) VALUES('{nombre}',{edad})"

    cursor.execute(sentencia)
    conn.commit()
    conn.close()

if __name__=="__main__":
    insertAlumno("jory",20)
    insertAlumno("chinita",12)

def insertAlumnos(lista):
    conn=connect("./BASE_DATOS/tecnologico.db")
    cursor=conn.cursor()
    sentencia=f"INSERT INTO Alumnos(nombre,edad) VALUES(?,?)"

    cursor.executemany(sentencia,lista)
    conn.commit()
    conn.close()

if __name__=="__main__":
    alum=[
        ("jorycha",50),
        ("chinita",60),
        ("nidincita",18),
        ("mochucha",15),
        ("viuda negra",300)
    ]
    insertAlumnos(alum)