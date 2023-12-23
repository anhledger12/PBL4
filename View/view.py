# view
import tkinter as tk


class CSVViewerApp:
    def __init__(self, root, controller):
        self.root = root
        self.controller = controller

        self.create_widgets()

    def create_widgets(self):
        self.open_button = tk.Button(
            self.root, text="Open CSV", command=self.controller.open_csv
        )
        self.open_button.pack(pady=10)

        self.text_widget = tk.Text(self.root, wrap="none")
        self.text_widget.pack(expand=True, fill="both", padx=10, pady=10)

    def display_csv_content(self, df):
        self.text_widget.delete(1.0, tk.END)
        csv_content = df.to_string(index=False)
        self.text_widget.insert(tk.END, csv_content)

    def display_empty_message(self):
        self.text_widget.delete(1.0, tk.END)
        self.text_widget.insert(tk.END, "The selected CSV file is empty.")