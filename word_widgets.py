from tkinter import *
import random
from wordlist import words
from colors import *


class Widgets:
    def __init__(self):
        """creates widgets words(Canvas), start(Button), text(Text) and high_score(Label)"""
        self.words = Canvas()
        self.words.config(width=768, height=150, bg=DARKBLUE)
        self.to_type = self.words.create_text(384, 75, text=" ", font=("Arial", 20, "bold"), fill=LIGHTBLUE)
        self.words.grid(column=1, row=2, columnspan=3)

        self.word_list = words
        self.displayed_words = []
        self.user_words = []
        self.typos = []

        self.text = Text()
        self.text.config(width=51, height=5, font=("Arial", 20))
        self.text.bind("<Return>", self.show_word)
        self.text.grid(column=1, row=3, columnspan=3)

        self.high_score = Label()
        with open("high_score.txt") as data:
            self.score = int(data.read())
        self.high_score.config(text=f"High Score: {self.score} wpm", font=("Courier", 25, "bold"), bg=LIGHTBLUE,
                               fg=DARKBLUE)
        self.high_score.grid(column=2, row=5)

    def random_word(self):
        """gets a random word from the wordlist and returns it as word_to_type"""
        word_to_type = random.choice(self.word_list)
        if word_to_type in self.displayed_words:
            word_to_type = random.choice(self.word_list)
        return word_to_type

    def show_word(self, event):
        """changes the word that is shown on the WordsCanvas, saves the user input into a list called 'user words' and
        deletes the input after Return Button is pressed"""
        word_to_type = self.random_word()
        self.words.itemconfig(self.to_type, text=word_to_type)
        self.displayed_words.append(word_to_type)
        self.text.focus()
        if event == "<Button>":
            pass
        elif event.keysym:
            typed_word = self.text.get("1.0", END).lower()
            self.user_words.append(typed_word)
            self.text.delete("1.0", END)
        # hinders the return key to call a line break in text box
        return "break"

    def check_typing_speed(self):
        """checks how many of the displayed words the user typed correctly and returns the amount"""
        correct_words = 0
        index = 0
        user_words = [word.strip() for word in self.user_words]
        for word in user_words:
            if word == self.displayed_words[index]:
                correct_words += 1
            else:
                self.typos.append(self.displayed_words[index])
            index += 1
        if correct_words > self.score:
            self.score = correct_words
            with open("high_score.txt", mode="w") as file:
                file.write(str(correct_words))
            self.high_score.config(text=f"High Score: {self.score} wpm")
        return correct_words

    def show_result(self):
        """calls the function check_typing_speed to get result of test, checks for typos, creates a text that is used
        in the result popup"""
        result = self.check_typing_speed()
        wrong_words = ""
        for word in self.typos:
            # wrong_words += f"{word}  "
            if self.typos.index(word) == len(self.typos)-1:
                wrong_words += f"{word}"
            else:
                wrong_words += f"{word}, "
        if self.typos:
            if len(self.typos) == 1:
                result_text = f"Well done!\nYour speed is {result} words per minute!\nYou misspelled the word: " \
                              f"{wrong_words}.\nCan you go even faster?"
            else:
                result_text = f"Well done!\nYour speed is {result} words per minute!\nYou misspelled " \
                              f"{len(self.typos)} words: {wrong_words}.\nCan you go even faster?"
        else:
            result_text = f"Well done!\nYour speed is {result} words per minute!\nYou spelled all words correctly.\n" \
                           f"Can you go even faster?"
        return result_text

    def restart(self):
        """deletes the word to type, clears the text box, sets displayed_words, user_words and typos back to zero, to
        restart the program"""
        self.words.itemconfig(self.to_type, text=" ")
        self.text.delete("1.0", END)
        self.displayed_words = []
        self.user_words = []
        self.typos = []
