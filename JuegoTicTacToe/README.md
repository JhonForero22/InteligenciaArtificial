# Triki (Tic-Tac-Toe) con Minimax y Poda Alfa-Beta
Este proyecto implementa el clásico juego de Triki (Tic-Tac-Toe) utilizando el algoritmo 
Minimax con Poda Alfa-Beta para optimizar la búsqueda de la jugada óptima. También se 
incluye una versión básica del algoritmo Minimax sin optimización. El código está escrito 
en Python y simula un jugador que toma decisiones óptimas para ganar el juego.
El objetivo es crear una IA eficiente que juege contra los humanos, evaluado 
y decidiendo los mejores movimientos posibles en el tablero.
La investigación busca comparar ambos algoritmos en términos de tiempo y movimientos posibles,
además de una interfaz interactiva.

**Características:**
- Simulación del juego Triki: El juego sigue las reglas estándar del Triki.
- Algoritmo Minimax: El Algoritmo toma decisiones óptimas basadas en el algoritmo Minimax.
- Poda Alfa-Beta: Se usa para mejorar la eficiencia del algoritmo reduciendo el número de nodos evaluados.
- Soporte para Minimax básico: Se incluye una versión no optimizada del algoritmo Minimax.
- Detección de ganador: El juego determina si hay un ganador o si hay empate.
- Funcionalidad completa del juego: Jugador vs Computadora optimizada.

# Implementacion 
El desarrollo del proyecto se va a realizar en Python, integrando la librería Pygame, para genera una interfaz grafica, estará divido en dos módulos:

- ***runner.py***: Contiene la lógica de la interfaz grafica, manejo y flujo de juego. Además de mostrar el tablero y registrar los movimiento del jugador.

- ***tictactoe.py***: Contiene la implementa la lógica del juego Tic-Tac-Toe y los algoritmos de inteligencia artificial, incluyendo Minimax y la optimización con Poda Alfa-Beta. 

# Requisitos
- **1 -> Instalar Python:**
  Puedes instalar python desde [aqui](https://www.python.org/downloads/)
- **2 -> Clonar el resositorio:**
```bash
git clone https://github.com/tu-usuario/nombre-repositorio.git
cd nombre-repositorio
```

- **3 -> Ejecutar el codigo:**
  Dentro de la carpeta ejecutar el comando:
```bash
python runner.py
```

# Estructura del Código:
El código consta de las siguientes partes importantes:

## Logica del juego
#### - initial_state(): Devuelve el estado inicial del tablero vacío.
![image](https://github.com/user-attachments/assets/9cd139c3-a2c0-4516-9e91-269476d19343)

## Funciones del juego
#### - player(board): Retorna el jugador que tiene el siguiente turno (X u O).
#### - actions(board): Lista todas las acciones posibles en el tablero (casillas vacías).
#### - result(board, action): Aplica una acción al tablero y devuelve el nuevo estado.
![image](https://github.com/user-attachments/assets/47f0dc33-7e30-4fa3-9ba8-22ccea1f10f8)
![image](https://github.com/user-attachments/assets/19ea97d9-1b8a-485d-bc71-7925b5df146d)

## Estado del juego
#### - winner(board): Determina si hay un ganador en el juego.
#### - terminal(board): Verifica si el juego ha terminado (ganador o empate).
#### - utility(board): Evalúa el resultado del juego: 1 si gana X, -1 si gana O, 0 si es empate.
![image](https://github.com/user-attachments/assets/5c9e910a-10e5-4fa8-94bc-7fe16ade8fd0)
![image](https://github.com/user-attachments/assets/0c47838b-f07a-4338-9e73-70ddc8446fc2)
![image](https://github.com/user-attachments/assets/456d5618-9c78-427f-bd66-d0455a153c97)

## Minimax 
#### - basic_minimax(board): Versión no optimizada del algoritmo Minimax.
![image](https://github.com/user-attachments/assets/2c4056a3-6616-4f88-911e-02a8651cb134)

## Minimax Poda Alfa-Beta
#### - minimax(board): Implementación del algoritmo Minimax con Poda Alfa-Beta.
![image](https://github.com/user-attachments/assets/9606f2eb-300d-4558-9039-976fb612a73d)
![image](https://github.com/user-attachments/assets/5d2b3253-f2d8-4e97-854c-6c99a331dfc8)
![image](https://github.com/user-attachments/assets/e49b1015-f3ab-4406-840c-a43e5d995a44)

# Ejecución del Juego
- El tablero se representa como una matriz 3x3, donde cada casilla puede estar vacía (None), ocupada por una 'X', o ocupada por una 'O'.
- El jugador juega con 'X' o 'O', y la computadora toma decisiones usando Minimax con Poda Alfa-Beta.
- El juego continúa hasta que haya un ganador o un empate.

# Decisión Óptima:
El algoritmo Minimax evaluará todas las acciones posibles y retornará la mejor jugada para el jugador actual.

### Captura de Pantalla
![Juego](https://github.com/user-attachments/assets/78d8da56-6e68-49f3-9871-836b3bf407da)
![image](https://github.com/user-attachments/assets/892348f9-f373-4db6-80a5-87fac653fe86)
![image](https://github.com/user-attachments/assets/f5dae8d3-d3ef-4bbb-9176-4a26ca4e7299)
