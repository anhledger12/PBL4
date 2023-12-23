# controller
from tkinter import filedialog
import tkinter as tk
from View.view import CSVViewerApp
from Model.model import CSVModel


class CSVController:
    def __init__(self, root):
        self.root = root
        self.root.title("CSV Viewer")

        self.view = CSVViewerApp(root, self)
        self.model = CSVModel()

    def open_csv(self):
        file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])

        if file_path:
            df = self.model.read_csv(file_path)
            if df is not None:
                self.view.display_csv_content(df)
            else:
                self.view.display_empty_message()
