# Função para imprimir o tabuleiro
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

# Função para verificar se há um vencedor
def check_winner(board, player):
    # Verificar linhas
    for row in board:
        if all([cell == player for cell in row]):
            return True

    # Verificar colunas
    for col in range(3):
        if all([board[row][col] == player for row in range(3)]):
            return True

    # Verificar diagonais
    if all([board[i][i] == player for i in range(3)]) or all([board[i][2 - i] == player for i in range(3)]):
        return True

    return False

# Função para verificar se o tabuleiro está cheio
def is_board_full(board):
    return all([cell != " " for row in board for cell in row])

# Função principal do jogo
def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"

    while True:
        print_board(board)
        row = int(input(f"Jogador {current_player}, escolha a linha (0, 1, 2): "))
        col = int(input(f"Jogador {current_player}, escolha a coluna (0, 1, 2): "))

        if board[row][col] == " ":
            board[row][col] = current_player
            if check_winner(board, current_player):
                print_board(board)
                print(f"Jogador {current_player} venceu!")
                break
            elif is_board_full(board):
                print_board(board)
                print("Empate!")
                break
            current_player = "O" if current_player == "X" else "X"
        else:
            print("Posição já ocupada. Tente novamente.")

# Iniciar o jogo
tic_tac_toe()