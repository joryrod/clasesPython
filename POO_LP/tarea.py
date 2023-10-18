alumnos=[
    {
        'id':1,
        'nombre':'Jory',
        'apellido':'Rodriguez Camargo',
        'dni':47686117,
        'edad':30,
        'sexo':'M',
        'periodo academico':'IV periodo',
        'programa de estudio':'apsti'
        
    }
]


class Alumno:
   
    def __init__(self, nombre, apellido, dni, edad, sexo, periodo, programa):
        self.nombre=nombre
        self.apellido=apellido
        self.dni=dni
        self.edad=edad
        self.sexo=sexo
        self.periodo=periodo
        self.programa=programa


   
    def mostrar_alumnos(self):
        mensaje=f"""
        tienes {len(alumnos)} alumnos registrados
        los Alumnos son:
        {alumnos}
        """
        return mensaje
    def mostrar_alumno(self, id):
        producto_buscar=alumnos[id-1] 
        pass

    def registrar_alumno(self):
        nuevo_id=len(alumnos)+1
        alumno_nuevo={
            'id':nuevo_id,
            'nombre':self.nombre,
            'apellido':self.apellido,
            'dni':self.dni,
            'edad':self.edad,
            'sexo':self.sexo,
            'periodo academico':self.periodo,
            'programa de estudio':self.programa
        }
            
        registro_alumno=alumnos.append(alumno_nuevo)
        return 'El siguienten alumno fue registrado exitosamente: {alumno_nuevo}'

    def eliminar_alumno(self, id):
        alumno_eliminar=alumnos.pop(id-1)
        return f"el siguiente alumno fue eliminado de la lista: {alumno_eliminar}"

    def actualizar_alumno(self, id, clave, valor):
        alumnos[id-1][clave]=valor
        pass
    

a=Alumno('JONATHAN','FLORES CUPE',73211542, 19,'M', 'IV periodo','APSTI')
print(a.mostrar_alumnos())
print(a.registrar_alumno())
print(a.mostrar_alumnos())
print(a.mostrar_alumno(1))
print(a.eliminar_alumno(2))
print(a.mostrar_alumnos())
print(a.actualizar_alumno(1,clave='edad',valor='aceite'))