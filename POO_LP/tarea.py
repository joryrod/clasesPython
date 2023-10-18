
alumnos=[
    {
        'ID':1,
        'NOMBRE':'Orlando',
        'APELLIDO':'Lopez Santaria',
        'DNI':7454522,
        'EDAD':20,
        'SEXO':'M',
        'PERIODO ACADEMICO':'III periodo',
        'PROGRAMA DE ESTUDIO':'APSTI'
        
    }
]


class Alumno:
   
    def __init__(self, nombre, apellido, dni, edad, sexo, periodo, programa='APSTI'):
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
            'ID':nuevo_id,
            'NOMBRE':self.nombre,
            'APELLIDO':self.apellido,
            'DNI':self.dni,
            'EDAD':self.edad,
            'SEXO':self.sexo,
            'PERIODO ACADEMICO':self.periodo,
            'PROGRAMA DE ESTUDIO':self.programa
        }
            
        registro_alumno=alumnos.append(alumno_nuevo)
        return 'El siguienten alumno fue registrado exitosamente: {alumno_nuevo}'

    def eliminar_alumno(self, id):
        alumno_eliminar=alumnos.pop(id-1)
        return f"el siguiente alumno fue eliminado: {alumno_eliminar}"

    def actualizar_alumno(self, id, clave, valor):
         ol=valor
         actualizacion= list(filter(lambda obj: obj[clave]==id, alumnos))[0].update({clave:valor}) 
        # alumnos[id-1][clave]=valor
        # pass
    

a=Alumno('Maria','Calle Limascca',73211542, 19,'F', 'IV periodo')
print(a.registrar_alumno())
print(a.mostrar_alumnos())
# print(a.mostrar_alumno(1))
# print(a.mostrar_alumnos())
# print(a.eliminar_alumno(2))
# print(a.mostrar_alumnos())
#--print(a.actualizar_alumno(1,clave='edad',valor='sexo'))
print(a.actualizar_alumno())
print(a.mostrar_alumnos(73211542, 'DNI'))