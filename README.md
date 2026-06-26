# Last Move Game Simulation

**Course:** Algorithms and Programming — Project 2  
**Students:** Orhun Sezgin, (Partner Student Number: 05220000334)  
**Contact:** orhunsez@gmail.com

---

## Project Description

A Python program that simulates **Last Move**, a two-player strategy board game. The program was developed as a course project for the Algorithms and Programming class at Ege University.

The playing field can be **3×3, 5×5, or 7×7** in size. Each player controls a big stone and takes turns moving it across the board, then placing a small stone on any empty square. The goal is to trap the opponent's big stone so it has no empty neighboring squares to move into.

---

## Game Rules

- Each player is represented by a unique capital letter (e.g. `X`, `Y`).
- Small stones placed on the board are represented by the letter `O`.
- At the start, each player's big stone is placed in the **center cell of their closest row**.
- On each turn, the active player:
  1. Moves their big stone one step in any of the 8 directions.
  2. Places a small stone on any empty square.
- A player **loses** when their big stone is completely surrounded — no adjacent square is empty.

---

## Movement Directions

| Input | Direction  |
|-------|------------|
| `N`   | North      |
| `S`   | South      |
| `E`   | East       |
| `W`   | West       |
| `NE`  | Northeast  |
| `NW`  | Northwest  |
| `SE`  | Southeast  |
| `SW`  | Southwest  |

---

## Board Layout Example (3×3)

```
    A   B   C
1 |   | Y |   | 1
------------------
2 |   |   |   | 2
------------------
3 |   | X |   | 3
    A   B   C
```

Rows are numbered (1–7), columns are lettered (A–G). Stone placement is entered as a row-column pair, e.g. `2B`.

---

## Running the Program

```bash
python last_move.py
```

Enter player letters when prompted, choose a board size (3, 5, or 7), and play. At the end of each game you will be asked whether to play again.

---

## Program Structure

| Function | Description |
|---|---|
| `game_jenerator` | Creates the board and prompts for board size with validation |
| `show_board` | Prints the current board state with row/column labels |
| `move_player` | Handles directional movement input and updates player position |
| `put_stone` | Handles small stone placement input and updates the board |
| `wincheck` | Checks both players for a surrounded state and announces the result |
| `main` | Entry point; manages player setup, game loop, and replay logic |

---

## Old Iterations

| File | Description |
|---|---|
| `deneme1.py` | First prototype — core functions working, single-player win check, no input validation |
| `deneme2.py` | Second iteration — win check refactored for both players, lose state tracking added |
| `05230000296_05220000334.py` | **Submitted final file** |

These were the iterations created before using git version control. They were merged into the single tracked file `last_move.py`.

---

## Final File History

| File | Description |
|---|---|
| `last_move.py` | First prototype — board, movement, stone placement, single-player win check |
| `last_move.py` | Refactored win check to evaluate both players and correctly announce the winner |
| `last_move.py` | **Submitted final** — input validation, global variable removed, movement dict refactor |
