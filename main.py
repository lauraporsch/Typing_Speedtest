import math
from tkinter import *
from UI import TypingSpeedTest
from word_widgets import Widgets
from colors import *


# ---------------------------- FUNCTIONS ------------------------------- #
def start(event):
    """triggers the start of the test by calling the function widgets.show_word and start_timer"""
    widgets.show_word('<Button>')
    start_timer(60)


def start_timer(count):
    """starts the countdown with the set amount 'count', while timer is running, refreshes window every second to create
    impression of a running countdown"""
    # turn count from 60 seconds to a minute
    count_min = math.floor(count / 60)
    # if count smaller than 60 seconds, modulus returns count, if equals 60 seconds it returns 0
    count_sec = count % 60
    # ensuring the timer always shows 2 digits on each side, even with numbers smaller than 10
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    if count_min < 10:
        count_min = f"0{count_min}"
    Timer.config(text=f"{count_min}:{count_sec}")
    # count gets reduced by one every second (1000ms), once countdown is at zero pop up is created
    if count > 0:
        window.after(1000, start_timer, count - 1)
    else:
        create_popup()


def create_popup():
    """creates a popup that shows the result of the test and gives the option to either restart or end the program"""
    popup_x = window.winfo_rootx() + 550
    popup_y = window.winfo_rooty() + 300
    popup = Toplevel(window)
    popup.geometry(f'+{popup_x}+{popup_y}')
    popup.config(padx=40, pady=40, bg=LIGHTBLUE)
    result_text = widgets.show_result()
    result_label = Label(popup, text=result_text, font=("Arial", 15), bg=LIGHTBLUE, fg=DARKBLUE)
    result_label.grid(column=0, row=0, columnspan=3)
    empty_space = Label(popup, text=" ")
    empty_space.grid(column=1, row=1)
    again_button = Button(popup, text="TRY AGAIN", font=("Courier", 15, "bold"), bg=DARKPURPLE, fg=LIGHTPURPLE,
                          command=lambda: restart(popup))
    again_button.grid(column=0, row=2)
    end_button = Button(popup, text="END", font=("Courier", 15, "bold"), bg=DARKPURPLE, fg=LIGHTPURPLE,
                        command=window.close_window)
    end_button.grid(column=2, row=2)


def restart(popup):
    """destroys the result popup and sets the displayed and typed words to zero to restart the program"""
    widgets.restart()
    popup.destroy()
    return "break"


# ---------------------------- UI SETUP ------------------------------- #
window = TypingSpeedTest()
widgets = Widgets()
StartButton = Button()
StartButton.config(text="START", font=("Courier", 25, "bold"), bg=DARKPURPLE, fg=LIGHTPURPLE,
                   command=lambda: start(event='<Button>'))

StartButton.grid(column=1, row=5)
Timer = Label()
Timer.config(text="00:00", font=("Courier", 30, "bold"), fg=DARKPURPLE, bg=LIGHTPURPLE)
Timer.grid(column=3, row=5)

empty_row = Label(text="")
empty_row.grid(column=1, row=4)

# keep window open
window.mainloop()
