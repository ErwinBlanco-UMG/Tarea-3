import os
import csv
from graphviz import Digraph

class nodoA:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None

class ABB:
    def __init__(self):
        self.raiz = None

    def insertar(self, valor):
        self.raiz = self.agregar(self.raiz, valor)

    def agregar(self, nodo, valor):
        if nodo is None:
            return nodoA(valor)
        if valor < nodo.valor:
            nodo.izquierda = self.agregar(nodo.izquierda, valor)
        else:
            nodo.derecha = self.agregar(nodo.derecha, valor)
        return nodo

    def buscador(self, nodo, valor):
        if nodo is None or nodo.valor == valor:
            return nodo
        if nodo.valor < valor:
            return self.buscador(nodo.derecha, valor)
        elif nodo.valor > valor:
            return self.buscador(nodo.izquierda, valor)

    def elimina(self, valor):
        self.raiz = self._eliminar(self.raiz, valor)

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

    def _minimo(self, nodo):
        actual = nodo
        while actual.izquierda is not None:
            actual = actual.izquierda
        return actual

    def borrar_arbol(self):
        self.raiz = None
        print("SE ELIMINO EL ARBOLITO/anterior de registros :)")

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

    def _generar(self, dot, nodo):
        if nodo:
            dot.node(str(nodo.valor))
            if nodo.izquierda:
                dot.edge(str(nodo.valor), str(nodo.izquierda.valor))
                self._generar(dot, nodo.izquierda)
            if nodo.derecha:
                dot.edge(str(nodo.valor), str(nodo.derecha.valor))
                self._generar(dot, nodo.derecha)

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