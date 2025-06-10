"""
Representación de Fixtures Deportivos como Árboles Binarios
Implementación usando listas anidadas en Python

Autores: Luciano José Cartagena, Santiago Arroquigaray
Materia: Programación I
Fecha: Junio 2025
"""

def crear_partido(nombre):
    """
    Crea un nuevo nodo que representa un partido.

    Args:
        nombre (str): Nombre descriptivo del partido

    Returns:
        list: Lista de 3 elementos [nombre, hijo_izq, hijo_der]

    Complejidad: O(1) tiempo, O(1) espacio
    """
    return [nombre, [], []]

def asignar_subpartidos(nodo, izq, der):
    """
    Asigna los partidos previos (hijos) a un partido dado.

    Args:
        nodo (list): Nodo padre (partido actual)
        izq (list): Subpartido izquierdo
        der (list): Subpartido derecho

    Complejidad: O(1) tiempo, O(1) espacio
    """
    nodo[1] = izq  # Hijo izquierdo
    nodo[2] = der  # Hijo derecho

def imprimir_fixture(arbol, nivel=0, prefijo=""):
    """
    Imprime el fixture de forma visual (rotado 90°).
    Utiliza recursión para recorrer el árbol.

    Args:
        arbol (list): Nodo raíz del árbol
        nivel (int): Nivel actual de profundidad
        prefijo (str): Prefijo para la visualización

    Complejidad: O(n) tiempo, O(h) espacio (por la pila de recursión)
    donde n = número de nodos, h = altura del árbol
    """
    if arbol:  # Caso base: si el nodo existe
        # Recorrer primero el subárbol derecho (se imprime arriba)
        imprimir_fixture(arbol[2], nivel + 1, "┌── ")

        # Imprimir el nodo actual con indentación
        indentacion = "    " * nivel
        print(f"{indentacion}{prefijo}{arbol[0]}")

        # Recorrer el subárbol izquierdo (se imprime abajo)
        imprimir_fixture(arbol[1], nivel + 1, "└── ")

def avanzar_ganador(arbol, ganador):
    """
    Actualiza un partido con su ganador.

    Args:
        arbol (list): Nodo del partido
        ganador (str): Nombre del equipo ganador

    Complejidad: O(1) tiempo, O(1) espacio
    """
    arbol[0] = f"{arbol[0]} → Ganador: {ganador}"

def recorrido_preorden(arbol, resultado=None):
    """
    Realiza recorrido preorden del árbol (Raíz → Izq → Der).

    Args:
        arbol (list): Nodo raíz
        resultado (list): Lista para almacenar el recorrido

    Returns:
        list: Lista con los nodos en orden preorden

    Complejidad: O(n) tiempo, O(n) espacio
    """
    if resultado is None:
        resultado = []

    if arbol:
        resultado.append(arbol[0])      # Visitar raíz
        recorrido_preorden(arbol[1], resultado)  # Subárbol izquierdo
        recorrido_preorden(arbol[2], resultado)  # Subárbol derecho

    return resultado

def recorrido_inorden(arbol, resultado=None):
    """
    Realiza recorrido inorden del árbol (Izq → Raíz → Der).

    Args:
        arbol (list): Nodo raíz
        resultado (list): Lista para almacenar el recorrido

    Returns:
        list: Lista con los nodos en orden inorden

    Complejidad: O(n) tiempo, O(n) espacio
    """
    if resultado is None:
        resultado = []

    if arbol:
        recorrido_inorden(arbol[1], resultado)   # Subárbol izquierdo
        resultado.append(arbol[0])               # Visitar raíz
        recorrido_inorden(arbol[2], resultado)   # Subárbol derecho

    return resultado

def recorrido_postorden(arbol, resultado=None):
    """
    Realiza recorrido postorden del árbol (Izq → Der → Raíz).

    Args:
        arbol (list): Nodo raíz
        resultado (list): Lista para almacenar el recorrido

    Returns:
        list: Lista con los nodos en orden postorden

    Complejidad: O(n) tiempo, O(n) espacio
    """
    if resultado is None:
        resultado = []

    if arbol:
        recorrido_postorden(arbol[1], resultado)  # Subárbol izquierdo
        recorrido_postorden(arbol[2], resultado)  # Subárbol derecho
        resultado.append(arbol[0])                # Visitar raíz

    return resultado

def obtener_altura(arbol):
    """
    Calcula la altura del árbol.

    Args:
        arbol (list): Nodo raíz

    Returns:
        int: Altura del árbol (0 para árbol vacío)

    Complejidad: O(n) tiempo, O(h) espacio
    """
    if not arbol:
        return 0

    altura_izq = obtener_altura(arbol[1])
    altura_der = obtener_altura(arbol[2])

    return 1 + max(altura_izq, altura_der)

def contar_nodos(arbol):
    """
    Cuenta el número total de nodos en el árbol.

    Args:
        arbol (list): Nodo raíz

    Returns:
        int: Número total de nodos

    Complejidad: O(n) tiempo, O(h) espacio
    """
    if not arbol:
        return 0

    return 1 + contar_nodos(arbol[1]) + contar_nodos(arbol[2])

def buscar_partido(arbol, nombre_partido):
    """
    Busca un partido específico en el árbol.

    Args:
        arbol (list): Nodo raíz
        nombre_partido (str): Nombre del partido a buscar

    Returns:
        list or None: Nodo del partido si se encuentra, None si no existe

    Complejidad: O(n) tiempo, O(h) espacio
    """
    if not arbol:
        return None

    if nombre_partido in arbol[0]:
        return arbol

    # Buscar en subárbol izquierdo
    resultado_izq = buscar_partido(arbol[1], nombre_partido)
    if resultado_izq:
        return resultado_izq

    # Buscar en subárbol derecho
    return buscar_partido(arbol[2], nombre_partido)

# =====================================================
# PROGRAMA PRINCIPAL - DEMOSTRACIÓN
# =====================================================

def main():
    """
    Función principal que demuestra el uso del sistema.
    """
    print("=" * 60)
    print("SISTEMA DE FIXTURES DEPORTIVOS CON ÁRBOLES BINARIOS")
    print("=" * 60)

    # Crear partidos de cuartos de final
    cuartos1 = crear_partido("Cuartos 1: Argentina vs Brasil")
    cuartos2 = crear_partido("Cuartos 2: España vs Francia") 
    cuartos3 = crear_partido("Cuartos 3: Alemania vs Italia")
    cuartos4 = crear_partido("Cuartos 4: Inglaterra vs Portugal")

    # Crear semifinales
    semi1 = crear_partido("Semifinal 1")
    semi2 = crear_partido("Semifinal 2")

    # Conectar cuartos con semifinales
    asignar_subpartidos(semi1, cuartos1, cuartos2)
    asignar_subpartidos(semi2, cuartos3, cuartos4)

    # Crear final
    final = crear_partido("FINAL DEL TORNEO")
    asignar_subpartidos(final, semi1, semi2)

    # Mostrar fixture inicial
    print("\n🏆 FIXTURE INICIAL DEL TORNEO:")
    print("-" * 40)
    imprimir_fixture(final)

    # Estadísticas del árbol
    print(f"\n📊 ESTADÍSTICAS:")
    print(f"   • Altura del árbol: {obtener_altura(final)}")
    print(f"   • Total de partidos: {contar_nodos(final)}")

    # Simular resultados
    print("\n⚽ SIMULANDO RESULTADOS...")
    avanzar_ganador(cuartos1, "Argentina")
    avanzar_ganador(cuartos2, "España")
    avanzar_ganador(cuartos3, "Alemania") 
    avanzar_ganador(cuartos4, "Inglaterra")

    avanzar_ganador(semi1, "Argentina")
    avanzar_ganador(semi2, "Alemania")

    avanzar_ganador(final, "Argentina")

    # Mostrar fixture final
    print("\n🏆 FIXTURE CON RESULTADOS:")
    print("-" * 40)
    imprimir_fixture(final)

    # Mostrar recorridos
    print(f"\n🔄 RECORRIDOS DEL ÁRBOL:")
    print("-" * 30)

    recorrido_pre = recorrido_preorden(final)
    print("\n📋 Preorden (Raíz → Izq → Der):")
    for i, partido in enumerate(recorrido_pre, 1):
        print(f"   {i}. {partido}")

    recorrido_in = recorrido_inorden(final)
    print("\n📋 Inorden (Izq → Raíz → Der):")
    for i, partido in enumerate(recorrido_in, 1):
        print(f"   {i}. {partido}")

    recorrido_post = recorrido_postorden(final)
    print("\n📋 Postorden (Izq → Der → Raíz):")
    for i, partido in enumerate(recorrido_post, 1):
        print(f"   {i}. {partido}")

    # Demostrar búsqueda
    print("\n🔍 BÚSQUEDA DE PARTIDOS:")
    print("-" * 25)
    partido_buscado = buscar_partido(final, "Semifinal 1")
    if partido_buscado:
        print(f"✅ Encontrado: {partido_buscado[0]}")
    else:
        print("❌ Partido no encontrado")

def ejemplo_torneo_simple():
    """
    Ejemplo adicional con un torneo más simple de 4 equipos.
    """
    print("\n" + "=" * 50)
    print("EJEMPLO: TORNEO SIMPLE DE 4 EQUIPOS")
    print("=" * 50)

    # Crear semifinales
    semi1 = crear_partido("Semifinal A: Real Madrid vs Barcelona")
    semi2 = crear_partido("Semifinal B: Liverpool vs Manchester City")

    # Crear final
    final_simple = crear_partido("FINAL")
    asignar_subpartidos(final_simple, semi1, semi2)

    print("\n🏆 FIXTURE INICIAL:")
    imprimir_fixture(final_simple)

    # Simular
    avanzar_ganador(semi1, "Real Madrid")
    avanzar_ganador(semi2, "Liverpool")
    avanzar_ganador(final_simple, "Real Madrid")

    print("\n🏆 RESULTADO FINAL:")
    imprimir_fixture(final_simple)

if __name__ == "__main__":
    main()
    ejemplo_torneo_simple()
