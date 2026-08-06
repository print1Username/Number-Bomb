import tkinter as tk
from tkinter import messagebox


class Windows(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)

        self.width = 800
        self.height = 600

        self.title("Number Bomb")
        self.geometry(f"{self.width}x{self.height}")

    def LoadIconFiles(self, path):
        try:
            self.iconbitmap(path)
        except tk.TclError as e:
            print(f"Warning: Icon not found ({e})")
        else:
            print("Icon loaded successful.")

    def LoadTitle(self, text):
        label = tk.Label(
            self,
            text=text,
            font=("Arial", 32, "bold"),
            fg="black",
        )
        label.pack(pady=20)
        print('Title loaded successful.')

    def LoadContent(self, text):
        label = tk.Label(
            self,
            text=text,
            font=("Arial", 22, "normal"),
            fg="black",
        )
        label.pack(pady=20)
        print('Content loaded successful.')

    def LoadButton(self, text, command_func = None):
        button = tk.Button(
            self,
            text=text,
            font=("Arial", 18, "bold"),
            width=10,
            height=2,
            fg="black",
            command=command_func,
        )
        button.pack(pady=20)
        print('Button loaded successful.')

        return button

    def LoadInsert(self, text):
        placeholder = text
        placeholder_color = "gray"
        default_color = "black"

        def validate_digit(p):
            if p == "" or p.isdigit():
                return True
            return False

        vcmd = (self.register(validate_digit), '%P')

        entry = tk.Entry(
            self,
            font=("Arial", 18, "normal"),
            fg=placeholder_color
        )
        entry.pack(pady=20)

        entry.insert(0, placeholder)

        def on_focus_in(event):
            if entry.get() == placeholder:
                entry.delete(0, tk.END)
                entry.config(fg=default_color)
                entry.config(validate="key", validatecommand=vcmd)

        def on_focus_out(event):
            if not entry.get().strip():
                entry.config(validate="none")
                entry.insert(0, placeholder)
                entry.config(fg=placeholder_color)

        entry.bind("<FocusIn>", on_focus_in)
        entry.bind("<FocusOut>", on_focus_out)

        print('Entry inserted successful.')

        return entry

    def show_error(self, message):
        messagebox.showerror("Error", message)

    def ClearWindows(self):
        for widget in self.winfo_children():
            widget.destroy()