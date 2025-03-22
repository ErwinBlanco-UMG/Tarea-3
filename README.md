Erwin Fernando Blanco Melendres 9490-23-7748
Sara Abigail Solis Ixquiactap 94902312295

1. Arbol de Busqueda Binaria (ABB)
Este proyecto implementa un árbol de búsqueda en Python, permitiendo la inserción, eliminación, Carga de archivos .txt y .csv, visualización en representación gráfica de los nodos.

2. Como funciona
Clase 1: Representa cada nodo con un valor y referencias a sus hijos izquierdo y derecho.
Clase 2 abb: Inserta un nuevo valor respetando las reglas del ABB: Inserta numeros, te indica si el número está en el arbol,Borra un número y reacomoda el árbol
Lee un archivo y carga números, Genera una imagen del árbol
Ejemplo: ![image](https://github.com/user-attachments/assets/cad36b06-5631-4e62-808b-69f0cd13f760)


2. Instalar dependencias
Instala la librería Graphviz con pip install graphviz
Instala la librería csv
Instala la librería os



3. Detalles de la ejecución del código completo.
La clase nodoA inicializa punteros y un valor
La Clase ABB inicializa una raiz de un nuevo arbol
Def insertar, agrega un nuevo valor inicial (raiz al nuevo arbol como base)
Def agregar busca si tiene un valor inicial y si ya tiene los compara y si es mayor lo envia a la derecha si es menor a la izquierda
Def buscador, busca el nodo que uno desea
Def elimina, elimina el nodo que uno desea
Del eliminar, elimina el nodo ya sea donde se encuentre ubicado y rehace el arbol
Def minimo, encuentra el minimo del arbol derecho o nodo con un solo hijo o sin hijos
Def borrar arbol, elimina el arbol completo
Pinta una nueva grafica sobre el arbol que esta creando
El def generar, genera un nuevo nodo
El def cargar_archivo, carga un archivo ya sea txt o CSV y lo agrega al arbol existente
Menú de opciones
Insertar nodo:
Opcion 1: Ingresa un número para insertarlo en el árbol.
* Buscar nodo:
Opcion 2: Ingresa un número y se indica si está presente.
* Eliminar nodo:
Opcion 3: Ingresa un número para eliminarlo del árbol.
 * Eliminar todo el árbol:
Opcion 4: Borra todos los nodos del árbol.
* Cargar desde archivo:
Opcion 5: Ingresa la ruta de un archivo .txt o .csv con números.
Los datos se cargan automáticamente al árbol.
Se ignoran valores no numéricos.
* Visualizar árbol:
Opcion 6: Genera una imagen output/arbol.png representando el árbol.
* Salir:
Opcion 7: Finaliza la ejecución del programa.

4. Documentación Extra
El código fuente está comentado para facilitar su comprensión.

