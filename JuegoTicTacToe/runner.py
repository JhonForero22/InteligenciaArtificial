import pygame
import sys
import time

import tictactoe as ttt

pygame.init()
size = width, height = 600, 400

# Cargar la imagen de fondo
background_image = pygame.image.load('juego.png')
background_image = pygame.transform.scale(background_image, (width, height))

# Colores
black = (0, 0, 0)
white = (255, 255, 255)

# Configuración de la pantalla
screen = pygame.display.set_mode(size)

# Fuentes para los textos
mediumFont = pygame.font.SysFont("Arial", 28)
largeFont = pygame.font.SysFont("Arial", 40)
moveFont = pygame.font.SysFont("Arial", 60)

user = None  # Variable para almacenar el jugador humano ('X' o 'O')
board = ttt.initial_state()  # Estado inicial del tablero
ai_turn = False  # Indica si es el turno de la IA

use_alpha_beta = True # Aquí se decide si usar o no Alpha-Beta Pruning

def reset_game():
    global board, ai_turn, user
    board = ttt.initial_state()  # Reiniciar el tablero
    ai_turn = False
    user = None
    screen.fill(black)  # Limpiar el fondo al reiniciar el juego

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()  # Cierra la ventana si el usuario sale

    if user is None:
        # Mostrar la imagen de fondo solo en la pantalla de selección
        screen.blit(background_image, [0, 0])

        # Dibujar el título
        title = largeFont.render("Tic-Tac-Toe", True, white)
        titleRect = title.get_rect()
        titleRect.center = ((width / 2), 145)
        screen.blit(title, titleRect)

        # Dibujar botones para elegir 'X' o 'O'
        playXButton = pygame.Rect((width / 8), (height / 2), width / 4, 50)
        playX = mediumFont.render("Jugar con X", True, black)
        playXRect = playX.get_rect()
        playXRect.center = playXButton.center
        pygame.draw.rect(screen, white, playXButton)
        screen.blit(playX, playXRect)

        playOButton = pygame.Rect(5 * (width / 8), (height / 2), width / 4, 50)
        playO = mediumFont.render("Jugar con O", True, black)
        playORect = playO.get_rect()
        playORect.center = playOButton.center
        pygame.draw.rect(screen, white, playOButton)
        screen.blit(playO, playORect)

        # Verificar si el usuario hace clic en un botón
        click, _, _ = pygame.mouse.get_pressed()
        if click == 1:
            mouse = pygame.mouse.get_pos()
            if playXButton.collidepoint(mouse):
                time.sleep(0.2)
                user = ttt.X  # Usuario juega con 'X'
                ai_turn = False
                screen.fill(black)  # Cambiar el fondo a negro al empezar el juego
            elif playOButton.collidepoint(mouse):
                time.sleep(0.2)
                user = ttt.O  # Usuario juega con 'O'
                ai_turn = False
                screen.fill(black)  # Cambiar el fondo a negro al empezar el juego
    else:
        # Durante el juego, mantener el fondo negro
        screen.fill(black)

        # Dibujar el tablero del juego
        tile_size = 80
        tile_origin = (width / 2 - (1.5 * tile_size),
                       height / 2 - (1.5 * tile_size))
        tiles = []
        for i in range(3):
            row = []
            for j in range(3):
                rect = pygame.Rect(
                    tile_origin[0] + j * tile_size,
                    tile_origin[1] + i * tile_size,
                    tile_size, tile_size
                )
                pygame.draw.rect(screen, white, rect, 3)

                if board[i][j] != ttt.EMPTY:
                    move = moveFont.render(board[i][j], True, white)
                    moveRect = move.get_rect()
                    moveRect.center = rect.center
                    screen.blit(move, moveRect)
                row.append(rect)
            tiles.append(row)

        game_over = ttt.terminal(board)  # Verificar si el juego ha terminado
        player = ttt.player(board)  # Obtener el jugador actual

        # Mostrar el título según el estado del juego
        if game_over:
            winner = ttt.winner(board)
            if winner is None:
                title = "Empate"
            else:
                if winner == user:
                    title = "Usuario Gana"  # Mensaje si el usuario gana
                else:
                    title = "IA gana"  # Mensaje si la IA gana
        elif user == player:
            title = f"Usuario juega con {user}"
        else:
            title = "IA pensando..."
        title = largeFont.render(title, True, white)
        titleRect = title.get_rect()
        titleRect.center = ((width / 2), 30)
        screen.blit(title, titleRect)

        # Movimiento de la IA
        if user != player and not game_over:
            start_time = time.time()  # Medir el tiempo de inicio

            if use_alpha_beta:
                move = ttt.minimax(board)  # Algoritmo Minimax con poda Alfa-Beta
                algorithm_used = "Minimax con Alpha-Beta Pruning"
            else:
                _, move = ttt.basic_minimax(board)  # Algoritmo Minimax básico
                algorithm_used = "Minimax básico sin Alpha-Beta Pruning"

            end_time = time.time()  # Medir el tiempo de finalización
            print(f"Tiempo de ejecución para {algorithm_used}: {end_time - start_time:.4f} segundos")

            board = ttt.result(board, move)  # Actualizar el tablero con el movimiento de la IA
            ai_turn = False
        else:
            ai_turn = True

        # Verificar si el usuario realiza un movimiento
        click, _, _ = pygame.mouse.get_pressed()
        if click == 1 and user == player and not game_over:
            mouse = pygame.mouse.get_pos()
            for i in range(3):
                for j in range(3):
                    if (board[i][j] == ttt.EMPTY and tiles[i][j].collidepoint(mouse)):
                        board = ttt.result(board, (i, j))

        # Si el juego ha terminado, ofrecer la opción de volver a jugar
        if game_over:
            againButton = pygame.Rect(width / 3, height - 65, width / 3, 50)
            again = mediumFont.render("Jugar de nuevo", True, black)
            againRect = again.get_rect()
            againRect.center = againButton.center
            pygame.draw.rect(screen, white, againButton)
            screen.blit(again, againRect)
            click, _, _ = pygame.mouse.get_pressed()
            if click == 1:
                mouse = pygame.mouse.get_pos()
                if againButton.collidepoint(mouse):
                    time.sleep(0.2)
                    reset_game()  # Reiniciar el juego y limpiar la pantalla

    pygame.display.flip()  # Actualizar la pantalla
