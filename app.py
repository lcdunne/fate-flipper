import random
import tkinter as tk
from tkinter import ttk
import time


class Colours:
    text = "#3B4252"
    window_bg = "#ECEFF4"
    alt_bg = "#D8DEE9"


class App:
    def __init__(self):
        self.root = tk.Tk()

        # Set window icon
        self.root.geometry("350x200")
        self.root.title("Fate Flipper")
        self.root.iconbitmap("assets/vecteezy_whale-tail-symbol_6720669-1_resized.ico")

        # Widgets inside frame
        self.mainframe = tk.Frame(self.root, background=Colours.window_bg)
        self.mainframe.pack(fill="both", expand=True)

        self.text = ttk.Label(
            self.mainframe,
            text="Flip for fate",
            # background="Colo",
            foreground=Colours.text,
            font=("Arial", 26),
        )
        self.text.grid(row=0, column=0, columnspan=2, pady=10)
        self.btn_flip = ttk.Button(
            self.mainframe,
            text="go",
            command=self.flip,
        )
        self.btn_flip.grid(row=1, column=0, pady=10, sticky="ns")

        # Center all content
        self.mainframe.columnconfigure(0, weight=1)  # All available H space
        self.mainframe.rowconfigure(0, weight=1)  # All available V space

        # Increase the vertical height of the button
        self.mainframe.rowconfigure(1, weight=1)

        # Style the button
        style = ttk.Style()
        style.configure(
            "TButton", font=("Arial", 12), padding=(10, 5), foreground=Colours.text
        )

        self.root.mainloop()
        return

    def flip(self):
        self.text.config(text=f"{random.random():.0%}")


if __name__ == "__main__":
    App()
