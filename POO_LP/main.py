class Perro: # el nombre de la clase ebera ser singular y con la primera letra mayusula.
    nombre="boby"
    edad="2 meses"
    color="marron"
    raza="chihuahua"

    def ladra(self):
        return "un ladrido"
    
    def corre(self,pasos):
        corriste= f"corriste {pasos} pasos"
        return corriste
    
res=Perro()
print(res.nombre)

print(res.ladra())

print(res.corre(12))