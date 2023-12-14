# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
#  pyinstaller app.spec

import tkinter as tk
from tkinter import filedialog

class Notepad:
    def __init__(self, root):
        self.root = root
        self.root.title("Блокнот")
        self.text_area = tk.Text(self.root, undo=True)
        self.text_area.pack(fill="both", expand=True)
        self.setup_menu()

    def setup_menu(self):
        menu_bar = tk.Menu(self.root)
        file_menu = tk.Menu(menu_bar, tearoff=0)
        file_menu.add_command(label="Открыть", command=self.open_file)
        file_menu.add_command(label="Сохранить", command=self.save_file)
        file_menu.add_separator()
        file_menu.add_command(label="Выход", command=self.root.quit)
        menu_bar.add_cascade(label="Файл", menu=file_menu)

        edit_menu = tk.Menu(menu_bar, tearoff=0)
        edit_menu.add_command(label="Отменить", command=self.text_area.edit_undo)
        edit_menu.add_command(label="Повторить", command=self.text_area.edit_redo)
        menu_bar.add_cascade(label="Правка", menu=edit_menu)

        self.root.config(menu=menu_bar)

    def open_file(self):
        file_path = filedialog.askopenfilename(title="Открыть файл", filetypes=[("Текстовые файлы", "*.txt")])
        if file_path:
            with open(file_path, "r") as file:
                content = file.read()
            self.text_area.delete("1.0", "end")
            self.text_area.insert("1.0", content)

    def save_file(self):
        file_path = filedialog.asksaveasfilename(title="Сохранить файл", filetypes=[("Текстовые файлы", "*.txt")])
        if file_path:
            content = self.text_area.get("1.0", "end")
            with open(file_path, "w") as file:
                file.write(content)

root = tk.Tk()
notepad = Notepad(root)
root.mainloop()
