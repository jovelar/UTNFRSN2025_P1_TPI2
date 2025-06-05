class Persona:
    def __init__(self,apellido,nombre,dni):
        self.apellido=apellido
        self.nombre=nombre
        self.dni=dni
    
    def mostrar(self):
        print(f"{self.nombre}, {self.dni}")