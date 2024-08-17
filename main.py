from tkinter import Tk
from gui_components import MinesweeperGUI

def main():
    root = Tk()
    root.title("Minesweeper")
    game = MinesweeperGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
