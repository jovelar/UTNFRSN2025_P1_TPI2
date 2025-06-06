from arbol import ArbolBinario
from Persona import Persona

def menu():
    while True:
        print("1- Agregar una persona")
        print("2- Mostrar Arbol de Apellidos y Lista de Personas")
        print("3- Editar una persona")
        print("4- Borrar persona")
        print("5- Salir")
        
        try:
            opcion=int(input("Ingrese un numero: "))
        except ValueError:
            print("Opcion invalida")
            continue
        else:
            break
    return opcion

def main():
    opcion=0

    arbol=ArbolBinario()

    while opcion!=5:
        print(f"nodos: {arbol.contarNodos(arbol.raiz)}")
        opcion=menu()
        
        match(opcion):
            case 1:
                apellido=input("Ingrese un apellido: ")
                nombre=input("Ingrese un nombre: ")
                dni=input("Ingrese un DNI: ")

                nuevaPersona=Persona(apellido,nombre,dni)
                arbol.agregarPersona(nuevaPersona)
                
            case 2:
                arbol.mostrar()
                pass
            case 3:
                pass
            case 4:
                arbol.borrarPersona(arbol.raiz)
                pass
            case 5:
                break
            case _:
                print("Opcion invaida")
                pass

main()