from tkinter import Button, Frame, messagebox
from game_logic import Minesweeper
from config import GRID_SIZE, NUM_MINES

class MinesweeperGUI:
    def __init__(self, root):
        self.root = root
        self.game = Minesweeper(GRID_SIZE, GRID_SIZE, NUM_MINES)
        self.buttons = {}
        self.game_over_flag = False
        self.create_widgets()

    def create_widgets(self):
        frame = Frame(self.root)
        frame.pack()

        # Create the grid of buttons
        for row in range(GRID_SIZE):
            for col in range(GRID_SIZE):
                button = Button(frame, width=3, height=1, command=lambda r=row, c=col: self.on_click(r, c))
                button.grid(row=row, column=col)
                self.buttons[(row, col)] = button

        # Create the restart button
        restart_button = Button(self.root, text="Restart Game", command=self.restart_game)
        restart_button.pack(pady=10)

    def on_click(self, row, col):
        if not self.game_over_flag:
            self.reveal_cell(row, col)

    def reveal_cell(self, row, col):
        cell_value = self.game.grid[row][col]
        button = self.buttons[(row, col)]
        if cell_value == -1:
            button.config(text="*", bg="red")
            self.game_over()
        else:
            button.config(text=str(cell_value), state="disabled")
            if cell_value == 0:
                self.reveal_adjacent_cells(row, col)  # You may implement this method to reveal surrounding cells

    def reveal_adjacent_cells(self, row, col):
        # Optional method to reveal adjacent cells when the cell value is 0
        pass

    def game_over(self):
        self.game_over_flag = True
        messagebox.showinfo("Game Over", "You clicked on a mine! Game Over!")
        self.reveal_all_mines()

    def reveal_all_mines(self):
        for (row, col), button in self.buttons.items():
            if self.game.grid[row][col] == -1:
                button.config(text="*", bg="red")

    def restart_game(self):
        # Reset the game state
        self.game_over_flag = False
        self.game = Minesweeper(GRID_SIZE, GRID_SIZE, NUM_MINES)
        
        # Reset all buttons
        for row in range(GRID_SIZE):
            for col in range(GRID_SIZE):
                button = self.buttons[(row, col)]
                button.config(text="", bg="SystemButtonFace", state="normal")
