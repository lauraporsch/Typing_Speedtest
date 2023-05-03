import random
from wordlist import words
from tkinter import *
import math
import time
# ---------------------------- CONSTANTS ------------------------------- #
LIGHTBLUE = "#ECF2FF"
DARKBLUE = "#3E54AC"
DARKPURPLE = "#655DBB"
LIGHTPURPLE = "#BFACE2"
user_words = []
displayed_words = []
word_list = words


# ---------------------------- CREATE LIST OF RANDOM WORDS ------------------------------- #
def random_word(event):
    """gets a random word from the wordlist and returns it as word to type"""
    global displayed_words, word_list, user_words
    if event == "<Button>":
        start_timer(60)
    # set cursor in text box
    text_box.focus()
    word_to_type = random.choice(word_list)
    # changes displayed word on Canvas
    words_canvas.itemconfig(to_type, text=word_to_type)
    displayed_words.append(word_to_type)
    # if first word is displayed, no text input to get yet
    if event == "<Button>":
        pass
    else:
        typed_word = text_box.get("1.0", END)
        user_words.append(typed_word)
    print(displayed_words)
    print(user_words)
    text_box.delete("1.0", END)
    # hinders the return key to call a line break in text box
    return "break"


# ---------------------------- CHECK TYPING SPEED ------------------------------- #
def check_typing_speed():
    """checks how many of the displayed words the user typed correctly and returns the amount"""
    global displayed_words, user_words
    correct_words = 0
    index = 0
    time.sleep(1)
    user_words = [word.strip() for word in user_words]
    for word in user_words:
        if word == displayed_words[index]:
            correct_words += 1
        index += 1
    return correct_words


# ---------------------------- START TIMER ------------------------------- #
def start_timer(count):
    """starts the one-minute countdown"""
    # turn count from 60 seconds to a minute
    count_min = math.floor(count / 60)
    # if count smaller than 60 seconds, modulus returns count, if equals 60 seconds it returns 0
    count_sec = count % 60
    # ensuring the timer always shows 2 digits on each side, even with numbers smaller than 10
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    if count_min < 10:
        count_min = f"0{count_min}"
    timer_label.config(text=f"{count_min}:{count_sec}")
    # count gets reduced by one every second (1000ms), once countdown is at zero pop up is created
    if count > 0:
        window.after(1000, start_timer, count - 1)
    else:
        show_result()


# ---------------------------- SHOW RESULT ------------------------------- #
def show_result():
    """creates pop up that shows the result of the Typing Speed Test"""
    words_canvas.itemconfig(to_type, text=" ")
    popup_x = window.winfo_rootx() + 550
    popup_y = window.winfo_rooty() + 300
    popup = Toplevel(window)
    popup.geometry(f'+{popup_x}+{popup_y}')
    popup.config(padx=40, pady=40, bg=LIGHTBLUE)
    result = check_typing_speed()
    result_label = Label(popup, text=f"Well done!\nYour speed is {result} words per minute!\nCan you go even faster?",
                         font=("Arial", 15), bg=LIGHTBLUE, fg=DARKBLUE)
    result_label.grid(column=0, row=0, columnspan=3)
    empty_space = Label(popup, text=" ")
    empty_space.grid(column=1, row=1)
    again_button = Button(popup, text="TRY AGAIN", font=("Courier", 15, "bold"), bg=DARKPURPLE, fg=LIGHTPURPLE,
                          command=lambda: restart(popup))
    again_button.grid(column=0, row=2)
    end_button = Button(popup, text="END", font=("Courier", 15, "bold"), bg=DARKPURPLE, fg=LIGHTPURPLE,
                        command=close_window)
    end_button.grid(column=2, row=2)


# ---------------------------- RESTART ------------------------------- #
def restart(popup):
    """destroys the result popup and sets the displayed and typed words to zero"""
    global displayed_words, user_words
    popup.destroy()
    displayed_words = []
    user_words = []


# ---------------------------- CLOSE WINDOW ------------------------------- #
def close_window():
    """closes the whole application"""
    window.destroy()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Typing Speed Test")
window.config(bg=LIGHTBLUE)
width = window.winfo_screenwidth()
height = window.winfo_screenheight()
window.geometry("%dx%d" % (width, height))

# ---------------------------- WIDGETS ------------------------------- #
title_label = Label(text="Typing Speed Test", font=("Courier", 50, "bold"), fg=DARKBLUE, bg=LIGHTBLUE)
title_label.grid(column=1, row=0, columnspan=2)
title_label.config(pady=20)

explanation_canvas = Canvas(width=1536, height=200, bg=LIGHTBLUE, highlightthickness=0)
explanation_canvas.create_text(768, 96, text="Welcome to the Typing Speed Test!\nLet's see how many words a minute you "
                                             "can type.\n1. Click the 'Start' Button.\n2. A word will appear above the "
                                             "Text Box.\n3.Type the word and hit 'Enter'\n4. After 1 Minute the "
                                             "Test will automatically stop.\n5. Words with Typos will not count!",
                               font=("Arial", 10), fill=DARKBLUE)
explanation_canvas.grid(column=1, row=1, columnspan=2)

words_canvas = Canvas(width=768, height=150, bg=DARKBLUE)
to_type = words_canvas.create_text(384, 75, text=" ", font=("Arial", 20, "bold"), fill=LIGHTBLUE)
words_canvas.grid(column=1, row=2, columnspan=2)

text_box = Text(width=51, height=5, font=("Arial", 20))
text_box.bind("<Return>", random_word)
text_box.grid(column=1, row=3, columnspan=2)

empty_row = Label(text="")
empty_row.grid(column=1, row=4)

start_button = Button(text="START", font=("Courier", 25, "bold"), bg=DARKPURPLE, fg=LIGHTPURPLE,
                      command=lambda: random_word(event="<Button>"))
start_button.grid(column=1, row=5)

timer_label = Label(text="00:00", font=("Courier", 30, "bold"), fg=DARKPURPLE, bg=LIGHTPURPLE)
timer_label.grid(column=2, row=5)


# keep window open
window.mainloop()
