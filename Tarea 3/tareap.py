import os
import csv
from graphviz import Digraph
#la clase nodoA inicializa punteros y un valor
class nodoA:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None
#La Clase ABB inicializa una raiz de un nuevo arbol
class ABB:
    #inicializa la clase
    def __init__(self):
        self.raiz = None
    #def insertar, agrega un nuevo valor inicial (raiz al nuevo arbol como base)
    def insertar(self, valor):
        self.raiz = self.agregar(self.raiz, valor)
    #def agregar busca si tiene un valor inicial y si ya tiene los compara y si es mayor lo envia a la derecha si es menor a la izquierda
    def agregar(self, nodo, valor):
        if nodo is None:
            return nodoA(valor)
        if valor < nodo.valor:
            nodo.izquierda = self.agregar(nodo.izquierda, valor)
        else:
            nodo.derecha = self.agregar(nodo.derecha, valor)
        return nodo
    # def buscador, busca el nodo que uno desea
    def buscador(self, nodo, valor):
        if nodo is None or nodo.valor == valor:
            return nodo
        if nodo.valor < valor:
            return self.buscador(nodo.derecha, valor)
        elif nodo.valor > valor:
            return self.buscador(nodo.izquierda, valor)
    #def elimina, elimina el nodo que uno desea
    def elimina(self, valor):
        self.raiz = self._eliminar(self.raiz, valor)
    #del eliminar, elimina el nodo ya sea donde se encuentre ubicado y rehace el arbol
    def _eliminar(self, nodo, valor):
        if nodo is None:
            return nodo
        if nodo.valor < valor:
            nodo.derecha = self._eliminar(nodo.derecha, valor)
        elif nodo.valor > valor:
            nodo.izquierda = self._eliminar(nodo.izquierda, valor)
        else:
            if nodo.izquierda is None:
                return nodo.derecha
            elif nodo.derecha is None:
                return nodo.izquierda
            sucesor = self._minimo(nodo.derecha)
            nodo.valor = sucesor.valor
            nodo.derecha = self._eliminar(nodo.derecha, sucesor.valor)
        return nodo
    #def minimo, encuentra el minimo del arbol derecho o nodo con un solo hijo o sin hijos
    def _minimo(self, nodo):
        actual = nodo
        while actual.izquierda is not None:
            actual = actual.izquierda
        return actual
    #def borrar arbol, elimina el arbol completo
    def borrar_arbol(self):
        self.raiz = None
        print("SE ELIMINO EL ARBOLITO/anterior de registros :)")
    #pinta una nueva grafica sobre el arbol que esta creando
    def visualizar(self, nodo, nombre="arbol"):
        if nodo is None:
            print("El árbol está vacío. No se puede generar la imagen.")
            return

        os.makedirs("output", exist_ok=True)
        dot = Digraph()
        self._generar(dot, nodo)

        ruta_png = f"output/{nombre}"
        dot.render(ruta_png, format="png", cleanup=True)
        print(f"Imagen PNG generada: {ruta_png}.png")
    #El def generar, genera un nuevo nodo
    def _generar(self, dot, nodo):
        if nodo:
            dot.node(str(nodo.valor))
            if nodo.izquierda:
                dot.edge(str(nodo.valor), str(nodo.izquierda.valor))
                self._generar(dot, nodo.izquierda)
            if nodo.derecha:
                dot.edge(str(nodo.valor), str(nodo.derecha.valor))
                self._generar(dot, nodo.derecha)
    #El def cargar_archivo, carga un archivo ya sea txt o CSV y lo agrega al arbol existente
    def cargar_archivo(self):
        try:
            ruta = input("Ingrese la ruta del archivo .txt o .csv: ")
            with open(ruta, 'r', encoding='utf-8') as archivo:
                lector = csv.reader(archivo)
                for fila in lector:
                    for valor_str in fila:
                        valor_str = valor_str.strip()
                        if valor_str.isdigit():
                            valor = int(valor_str)
                            self.insertar(valor)
                        else:
                            print(f"Ignorado valor no numérico: {valor_str}")

            print("Datos cargados correctamente al árbol.")
        except FileNotFoundError:
            print("Archivo no encontrado, verifíquelo.")
        except ValueError:
            print("Error al convertir datos. El archivo debe contener solo números.")
        except Exception as e:
            print(f"Error inesperado: {e}")

def menu():
    arbol = ABB()

    while True:
        print("\n*** MENU PRINCIPAL *****")
        print("1. Agregar")
        print("2. Buscar")
        print("3. Eliminar nodo")
        print("4. Eliminar todo el arbol")
        print("5. Cargar desde archivo (.txt o .csv)")
        print("6. Mostrar Graphviz")
        print("7. SALIR")
#La opcion 1 agrega un nuevo nodo al arbol existente y lo coloca segun la validación si es mayor o menor
#La opción 2 recorre el arbol y busca el nodo que necesitamos
#La opción 3 elimina el nodo que ya no es necesario, para ello recorre el arbol y realiza la busqueda
#La opción 4 elimina todo el arbol desde la raiz
#La opción 5 realiza la carga de archivo desde un archivo existente ya sea txt o CSV y extrae todos los numeros y los agrega al arbol existente
#La opción 6 Genera la grafica por medio de la libreria Graphviz
#La opción 7 nos finaliza el programa
        try:
            opcion = input("SELECCIONE UNA OPCIÓN: ")

            if opcion == "1":
                valor = int(input("Ingrese un número a insertar: "))
                arbol.insertar(valor)
                print("NUMERO INSERTADO")

            elif opcion == "2":
                valor = int(input("Ingrese un número a buscar: "))
                nodo_encontrado = arbol.buscador(arbol.raiz, valor)
                if nodo_encontrado:
                    print(f" NUMERO {valor} ENCONTRADO EN EL ARBOL")
                else:
                    print(f"NUMERO {valor} NO ENCONTRADO")

            elif opcion == "3":
                valor = int(input("INGRESE EL NUMERO A ELIMINAR: "))
                arbol.elimina(valor)
                print(f"El numero {valor} ha sido eliminado.")

            elif opcion == "4":
                arbol.borrar_arbol()

            elif opcion == "5":
                arbol.cargar_archivo()

            elif opcion == "6":
                arbol.visualizar(arbol.raiz)

            elif opcion == "7":
                print("SALIENDO DEL PROGRAMA, DOEI")
                break

            else:
                print("Opcion no valida, intentalo de nuevo")
        except ValueError:
            print("ERROR: Ingresaste un valor inválido.")
        except Exception as e:
            print(f"Error inesperado: {e}")

menu()
