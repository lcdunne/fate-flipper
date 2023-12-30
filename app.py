import random
import time
import tkinter as tk
from tkinter import ttk


class Colours:
    text = "#3B4252"
    window_bg = "#ECEFF4"
    alt_bg = "#D8DEE9"
    danger = "#BF616A"
    success = "#8FBCBB"


class App:
    def __init__(self):
        self.root = tk.Tk()

        # Set window icon
        self.root.geometry("200x200")
        self.root.title("Fate Flipper")

        self._setup_icon()

        self.mainframe = tk.Frame(self.root, background=Colours.window_bg)
        self.mainframe.pack(fill="both", expand=True)
        # Center all content
        self.mainframe.columnconfigure(0, weight=1)  # All available H space
        self.mainframe.rowconfigure(0, weight=1)  # All available V space
        self.mainframe.rowconfigure(1, weight=1)
        # Setup for main app content
        self.threshold = tk.IntVar(value=50)
        self._setup_label()
        self._setup_randomization_btn()
        self._setup_slider()

        style = ttk.Style()
        style.configure(
            "TButton", font=("Arial", 12), padding=(10, 5), foreground=Colours.text
        )

        self.root.mainloop()
        return

    def _setup_icon(self):
        try:
            self.root.iconbitmap(
                "./assets/vecteezy_whale-tail-symbol_6720669-1_resized.ico"
            )
        except tk._tkinter.TclError:
            try:
                self.root.iconbitmap(
                    "@./assets/vecteezy_whale-tail-symbol_6720669-1_resized.xbm"
                )
                # # Alternatively:
                # img = tk.PhotoImage(
                #     file="./assets/vecteezy_whale-tail-symbol_6720669-1_resized.gif"
                # )
                # self.root.tk.call("wm", "iconphoto", self.root._w, img)
            except tk._tkinter.TclError as e:
                print(e)

    def _setup_label(self):
        self.text = ttk.Label(
            self.mainframe,
            text="",
            # background="Colo",
            foreground=Colours.text,
            font=("Arial", 26),
        )
        self.text.grid(row=0, column=0, columnspan=2, pady=10)
        self.set_flip_value()

    def _setup_randomization_btn(self):
        self.btn_flip = ttk.Button(
            self.mainframe,
            text="Go",
            command=self.flip,
        )
        self.btn_flip.grid(row=1, column=0, pady=10, sticky="ns")

    def _setup_slider(self):
        # Slider to set the threshold
        self.threshold_slider = ttk.Scale(
            self.mainframe,
            orient="horizontal",
            from_=0,
            to=100,
            variable=self.threshold,
            command=lambda _: self.threshold_label.config(
                text=f"{self.threshold.get()}%"
            ),
        )

        # Small label for the slider
        self.threshold_label = ttk.Label(
            self.mainframe,
            text=f"{self.threshold.get()}%",
            foreground=Colours.text,
            font=("Arial", 12),
        )

        self.threshold_slider.grid(row=2, column=0, pady=10, sticky="nsew")
        self.threshold_label.grid(row=3, column=0)

    def set_flip_value(self, y=None):
        y = y or self.threshold.get() / 100
        self.text.config(
            text=f"{y:.0%}",
            background=Colours.danger
            if y >= self.threshold.get() / 100
            else Colours.success,
        )

    def flip(self):
        self.set_flip_value(random.random())


if __name__ == "__main__":
    App()
