from Persona import Persona
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
    #Inserta de forma recursiva.
    
    """
    def insertarRecursivo(self,nodo,apellido):
        #Si el apellido nuevo es menor al dato del arbol existente, se prosigue hacia el nodo izquierdo
        if apellido < nodo.apellido:
            #si el nodo esta vacio, se crea un nodo nuevo y se apunta la referencia al mismo
            if nodo.izquierda is None:
                nodo.izquierda = Nodo(apellido)
            else:
            #Si no esta vacio, se continua avanzando por la izquierda
                self.insertarRecursivo(nodo.izquierda,apellido)
        #Si el dato nuevo es mayor al dato del nodo, se prosigue hacia el nodo derecho
        else:
            #Si esta vacio, se crea un nodo nuevo y se apunta la referencia al mismo
            if nodo.derecha is None:
                nodo.derecha = Nodo(apellido)
            else:
            #Si no esta vacio, se continua avanzando por la derecha
                self.insertarRecursivo(nodo.derecha,apellido)
    """

    def mostrarInorderRec(self,nodo):
        if nodo.izquierda!=None:
            self.mostrarInorderRec(nodo.izquierda)
        print(nodo.apellido)
        self.mostrarPersonas(nodo.arreglo)
        listado=nodo.arreglo
        if nodo.derecha!=None:
            self.mostrarInorderRec(nodo.derecha)
    """  
    def buscarNodoRec(self,nodo,apellido):
        #posicion=None
        if nodo.apellido==apellido:
            posicion=nodo
        elif apellido < nodo.apellido:
            self.buscarNodoRec(nodo.izquierda,apellido)
        else:
            self.buscarNodoRec(nodo.derecha,apellido)
        return posicion
    """
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


    """"
    def agregarPersona(self,persona):
        posicion=self.buscarNodoRec(self.raiz,persona.apellido)

        if posicion==None:
            self.insertarRecursivo(self.raiz,persona.apellido)
    """
    def agregarPersona(self, persona):
        posicion = self.buscarNodoRec(self.raiz, persona.apellido)
        if posicion is None:
            self.insertar(persona.apellido)
            posicion = self.buscarNodoRec(self.raiz, persona.apellido)
        posicion.arreglo.append(persona)

    def mostrarInorderRec(self,nodo):
        if nodo.izquierda!=None:
            self.mostrarInorderRec(nodo.izquierda)
        print(nodo.apellido)
        self.mostrarPersonas(nodo.arreglo)
        listado=nodo.arreglo
        if nodo.derecha!=None:
            self.mostrarInorderRec(nodo.derecha)

    def mostrarPersonas(self,arreglo):
        for persona in arreglo:
            persona.mostrar()



    def contarNodosApellido(self, nodo, apellido):
        if nodo is None:
            return 0
        contador_izq = self.contarNodosApellido(nodo.izquierda, apellido)
        contador_der = self.contarNodosApellido(nodo.derecha, apellido)
        return contador_izq + contador_der + (1 if nodo.apellido == apellido else 0)
    
    def contarNodos(self, nodo):
        if nodo is None:
            return 0
        cantidad_izquierda = self.contarNodos(nodo.izquierda)
        cantidad_derecha = self.contarNodos(nodo.derecha)
        return 1 + cantidad_izquierda + cantidad_derecha
    
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


