# From Logic to AI
### Building a Tic Tac Toe AI from scratch — using pure python and logic.
---

## What is this?

This project started as a simple two-player Tic Tac Toe game and evolved into an unbeatable AI using the Minimax algorithm with Alpha-Beta Pruning. Every single piece was built and understood from the ground up — not copied, not imported, just reasoned through step by step.

---

## Journey

### Stage 1 — Basic Game Logic
Started with a 2D list representing the board and two player classes taking turns. Learned that a 2D list in Python can hold mixed types (integers + strings), which is why plain Python lists were chosen over NumPy arrays.

```
board = [[0, 1, 2],
         [3, 4, 5],
         [6, 7, 8]]
```
Numbers represent empty cells. When a player moves, the number gets replaced by `"*"` or `"o"`. The number itself acts as the position identifier — which later became key to the AI.

---

### Stage 2 — check_win() and get_empty_cells()
Two critical helper functions were built before touching any AI logic:

**check_win()** returns:
- `"*"` if Player 1 wins
- `"o"` if AI wins
- `"draw"` if no empty cells and no winner
- `None` if the game is still going

The key insight here was that "no winner yet" and "draw" are NOT the same thing. A draw only happens when there are no empty cells left AND no winner. Mid-game with no winner yet is just `None`.

**get_empty_cells()** loops through the board and collects any cell that is not `"*"` or `"o"` — meaning it still holds its original number. That number doubles as the position identifier for the AI.

---

### Stage 3 — Understanding Minimax

The core question was: *"how do you build a tree from a 2D list?"*

The answer: **you don't**. The recursion itself IS the tree. There is only one board the whole time. You modify it, recurse deeper, then undo the move and try the next branch. The recursion call stack holds the "memory" of how you got there.

```
minimax(True)                        ← AI's turn
├── place "o" at cell 1
│   minimax(False)                   ← Human's turn
│   ├── place "*" at cell 2
│   │   minimax(True) → base case   ← game over, return score
│   │   undo cell 2
│   undo cell 1
├── place "o" at cell 2
│   minimax(False) ...
```

**Scores are always from the AI's perspective:**
- AI (`"o"`) wins → `+1`
- Human (`"*"`) wins → `-1`
- Draw → `0`

**Maximizer vs Minimizer:**
- `is_maximizing = True` → AI's turn → picks highest score
- `is_maximizing = False` → Human's turn → picks lowest score (worst for AI)

They alternate every level. AI maximizes, human minimizes, AI maximizes — all the way down until a terminal state is reached.

---

### Stage 4 — The place() function

Instead of a 50-line if-elif chain mapping positions to board cells, a simple mathematical formula handles it:

```python
def place(num, mark):
    row = num // 3
    col = num % 3
    board[row][col] = mark
```

Cell 0 → row 0, col 0. Cell 5 → row 1, col 2. The `//` and `%` operators do all the work.

Undoing a move is equally simple — the cell's original value was the number itself, so:
```python
place(cell, cell)  # restore the number back
```

---

### Stage 5 — Alpha-Beta Pruning

Pure Minimax explores every possible game state. For Tic Tac Toe that's 9! = 362,880 states — fast enough. But for chess that's 30^80 — impossible even for the fastest computer.

Alpha-Beta Pruning solves this by skipping branches that can never affect the final decision.

Two new parameters are added:
- **alpha** — best score the maximizer has found so far
- **beta** — best score the minimizer has found so far

When they cross (`alpha >= beta`), there's no point exploring further. The opponent would never allow that path.

```python
# Maximizer
alpha = max(alpha, best_score)
if alpha >= beta:
    break  # prune

# Minimizer
beta = min(beta, best_score)
if beta <= alpha:
    break  # prune
```

The final answer is identical to plain Minimax — just reached much faster by skipping useless branches.

---

## Why not NumPy?

NumPy arrays are typed — mixing integers and strings in the same array requires `dtype=object` which defeats NumPy's purpose. Plain Python lists handle mixed types naturally and the board is tiny (3x3), so NumPy's speed advantage means nothing here.

---

## Why not build an explicit tree?

For Tic Tac Toe, the entire game state fits in one 2D list. The recursion stack implicitly builds the tree without storing it anywhere. For more complex games (chess, Go), each state would need an explicit object capturing board position, whose turn it is, special rules etc. — and `generate_moves(state)` would return new state objects instead of modifying one board in place.

---

## Can you beat the AI?

No. A perfectly implemented Minimax AI is mathematically unbeatable at Tic Tac Toe. The best possible outcome for a human playing optimally is a draw. If you ever win, there's a bug somewhere.

---

## Files

| File | Description |
|------|-------------|
| `tictactoe.py` | Final clean version with all improvements |

---

## Concepts Covered

- 2D list manipulation
- Recursive algorithms
- Game tree search
- Minimax algorithm
- Alpha-Beta Pruning
- Input validation
- Global vs local state management

---

## What's Next?

- Implement depth limiting for larger boards
- Add a heuristic evaluation function
- Extend to Connect Four or chess
- Explore how neural networks replace hand-crafted evaluation (AlphaZero style)

---

*Built step by step, understood piece by piece.*
