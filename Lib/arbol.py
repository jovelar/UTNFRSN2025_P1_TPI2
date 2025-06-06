from Lib.Persona import Persona
class Nodo:
    def __init__(self,apellido):
        self.apellido=apellido
        self.arreglo=[]
        self.izquierda=None
        self.derecha=None
    

class ArbolBinario:
    def __init__(self):
        self.raiz=None

    def insertar(self,apellido):
        #Si el arbol esta vacio, se crea el primer nodo con el apellido indicado
        if self.raiz==None:
            self.raiz=Nodo(apellido)
        else:
            self.insertarRecursivo(self.raiz,apellido)

    #Inserta de forma recursiva
    def insertarRecursivo(self, nodo, apellido):
        if apellido == nodo.apellido:
            # Si el nodo con el apellido indicado ya existe, no se agrega y se termina la recursion
            return
        elif apellido < nodo.apellido:
            #Si el nodo esta vacio, se crea uno nuevo
            if nodo.izquierda is None:
                nodo.izquierda = Nodo(apellido)
            else:
                #Se continua avanzando por el lado izquierdo del arbol
                self.insertarRecursivo(nodo.izquierda, apellido)
        else:
            #Si el nodo esta vacio, se crea uno nuevo
            if nodo.derecha is None:
                nodo.derecha = Nodo(apellido)
            else:
                #Se continua avanzando por el lado derecho del arbol
                self.insertarRecursivo(nodo.derecha, apellido)
    
    def mostrar(self):
        if self.raiz==None:
            print("Lista vacia!")
        else:
            self.mostrarInorderRec(self.raiz)
    
    #Funcion auxiliar de mostrar()
    def mostrarInorderRec(self,nodo):
        if nodo.izquierda!=None:
            self.mostrarInorderRec(nodo.izquierda)
        print(f"XXX{nodo.apellido}XXX")
        print("Gol de river")
        self.mostrarPersonas(nodo.arreglo)
        listado=nodo.arreglo
        if nodo.derecha!=None:
            self.mostrarInorderRec(nodo.derecha)

    def buscarNodoRec(self,nodo,apellido):
        posicion = None
        if nodo is None:
            return None
        if nodo.apellido == apellido:
            return nodo
        elif apellido < nodo.apellido:
            return self.buscarNodoRec(nodo.izquierda,apellido)
        else:
            return self.buscarNodoRec(nodo.derecha,apellido)
    
    def buscarPersona(self,nodo,nombre):
        encontrado=False
        for persona in nodo.arreglo:
            if persona.nombre==nombre:
                encontrado=True
        return encontrado


    def agregarPersona(self, persona):
        posicion = self.buscarNodoRec(self.raiz, persona.apellido)
        if posicion == None:
            self.insertar(persona.apellido)
            posicion = self.buscarNodoRec(self.raiz, persona.apellido)
        posicion.arreglo.append(persona)

    def mostrarInorderRec(self,nodo):
        #Si la rama izquierda no esta vacia accede
        if nodo.izquierda!=None:
            self.mostrarInorderRec(nodo.izquierda)
        print(nodo.apellido)
        self.mostrarPersonas(nodo.arreglo)
        listado=nodo.arreglo
        #Si la rama derecha no esta vacia accede
        if nodo.derecha!=None:
            self.mostrarInorderRec(nodo.derecha)

    def mostrarPersonas(self,arreglo):
        for persona in arreglo:
            persona.mostrar()

    def borrarPersona(self,nodo):
        apellidoABuscar=input("Ingrese el apellido de la persona a eliminar: ")
        posicion=self.buscarNodoRec(nodo,apellidoABuscar)
        if posicion==None:
            print("No se encuentra el apellido")
        else:
            encontrado = None
            nombre=input("Ingrese el nombre a borrar: ")
            for persona in posicion.arreglo:
                if persona.nombre == nombre:
                    encontrado = persona
                    break

            if encontrado:
                posicion.arreglo.remove(encontrado)
                print("¡Eliminado!")
            else:
                print("No se encontró el nombre indicado")


