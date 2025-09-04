# Importar librerias necesarias
import pygame
import random
import logging

# Inicializar pygame
pygame.init()

# Configurar logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# Definir algunos colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

# Dimensiones de la ventana
WIDTH, HEIGHT = 540, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Resolver Sudoku")


# Dimensiones del tablero
BOARD_SIZE = 9
CELL_SIZE = WIDTH // BOARD_SIZE

# Fuente
FONT = pygame.font.SysFont("comicsans", 40)
BUTTON_FONT = pygame.font.SysFont("comicsans", 20)

# Crear un tablero vacío
board = [[0 for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]
initial_board = [row[:] for row in board]
user_board = [row[:] for row in board]

def draw_grid(win):
    """Dibuja la cuadrícula del Sudoku."""
    for i in range(BOARD_SIZE + 1):
        thickness = 4 if i % 3 == 0 else 1
        pygame.draw.line(win, BLACK, (0, i * CELL_SIZE), (WIDTH, i * CELL_SIZE), thickness)
        pygame.draw.line(win, BLACK, (i * CELL_SIZE, 0), (i * CELL_SIZE, WIDTH), thickness)

def draw_numbers(win, board):
    """Dibuja los números en el tablero."""
    for i in range(BOARD_SIZE):
        for j in range(BOARD_SIZE):
            if board[i][j] != 0:
                color = BLACK if initial_board[i][j] != 0 else BLUE if user_board[i][j] != 0 else RED
                text = FONT.render(str(board[i][j]), True, color)
                win.blit(text, (j * CELL_SIZE + 15, i * CELL_SIZE + 15))

def draw_buttons(win):
    """Dibuja los botones en la parte inferior."""
    button_width, button_height = 100, 40
    button_y = HEIGHT - button_height - 10
    
    pygame.draw.rect(win, GRAY, (20, button_y, button_width, button_height))
    pygame.draw.rect(win, GRAY, (140, button_y, button_width, button_height))
    pygame.draw.rect(win, GRAY, (260, button_y, button_width, button_height))
    pygame.draw.rect(win, GRAY, (380, button_y, button_width, button_height))
    
    solve_text = BUTTON_FONT.render("Resolver", True, BLACK)
    close_text = BUTTON_FONT.render("Cerrar", True, BLACK)
    generate_text = BUTTON_FONT.render("Generar", True, BLACK)
    user_input_text = BUTTON_FONT.render("Manual", True, BLACK)
    
    win.blit(solve_text, (30, button_y + 5))
    win.blit(close_text, (150, button_y + 5))
    win.blit(generate_text, (270, button_y + 5))
    win.blit(user_input_text, (390, button_y + 5))

def draw_window(win, board):
    """Dibuja la ventana completa del juego."""
    win.fill(WHITE)
    draw_grid(win)
    draw_numbers(win, board)
    draw_buttons(win)
    pygame.display.update()

def find_empty(board):
    """Encuentra una celda vacía en el tablero."""
    for i in range(BOARD_SIZE):
        for j in range(BOARD_SIZE):
            if board[i][j] == 0:
                return (i, j)  # Devolver las coordenadas (i, j) cuando se encuentre una celda vacía
    return None  # Devolver None si no se encuentra ninguna celda vacía

def is_valid(board, num, pos):
    """Verifica si es válido colocar 'num' en la posición 'pos' del tablero."""
    for j in range(BOARD_SIZE):
        if board[pos[0]][j] == num and pos[1] != j:
            return False
    for i in range(BOARD_SIZE):
        if board[i][pos[1]] == num and pos[0] != i:
            return False
    box_x, box_y = pos[1] // 3, pos[0] // 3
    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if board[i][j] == num and (i, j) != pos:
                return False
    return True

def is_board_valid(board):
    """Verifica si el tablero inicial es válido."""
    for i in range(BOARD_SIZE):
        for j in range(BOARD_SIZE):
            num = board[i][j]
            if num != 0:
                board[i][j] = 0
                if not is_valid(board, num, (i, j)):
                    board[i][j] = num
                    return False
                board[i][j] = num
    return True

def solve_sudoku(board):
    """Resuelve el Sudoku utilizando backtracking."""
    empty = find_empty(board)
    if not empty:
        return True
    row, col = empty
    for num in range(1, 10):
        if is_valid(board, num, (row, col)):
            board[row][col] = num
            if solve_sudoku(board):
                return True
            board[row][col] = 0
    return False

def generate_random_board():
    """Genera un tablero de Sudoku aleatorio y resoluble."""
    global board, initial_board, user_board
    board = [[0 for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]
    solve_sudoku(board)  # Resuelve un tablero vacío para obtener una solución completa
    cells_to_remove = 45  # Número de celdas a eliminar para obtener un tablero con dificultad media
    while cells_to_remove > 0:
        row, col = random.randint(0, 8), random.randint(0, 8)
        while board[row][col] == 0:
            row, col = random.randint(0, 8), random.randint(0, 8)
        board[row][col] = 0
        cells_to_remove -= 1
    initial_board = [r[:] for r in board]
    user_board = [[0 for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]
    logging.debug(f'Tablero generado: {board}')

def main():
    """Función principal del juego."""
    global board, initial_board, user_board
    run = True
    user_input_mode = False
    selected_cell = None

    while run:
        draw_window(WIN, board)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN:
                if user_input_mode:
                    if event.key == pygame.K_RETURN:
                        user_input_mode = False
                        initial_board = [r[:] for r in board]
                        if not is_board_valid(board) or not solve_sudoku([r[:] for r in board]):
                            print("El tablero ingresado manualmente no es válido o no tiene solución.")
                            board = [r[:] for r in initial_board]
                    elif selected_cell and event.unicode.isdigit():
                        num = int(event.unicode)
                        y, x = selected_cell
                        if is_valid(board, num, (y, x)):
                            board[y][x] = num
                            user_board[y][x] = num
                else:
                    if event.key == pygame.K_SPACE:
                        if is_board_valid(board):
                            solve_sudoku(board)
                        else:
                            print("El tablero tiene errores y no puede ser resuelto")

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                x, y = pos[0] // CELL_SIZE, pos[1] // CELL_SIZE
                button_width, button_height = 100, 40
                button_y = HEIGHT - button_height - 10
                if x < BOARD_SIZE and y < BOARD_SIZE:
                    selected_cell = (y, x)
                # Check if the solve button is clicked
                if 20 <= pos[0] <= 120 and button_y <= pos[1] <= button_y + button_height:
                    if is_board_valid(board):
                        solve_sudoku(board)
                    else:
                        print("El tablero tiene errores y no puede ser resuelto")
                # Check if the close button is clicked
                if 140 <= pos[0] <= 240 and button_y <= pos[1] <= button_y + button_height:
                    run = False
                # Check if the generate button is clicked
                if 260 <= pos[0] <= 360 and button_y <= pos[1] <= button_y + button_height:
                    generate_random_board()
                    user_input_mode = False
                # Check if the user input button is clicked
                if 380 <= pos[0] <= 480 and button_y <= pos[1] <= button_y + button_height:
                    user_input_mode = True
                    board = [[0 for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]
                    initial_board = [r[:] for r in board]
                    user_board = [r[:] for r in board]

    pygame.quit()

if __name__ == "__main__":
    main()






    







