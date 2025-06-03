from arbol import ArbolBinario
from Persona import Persona

def menu():
    while True:
        print("1- Agregar una persona")
        print("2- Mostrar una persona")
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
        opcion=menu()
        match(opcion):

            case 1:
                apellido=input("Ingrese un apellido: ")
                nombre=input("Ingrese un nombre: ")
                dni=input("Ingrese un DNI: ")

                nuevaPersona=Persona(apellido,nombre,dni)
                arbol=ArbolBinario.agregarPersona(arbol,nuevaPersona)

                break
            case 2:
                break
            case 3:
                break
            case 4:
                break
            case 5:
                break
            case _:
                print("Opcion invaida")
                break


main()