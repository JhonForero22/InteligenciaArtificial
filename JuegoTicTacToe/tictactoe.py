from copy import deepcopy

X = "X"
O = "O"
EMPTY = None

def initial_state():
    """
    Retorna el estado inicial del tablero.

    :return: Una lista de listas que representa el tablero vacío.
    :rtype: list
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]

# Funciones auxiliares para obtener las diagonales y columnas
def get_diagonal(board):
    """
    Retorna las diagonales del tablero.

    :param board: El tablero de juego.
    :type board: list
    :return: Una lista con las dos diagonales del tablero.
    :rtype: list
    """
    return [[board[0][0], board[1][1], board[2][2]],
            [board[0][2], board[1][1], board[2][0]]]

def get_columns(board):
    """
    Retorna las columnas del tablero.

    :param board: El tablero de juego.
    :type board: list
    :return: Una lista con las tres columnas del tablero.
    :rtype: list
    """
    columns = []
    for i in range(3):
        columns.append([row[i] for row in board])
    return columns

# Función auxiliar para verificar si una fila tiene todos los elementos iguales
def three_in_a_row(row):
    """
    Verifica si una fila tiene tres elementos iguales.

    :param row: Una fila del tablero.
    :type row: list
    :return: True si todos los elementos de la fila son iguales y no son None, False en caso contrario.
    :rtype: bool
    """
    return True if row.count(row[0]) == 3 else False

def player(board):
    """
    Retorna el jugador que tiene el siguiente turno en el tablero.

    :param board: El tablero de juego.
    :type board: list
    :return: 'X' si es el turno de X, 'O' si es el turno de O.
    :rtype: str
    """
    count_x = 0
    count_o = 0
    for i in board:
        for j in i:
            if j == "X":
                count_x += 1
            if j == "O":
                count_o += 1
    return O if count_x > count_o else X

def actions(board):
    """
    Retorna el conjunto de todas las acciones posibles (i, j) disponibles en el tablero.

    :param board: El tablero de juego.
    :type board: list
    :return: Un conjunto de tuplas (i, j) que representan las posiciones vacías.
    :rtype: set
    """
    action = set()
    for i, row in enumerate(board):
        for j, vall in enumerate(row):
            if vall == EMPTY:
                action.add((i, j))
    return action

def result(board, action):
    """
    Retorna el tablero que resulta al hacer el movimiento (i, j) en el tablero.

    :param board: El tablero de juego.
    :type board: list
    :param action: La acción a realizar, una tupla (i, j).
    :type action: tuple
    :raises Exception: Si la posición (i, j) ya está ocupada.
    :return: Un nuevo tablero con el movimiento realizado.
    :rtype: list
    """
    i, j = action
    if board[i][j] != EMPTY:
        raise Exception("Movimiento inválido")
    next_move = player(board)
    deep_board = deepcopy(board)  # Crea una copia profunda del tablero
    deep_board[i][j] = next_move
    return deep_board

def winner(board):
    """
    Retorna el ganador del juego, si existe.

    Verifica todas las filas, columnas y diagonales.

    :param board: El tablero de juego.
    :type board: list
    :return: 'X' si el jugador X ha ganado, 'O' si el jugador O ha ganado, None si no hay ganador.
    :rtype: str or None
    """
    rows = board + get_diagonal(board) + get_columns(board)
    for row in rows:
        current_player = row[0]
        if current_player is not None and three_in_a_row(row):
            return current_player
    return None

def terminal(board):
    """
    Retorna True si el juego ha terminado (ganador o empate), False en caso contrario.

    :param board: El tablero de juego.
    :type board: list
    :return: True si hay un ganador o si todas las casillas están llenas, False en caso contrario.
    :rtype: bool
    """
    if winner(board) is not None:
        return True
    if all(all(j != EMPTY for j in i) for i in board):
        return True
    return False

def utility(board):
    """
    Retorna 1 si X ha ganado, -1 si O ha ganado, 0 en caso contrario.

    :param board: El tablero de juego.
    :type board: list
    :return: 1 si X ha ganado, -1 si O ha ganado, 0 en caso de empate o si el juego no ha terminado.
    :rtype: int
    """
    win = winner(board)
    if win == X:
        return 1
    elif win == O:
        return -1
    else:
        return 0

# Poda Alfa-Beta: función Max-Value
def max_alpha_beta_pruning(board, alpha, beta):
    """
    Realiza la poda Alfa-Beta para el jugador X (Maximiza).

    :param board: El tablero de juego.
    :type board: list
    :param alpha: El valor alfa para la poda.
    :type alpha: float
    :param beta: El valor beta para la poda.
    :type beta: float
    :return: Un tuple con el valor de utilidad y la mejor acción.
    :rtype: tuple
    """
    if terminal(board):
        return utility(board), None
    value = float("-inf")
    best = None
    for action in actions(board):
        min_val, _ = min_alpha_beta_pruning(result(board, action), alpha, beta)
        if min_val > value:
            value = min_val
            best = action
        alpha = max(alpha, value)
        if beta <= alpha:
            break  # Ocurre la poda
    return value, best

# Poda Alfa-Beta: función Min-Value
def min_alpha_beta_pruning(board, alpha, beta):
    """
    Realiza la poda Alfa-Beta para el jugador O (Minimiza).

    :param board: El tablero de juego.
    :type board: list
    :param alpha: El valor alfa para la poda.
    :type alpha: float
    :param beta: El valor beta para la poda.
    :type beta: float
    :return: Un tuple con el valor de utilidad y la mejor acción.
    :rtype: tuple
    """
    if terminal(board):
        return utility(board), None
    value = float("inf")
    best = None
    for action in actions(board):
        max_val, _ = max_alpha_beta_pruning(result(board, action), alpha, beta)
        if max_val < value:
            value = max_val
            best = action
        beta = min(beta, value)
        if beta <= alpha:
            break  # Ocurre la poda
    return value, best

# Minimax con Poda Alfa-Beta
def minimax(board):
    """
    Retorna la acción óptima para el jugador actual en el tablero.

    Utiliza Poda Alfa-Beta para optimización.

    :param board: El tablero de juego.
    :type board: list
    :return: La mejor acción posible para el jugador actual.
    :rtype: tuple or None
    """
    if terminal(board):
        return None
    if player(board) == X:
        return max_alpha_beta_pruning(board, float("-inf"), float("inf"))[1]
    else:
        return min_alpha_beta_pruning(board, float("-inf"), float("inf"))[1]
    
# Minimax básico sin Poda Alfa-Beta
def basic_minimax(board):
    """
    Algoritmo Minimax básico sin Poda Alfa-Beta.

    Explora todo el árbol de juego sin poda.

    :param board: El tablero de juego.
    :type board: list
    :return: Un tuple con el valor de utilidad y la mejor acción.
    :rtype: tuple
    """
    if terminal(board):
        return utility(board), None

    current_player = player(board)

    if current_player == X:
        best_value = float('-inf')
        best_move = None
        for action in actions(board):
            value, _ = basic_minimax(result(board, action))
            if value > best_value:
                best_value = value
                best_move = action
        return best_value, best_move
    else:
        best_value = float('inf')
        best_move = None
        for action in actions(board):
            value, _ = basic_minimax(result(board, action))
            if value < best_value:
                best_value = value
                best_move = action
        return best_value, best_move