# main.py
import tkinter as tk
from Controller.controller import CSVController

if __name__ == "__main__":
    root = tk.Tk()
    app = CSVController(root)
    root.mainloop()