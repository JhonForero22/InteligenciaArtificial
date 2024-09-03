# Importar los juegos Sudokus desde el archivo 'JuegoSudoku'
from JuegoSudoku import sudoku_facil_1, sudoku_medio_1, sudoku_dificil_1

# Importar la librería de tiempo para medir el rendimiento
import time

# Función para imprimir un Sudoku con formato
def imprimir_sudoku(sudoku):
    for i, fila in enumerate(sudoku):
        # Agrega una línea horizontal cada 3 filas
        if i % 3 == 0 and i != 0:
            print("-" * 21)
        fila_con_separadores = ""
        for j, num in enumerate(fila):
            # Agrega una línea vertical cada 3 columnas
            if j % 3 == 0 and j != 0:
                fila_con_separadores += " | "
            # Añade el número o "0" en lugar de celdas vacías
            fila_con_separadores += str(num) if num != 0 else "0"
            # Agrega un espacio entre números, excepto después del último número de cada fila
            if j != len(fila) - 1:
                fila_con_separadores += " "
        # Imprime la fila formateada
        print(fila_con_separadores)

# Implementación del solucionador de Sudoku con Backtracking
def es_valido(sudoku, num, fila, col):
    # Verificar si el número ya está en la fila
    if num in sudoku[fila]:
        return False
    
    # Verificar si el número ya está en la columna
    for i in range(9):
        if sudoku[i][col] == num:
            return False
    
    # Verificar si el número ya está en la subcuadrícula 3x3
    inicio_fila = fila - fila % 3
    inicio_col = col - col % 3
    for i in range(3):
        for j in range(3):
            if sudoku[inicio_fila + i][inicio_col + j] == num:
                return False
    
    return True

def resolver_sudoku(sudoku):
    # Recorre cada celda del Sudoku
    for fila in range(9):
        for col in range(9):
            if sudoku[fila][col] == 0:  # Encontrar una celda vacía
                # Probar números del 1 al 9 en la celda vacía
                for num in range(1, 10):
                    if es_valido(sudoku, num, fila, col):
                        sudoku[fila][col] = num
                        if resolver_sudoku(sudoku):
                            return True
                        sudoku[fila][col] = 0  # Deshacer movimiento (backtrack)
                return False  # Si ningún número es válido, retroceder
    return True  # Si no quedan espacios vacíos, el Sudoku está resuelto

# Implementación optimizada con la heurística MRV (Minimum Remaining Values)
def encontrar_celda_con_menos_posibilidades(sudoku):
    min_posibilidades = 10  # Más que el número máximo de posibilidades (1-9)
    mejor_celda = None
    
    for fila in range(9):
        for col in range(9):
            if sudoku[fila][col] == 0:
                num_posibilidades = 0
                # Contar el número de posibilidades para la celda vacía
                for num in range(1, 10):
                    if es_valido(sudoku, num, fila, col):
                        num_posibilidades += 1
                # Encontrar la celda con menos posibilidades
                if num_posibilidades < min_posibilidades:
                    min_posibilidades = num_posibilidades
                    mejor_celda = (fila, col)
    
    return mejor_celda

def resolver_sudoku_opt(sudoku):
    # Encuentra la celda con menos posibilidades
    celda = encontrar_celda_con_menos_posibilidades(sudoku)
    if not celda:  # Si no hay celdas vacías, el Sudoku está resuelto
        return True
    
    fila, col = celda
    
    for num in range(1, 10):
        if es_valido(sudoku, num, fila, col):
            sudoku[fila][col] = num
            if resolver_sudoku_opt(sudoku):
                return True
            sudoku[fila][col] = 0  # Deshacer movimiento (backtrack)
    
    return False  # Si ningún número es válido, retroceder

# Función para medir el rendimiento del algoritmo de resolución de Sudoku
def medir_rendimiento(sudoku, metodo):
    inicio = time.time()  # Registrar el tiempo de inicio
    if metodo == "básico":
        resolver_sudoku(sudoku)  # Usar el método básico de resolución
    elif metodo == "optimizado":
        resolver_sudoku_opt(sudoku)  # Usar el método optimizado con MRV
    fin = time.time()  # Registrar el tiempo de finalización
    duracion = fin - inicio  # Calcular la duración
    imprimir_sudoku(sudoku)  # Imprimir el Sudoku resuelto
    print(f"Tiempo tomado: {duracion:.6f} segundos\n")  # Mostrar el tiempo tomado

# Imprimir el Sudoku original y resultados
print("     Sudoku Original")
imprimir_sudoku(sudoku_facil_1)  # Imprimir el Sudoku inicial
print()
print("     Resultados metodo basico:")
medir_rendimiento(sudoku_facil_1, "básico")  # Resolver y medir el rendimiento con el método básico
print("     Resultados metodo optimizado:")
medir_rendimiento(sudoku_facil_1, "optimizado")  # Resolver y medir el rendimiento con el método optimizado

"""
Explicación
Importación de módulos y funciones:

Se importan los Sudokus desde un archivo externo llamado JuegoSudoku.
Se importa la librería time para medir el rendimiento de los algoritmos.
Función imprimir_sudoku:

Imprime el Sudoku con un formato agradable, añadiendo líneas horizontales y verticales cada 3 filas y 3 columnas para mejorar la legibilidad.
Función es_valido:

Verifica si un número puede colocarse en una celda sin violar las reglas del Sudoku (no repetir números en la fila, columna y subcuadrícula 3x3).
Función resolver_sudoku:

Resuelve el Sudoku usando el algoritmo de backtracking básico. Intenta colocar números en celdas vacías y retrocede si encuentra un conflicto.
Función encontrar_celda_con_menos_posibilidades:

Encuentra la celda vacía con el menor número de posibilidades para aplicar la heurística MRV, lo que ayuda a optimizar la resolución del Sudoku.
Función resolver_sudoku_opt:

Utiliza la heurística MRV para resolver el Sudoku de manera más eficiente al elegir la celda con menos posibilidades.
Función medir_rendimiento:

Mide el tiempo que tarda en resolver el Sudoku usando el método seleccionado (básico u optimizado) e imprime el Sudoku resuelto junto con el tiempo tomado.
Bloque principal:

Imprime el Sudoku original.
Resuelve el Sudoku usando ambos métodos (básico y optimizado) y mide el tiempo que toma cada método.
"""