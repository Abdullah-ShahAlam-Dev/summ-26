import random

def attacking_pairs(board):
    attacks = 0
    for i in range(8):
        for j in range(i + 1, 8):
            # Check column attacks and diagonal attacks
            if board[i] == board[j]:
                attacks += 1
            elif abs(board[i] - board[j]) == abs(i - j):
                attacks += 1
    return attacks

def hill_climbing():
    # Random initial board create karna
    board = [random.randint(0, 7) for _ in range(8)]
    current = attacking_pairs(board)

    print("Initial Board:", board)
    print("Attacking Pairs:", current)

    while True:
        best_board = board[:]
        best_score = current

        # Har queen ko uski row mein move kar ke check karna
        for row in range(8):
            for col in range(8):
                if board[row] == col:
                    continue

                new_board = board[:]
                new_board[row] = col
                score = attacking_pairs(new_board)

                # Agar naya move behtar hai (attacks kam hain)
                if score < best_score:
                    best_score = score
                    best_board = new_board

        # Agar mazeed koi behtar move na mile toh ruk jana
        if best_score >= current:
            print("\nLocal Optimum Reached")
            print("Final Board:", board)
            print("Final Attacking Pairs:", current)
            break
        
        # Best move ko current board bana dena
        board = best_board
        current = best_score
        print(f"Move: {board} | Attacking Pairs: {current}")

# Function ko chalana
hill_climbing()