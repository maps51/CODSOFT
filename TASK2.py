'''
TASK 2: Implement an AI agent that plays the classic game of Tic-Tac-Toe
against a human player. You can use algorithms like Minimax with
or without Alpha-Beta Pruning to make the AI player unbeatable.
This project will help you understand game theory and basic search 
algorithms.

'''

#Tic-Tac-Toe game with AI using Minimax Algorithm

#Creating tic-tac-toe grid
def display_grid(grid):
    for row in grid:
        print(" | ".join(row))
        print("-" * 9)

#Determines winner through conditions
def winner(grid, player):
    for row in grid:
        if all(cell == player for cell in row):
            return True

    for col in range(3):
        if all(grid[row][col] == player for row in range(3)):
            return True

    if all(grid[i][i] == player for i in range(3)) or all(grid[i][2 - i] == player for i in range(3)):
        return True

    return False

#Checks if its a draw
def draw(grid):
    return all(cell != ' ' for row in grid for cell in row)

#Checks if its game over
def gameover(grid):
    return winner(grid, 'X') or winner(grid, 'O') or draw(grid)

#Algorithm Minimax
def minimax(grid, depth, maximizing):
    if winner(grid, 'X'):
        return -1
    if winner(grid, 'O'):
        return 1
    if draw(grid):
        return 0
    if maximizing:
        best_score = -float('inf')
        for row in range(3):
            for col in range(3):
                if grid[row][col] == ' ':
                    grid[row][col] = 'O'
                    score = minimax(grid, depth + 1, False)
                    grid[row][col] = ' '
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for row in range(3):
            for col in range(3):
                if grid[row][col] == ' ':
                    grid[row][col] = 'X'
                    score = minimax(grid, depth + 1, True)
                    grid[row][col] = ' '
                    best_score = min(score, best_score)
        return best_score

#Finding optimal move for AI
def get_best_move(grid):
    best_score = -float('inf')
    best_move = None
    for row in range(3):
        for col in range(3):
            if grid[row][col] == ' ':
                grid[row][col] = 'O'
                score = minimax(grid, 0, False)
                grid[row][col] = ' '
                if score > best_score:
                    best_score = score
                    best_move = (row, col)
    return best_move

#Game flow
def main():
    grid = [[' ' for _ in range(3)] for _ in range(3)]
    print("Tic-Tac-Toe")
    print("\nThe index of rows and columns in this game begin from 0 and end with 2.\n\nEnter your move like <row_index><space><column_index>.\n")
    display_grid(grid)
    while not gameover(grid):
        row, col = map(int, input("Enter your move (row col): ").split())
        if grid[row][col] == ' ':
            grid[row][col] = 'X'
            display_grid(grid)
            if not gameover(grid):
                print("AI's move")
                best_move = get_best_move(grid)
                grid[best_move[0]][best_move[1]] = 'O'
                display_grid(grid)
        else:
            print("Invalid move. Try again.")
    if winner(grid, 'X'):
        print("You win!")
    elif winner(grid, 'O'):
        print("AI wins!")
    else:
        print("It's a draw!")


if __name__ == "__main__":
    main()
