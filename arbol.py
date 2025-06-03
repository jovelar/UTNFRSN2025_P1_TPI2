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
        if self.raiz==None:
            self.raiz=Nodo(apellido)
        else:
            self.insertarRecursivo(self.raiz,apellido)
    
    def mostrar(self):
        if self.raiz==None:
            print("Lista vacia!")
        else:
            self.mostrarInorderRec(self.raiz)
    #Inserta de forma recursiva.
    
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

    def mostrarInorderRec(self,nodo):
        if nodo.izquierda!=None:
            self.mostrarInorderRec(nodo.izquierda)
        print(nodo.dato)
        listado=nodo.arreglo
        if nodo.derecha!=None:
            self.mostrarInorderRec(nodo.derecha)
    
    def buscarNodoRec(self,nodo,apellido):
        _#posicion=None
        if nodo.apellido==apellido:
            posicion=nodo
        elif apellido < nodo.apellido:
            self.buscarNodoRec(nodo.izquierda,apellido)
        else:
            self.buscarNodoRec(nodo.derecha,apellido)
        return posicion
    
    def agregarPersona(self,persona):
        posicion=self.buscarNodoRec(self.raiz,persona.apellido)

        if posicion==None:
            self.insertarRecursivo(nodo,persona.apellido)

