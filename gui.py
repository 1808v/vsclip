import tkinter as tk
from clipboard import save_to_history, load_history
import pyperclip

class ClippboardApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("VSClip")
        self.geometry("400x400")
        
        self.history_listbox = tk.Listbox(self, font=("Arial", 12))
        self.history_listbox.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        self.history_listbox.bind("<<ListboxSelect>>", self.on_select)

        self.update_history()

    def update_history(self):
        self.history_listbox.delete(0,tk.END)
        for item in load_history():
            self.history_listbox.insert(tk.END, item)

    def on_select(self, event):
        widget = event.widget
        if widget.curselection():
            index = widget.curselection()[0]
            value = widget.get(index)
            pyperclip.copy(value)
    
    def add_to_history(self, text):
        save_to_history(text)
        self.update_history()