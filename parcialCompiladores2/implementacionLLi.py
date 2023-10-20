import pandas as pd

from graphviz import Digraph

# Definicion de la clase NodoPila
class NodoPila:
    def __init__(self, simbolo, lexema):
        global contador
        self.simbolo = simbolo
        self.lexema = lexema
        self.id = contador + 1
        contador += 1

# Definicion de la clase NodoArbol
class NodoArbol:
    def __init__(self, id, simbolo, lexema):
        self.id = id
        self.simbolo = simbolo
        self.lexema = lexema
        self.hijos = []
        self.padre = None

    def agregar_hijo(self, hijo):
        self.hijos.append(hijo)
        hijo.padre = self

# Funcion para buscar un nodo en el arbol
def buscar_nodo(id, nodo):
    if nodo.id == id:
        return nodo
    else:
        for hijo in nodo.hijos:
            resultado = buscar_nodo(id, hijo)
            if resultado is not None:
                return resultado
        return None
    
# Funcion para realizar un recorrido en orden (inorden) e imprimir solo el simbolo
def recorrido_inorden(nodo):
    if nodo is not None:
        for hijo in nodo.hijos:
            recorrido_inorden(hijo)  # Hijo izquierdo
        # Imprimir solo el simbolo del nodo
        print(nodo.simbolo)

def imprimir_arbol(nodo, dot=None, nivel=0):
    if dot is None:
        dot = Digraph(comment='Arbol de Derivacion')

    # Incluir el lexema además del símbolo en el nodo
    nodo_label = f"{nodo.simbolo} ({nodo.lexema})" if nodo.lexema is not None else nodo.simbolo

    # Configurar estilo y color de relleno para el nodo
    dot.node(str(nodo.id), nodo_label, style='filled', fillcolor='aqua')

    for hijo in reversed(nodo.hijos):
        # Configurar color del borde de la arista y hacer que apunte desde el nodo padre al nodo hijo
        dot.edge(str(nodo.id), str(hijo.id), color='yellow')

    for hijo in reversed(nodo.hijos):
        imprimir_arbol(hijo, dot, nivel + 1)

    return dot

# Cargar la tabla y configurar la pila inicial
tabla = pd.read_csv("parcialCompiladores/final3.csv", index_col=0)
contador = 0
pila = []

# Inicializar la pila con simbolos de inicio y fin
simbolo_E = NodoPila('INICIO_CODIGO', None)
simbolo_dolar = NodoPila('$', None)
pila.append(simbolo_dolar)
pila.append(simbolo_E)

# Configurar el arbol con el simbolo de inicio
raiz = NodoArbol(simbolo_E.id, simbolo_E.simbolo, simbolo_E.lexema)

# Definir la entrada
entrada = [
    {"simbolo": "FUNCION", "lexema": "resta_numeros", "nroline": 1, "col": 1},
    {"simbolo": "IDENTIFICADOR", "lexema": "IDENTIFICADOR", "nroline": 1, "col": 9},
    {"simbolo": "PARENTESIS_ABRE", "lexema": "PARENTESIS_ABRE", "nroline": 1, "col": 21},
    {"simbolo": "DATO_ENTERO", "lexema": "DATO_ENTERO", "nroline": 1, "col": 36},
    {"simbolo": "IDENTIFICADOR", "lexema": "IDENTIFICADOR", "nroline": 1, "col": 48},
    {"simbolo": "COMA", "lexema": "COMA", "nroline": 1, "col": 60},
    {"simbolo": "DATO_ENTERO", "lexema": "DATO_ENTERO", "nroline": 1, "col": 65},
    {"simbolo": "IDENTIFICADOR", "lexema": "IDENTIFICADOR", "nroline": 1, "col": 77},
    {"simbolo": "PARENTESIS_CIERRA", "lexema": "PARENTESIS_CIERRA", "nroline": 1, "col": 89},
    {"simbolo": "LLAVE_ABRE", "lexema": "LLAVE_ABRE", "nroline": 1, "col": 101},
    {"simbolo": "DATO_ENTERO", "lexema": "DATO_ENTERO", "nroline": 1, "col": 113},
    {"simbolo": "IDENTIFICADOR", "lexema": "IDENTIFICADOR", "nroline": 1, "col": 125},
    {"simbolo": "IGUALDAD", "lexema": "IGUALDAD", "nroline": 1, "col": 137},
    {"simbolo": "NUM_ENTERO", "lexema": "NUM_ENTERO", "nroline": 1, "col": 148},
    {"simbolo": "OP_SUMA", "lexema": "OP_SUMA", "nroline": 1, "col": 159},
    {"simbolo": "NUM_ENTERO", "lexema": "NUM_ENTERO", "nroline": 1, "col": 166},
    {"simbolo": "IMPRESOR", "lexema": "IMPRESOR", "nroline": 1, "col": 177},
    {"simbolo": "IDENTIFICADOR", "lexema": "IDENTIFICADOR", "nroline": 1, "col": 188},
    {"simbolo": "LLAVE_CIERRA", "lexema": "LLAVE_CIERRA", "nroline": 1, "col": 200},
    {"simbolo": "INICIO_PROCESO", "lexema": "INICIO_PROCESO", "nroline": 1, "col": 212},
    {"simbolo": "LLAVE_ABRE", "lexema": "LLAVE_ABRE", "nroline": 1, "col": 225},
    {"simbolo": "DATO_ENTERO", "lexema": "DATO_ENTERO", "nroline": 1, "col": 237},
    {"simbolo": "IDENTIFICADOR", "lexema": "IDENTIFICADOR", "nroline": 1, "col": 249},
    {"simbolo": "IGUALDAD", "lexema": "IGUALDAD", "nroline": 1, "col": 261},
    {"simbolo": "NUM_ENTERO", "lexema": "NUM_ENTERO", "nroline": 1, "col": 273},
    {"simbolo": "DATO_ENTERO", "lexema": "DATO_ENTERO", "nroline": 1, "col": 284},
    {"simbolo": "IDENTIFICADOR", "lexema": "IDENTIFICADOR", "nroline": 1, "col": 296},
    {"simbolo": "IGUALDAD", "lexema": "IGUALDAD", "nroline": 1, "col": 308},
    {"simbolo": "NUM_ENTERO", "lexema": "NUM_ENTERO", "nroline": 1, "col": 320},
    {"simbolo": "PARENTESIS_ABRE", "lexema": "PARENTESIS_ABRE", "nroline": 1, "col": 332},
    {"simbolo": "DATO_ENTERO", "lexema": "DATO_ENTERO", "nroline": 1, "col": 347},
    {"simbolo": "IDENTIFICADOR", "lexema": "IDENTIFICADOR", "nroline": 1, "col": 359},
    {"simbolo": "COMA", "lexema": "COMA", "nroline": 1, "col": 371},
    {"simbolo": "DATO_ENTERO", "lexema": "DATO_ENTERO", "nroline": 1, "col": 376},
    {"simbolo": "IDENTIFICADOR", "lexema": "IDENTIFICADOR", "nroline": 1, "col": 388},
    {"simbolo": "PARENTESIS_CIERRA", "lexema": "PARENTESIS_CIERRA", "nroline": 1, "col": 400},
    {"simbolo": "LLAVE_CIERRA", "lexema": "LLAVE_CIERRA", "nroline": 1, "col": 412},
    {"simbolo": "FIN_PROCESO", "lexema": "FIN_PROCESO", "nroline": 1, "col": 424},
    {"simbolo": "$", "lexema": "$", "nroline": 0, "col": 0},
]


index_entrada = 0

# Analizar la entrada
while len(pila) > 0:
    simbolo_entrada = entrada[index_entrada]["simbolo"]

    # Verificar si el símbolo de entrada es válido
    if simbolo_entrada not in tabla.columns:
        print("1 Error en el proceso sintactico")
        break

    # Comparar la cima de la pila con el simbolo de entrada
    if pila[-1].simbolo == simbolo_entrada:
        pila.pop()
        index_entrada += 1
    else:
         # Obtener la produccion de la tabla de analisis
        produccion = tabla.loc[pila[-1].simbolo, simbolo_entrada]

        # Manejar errores de sintaxis
        if isinstance(produccion, float):
            print("2 Error en el proceso sintactico")
            break

        # Aplicar la produccion en la pila y el arbol
        if produccion != ('e'):
            padre = buscar_nodo(pila[-1].id, raiz)
            pila.pop()
            for simbolo in reversed(str(produccion).split()):
                nodo_p = NodoPila(simbolo, entrada[index_entrada]["lexema"]
)
                pila.append(nodo_p)
                hijo = NodoArbol(nodo_p.id, nodo_p.simbolo, nodo_p.lexema)
                padre.agregar_hijo(hijo)
        else:
            pila.pop()



# Check the result of the analysis
if len(pila) == 0:
    print("Proceso ejecutado correctamente")
else:
    print("Error en el proceso sintactico: pila no vacia al finalizar")

# Print and visualize the tree
dot = imprimir_arbol(raiz)
dot.render('arbol', format='png', cleanup=True)
print("Arbol de derivacion generado y guardado como 'arbol.png'.")


# Llamar a la funcion para realizar el recorrido en orden
#recorrido_inorden(raiz)


# Estructura de la tabla de simbolos
tabla_de_simbolos = []

# Funcion para registrar funciones en la tabla de símbolos
def registrar_funciones(nodo):
    if nodo is not None and nodo.simbolo == "FUNCION":
        # Verificar si el nodo tiene al menos tres hijos
            tipo_dato = "void"  # Obtener el ultimo hijo como el tipo de dato
            nombre_funcion = nodo.lexema  # Obtener el segundo hijo como el nombre de la funcion
            ambito = "global"
            codigo_flag = "FUNC"
            tabla_de_simbolos.append({
                "tipo_dato": tipo_dato,
                "nombre_funcion": nombre_funcion,
                "ambito": ambito,
                "codigo_flag": codigo_flag
            })

    for hijo in nodo.hijos:
        registrar_funciones(hijo)

# Llamada a la funcion para registrar funciones
registrar_funciones(raiz)

# Imprimir la tabla de simbolos
print("Tabla de Símbolos:")
for simbolo in tabla_de_simbolos:
    print(simbolo)


