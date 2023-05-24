from tkinter import *
from colors import *


class TypingSpeedTest(Tk):
    def __init__(self):
        """creates main window for application, including title and explanation"""
        super().__init__()
        self.title("Typing Speed Test")
        self.config(bg=LIGHTBLUE)
        width = self.winfo_screenwidth()
        height = self.winfo_screenheight()
        self.geometry("%dx%d" % (width, height))
        self.title_label = Label()
        self.title_label.config(text="Typing Speed Test", font=("Courier", 50, "bold"), fg=DARKBLUE, bg=LIGHTBLUE,
                                pady=20)
        self.title_label.grid(column=1, row=0, columnspan=3)
        self.explanation = Canvas()
        self.explanation.config(width=1536, height=200, bg=LIGHTBLUE, highlightthickness=0)
        self.explanation.create_text(768, 96, text="Welcome to the Typing Speed Test!\nLet's see how many words a "
                                                   "minute you can type.\n1. Click the 'Start' Button.\n2. A word "
                                                   "will appear above the Text Box.\n3. Type the word and hit 'Enter'\n"
                                                   "4. After 1 Minute the Test will automatically stop.\n5. Words with "
                                                   "Typos will not count!", font=("Arial", 10), fill=DARKBLUE)
        self.explanation.grid(column=1, row=1, columnspan=3)

    def close_window(self):
        """closes the whole application"""
        self.destroy()
