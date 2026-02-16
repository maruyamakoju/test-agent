"""Othello (Reversi) game with tkinter GUI."""

import tkinter as tk

BOARD_SIZE = 8
CELL_SIZE = 60
MARGIN = 4
COLORS = {"B": "#111111", "W": "#EEEEEE", "board": "#006400", "line": "#004400"}

DIRECTIONS = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]


class Othello:
    def __init__(self, root):
        self.root = root
        self.root.title("Othello")
        self.root.resizable(False, False)

        self.board = [[None] * BOARD_SIZE for _ in range(BOARD_SIZE)]
        self.turn = "B"

        canvas_size = CELL_SIZE * BOARD_SIZE
        self.canvas = tk.Canvas(root, width=canvas_size, height=canvas_size, bg=COLORS["board"])
        self.canvas.pack(padx=10, pady=(10, 0))
        self.canvas.bind("<Button-1>", self._on_click)

        self.status = tk.Label(root, text="", font=("Arial", 14))
        self.status.pack(pady=5)

        btn_frame = tk.Frame(root)
        btn_frame.pack(pady=(0, 10))
        tk.Button(btn_frame, text="New Game", command=self._new_game).pack()

        self._new_game()

    def _new_game(self):
        self.board = [[None] * BOARD_SIZE for _ in range(BOARD_SIZE)]
        mid = BOARD_SIZE // 2
        self.board[mid - 1][mid - 1] = "W"
        self.board[mid - 1][mid] = "B"
        self.board[mid][mid - 1] = "B"
        self.board[mid][mid] = "W"
        self.turn = "B"
        self._draw()

    def _draw(self):
        self.canvas.delete("all")
        # Grid lines
        for i in range(BOARD_SIZE + 1):
            pos = i * CELL_SIZE
            end = BOARD_SIZE * CELL_SIZE
            self.canvas.create_line(pos, 0, pos, end, fill=COLORS["line"])
            self.canvas.create_line(0, pos, end, pos, fill=COLORS["line"])

        # Stones and valid-move hints
        valid = self._all_valid_moves(self.turn)
        for r in range(BOARD_SIZE):
            for c in range(BOARD_SIZE):
                x = c * CELL_SIZE + CELL_SIZE // 2
                y = r * CELL_SIZE + CELL_SIZE // 2
                radius = CELL_SIZE // 2 - MARGIN
                if self.board[r][c]:
                    self.canvas.create_oval(
                        x - radius, y - radius, x + radius, y + radius,
                        fill=COLORS[self.board[r][c]], outline="#333333", width=1,
                    )
                elif (r, c) in valid:
                    hint_r = 6
                    self.canvas.create_oval(
                        x - hint_r, y - hint_r, x + hint_r, y + hint_r,
                        fill="#228B22", outline="",
                    )

        # Status
        b_count = sum(cell == "B" for row in self.board for cell in row)
        w_count = sum(cell == "W" for row in self.board for cell in row)
        name = {"B": "Black", "W": "White"}
        if valid:
            msg = f"{name[self.turn]}'s turn   |   Black: {b_count}  White: {w_count}"
        elif self._all_valid_moves(self._opponent()):
            msg = f"{name[self.turn]} has no moves – passing   |   Black: {b_count}  White: {w_count}"
        else:
            if b_count > w_count:
                winner = "Black wins!"
            elif w_count > b_count:
                winner = "White wins!"
            else:
                winner = "Draw!"
            msg = f"Game Over – {winner}   |   Black: {b_count}  White: {w_count}"
        self.status.config(text=msg)

    def _opponent(self):
        return "W" if self.turn == "B" else "B"

    def _flips(self, r, c, player):
        """Return list of positions flipped by placing player's stone at (r, c)."""
        if self.board[r][c] is not None:
            return []
        opp = "W" if player == "B" else "B"
        all_flips = []
        for dr, dc in DIRECTIONS:
            flips = []
            nr, nc = r + dr, c + dc
            while 0 <= nr < BOARD_SIZE and 0 <= nc < BOARD_SIZE and self.board[nr][nc] == opp:
                flips.append((nr, nc))
                nr += dr
                nc += dc
            if flips and 0 <= nr < BOARD_SIZE and 0 <= nc < BOARD_SIZE and self.board[nr][nc] == player:
                all_flips.extend(flips)
        return all_flips

    def _all_valid_moves(self, player):
        return {(r, c) for r in range(BOARD_SIZE) for c in range(BOARD_SIZE) if self._flips(r, c, player)}

    def _on_click(self, event):
        c = event.x // CELL_SIZE
        r = event.y // CELL_SIZE
        if not (0 <= r < BOARD_SIZE and 0 <= c < BOARD_SIZE):
            return

        flips = self._flips(r, c, self.turn)
        if not flips:
            return

        # Place stone and flip
        self.board[r][c] = self.turn
        for fr, fc in flips:
            self.board[fr][fc] = self.turn

        # Advance turn
        self.turn = self._opponent()
        if not self._all_valid_moves(self.turn):
            self.turn = self._opponent()

        self._draw()


if __name__ == "__main__":
    root = tk.Tk()
    Othello(root)
    root.mainloop()
