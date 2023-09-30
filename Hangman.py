# Tkinter provides classes which allow the display, positioning and control of widgets.
# Toplevel widgets are Tk and Toplevel. Other widgets are Frame, Label, Entry, Text, Canvas,
# Button, Radiobutton, Checkbutton, Scale, Listbox, Scrollbar, OptionMenu, Spinbox LabelFrame and PanedWindow.

# Tkinter is the de facto way in Python to create Graphical User interfaces (GUIs)

# ---------------------------------------------------------------------------------------------

# Import necessary modules from the tkinter library
from tkinter import *
from tkinter import messagebox
from string import ascii_uppercase
import random

# Create the main window
window = Tk()
window.title("Hangman-GUESS CITIES NAME")

# List of words to guess (cities' names)
word_list = [
    "MUMBAI",
    "DELHI",
    "BANGLORE",
    "HYDRABAD",
    "AHMEDABAD",
    "CHENNAI",
    "KOLKATA",
    "SURAT",
    "PUNE",
    "JAIPUR",
    "AMRITSAR",
    "ALLAHABAD",
    "RANCHI",
    "LUCKNOW",
    "KANPUR",
    "NAGPUR",
    "INDORE",
    "THANE",
    "BHOPAL",
    "PATNA",
    "GHAZIABAD",
    "AGRA",
    "FARIDABAD",
    "MEERUT",
    "RAJKOT",
    "VARANASI",
    "SRINAGAR",
    "RAIPUR",
    "KOTA",
    "JHANSI",
]

# ---------------------------------------------------------------------------------------------

# PhotoImage(file)
# file − This represents the name of the image file.

# ---------------------------------------------------------------------------------------------

# List of images to display as the game progresses (hangman images)
photos = [
    PhotoImage(file="images/hang0.png"),
    PhotoImage(file="images/hang1.png"),
    PhotoImage(file="images/hang2.png"),
    PhotoImage(file="images/hang3.png"),
    PhotoImage(file="images/hang4.png"),
    PhotoImage(file="images/hang5.png"),
    PhotoImage(file="images/hang6.png"),
    PhotoImage(file="images/hang7.png"),
    PhotoImage(file="images/hang8.png"),
    PhotoImage(file="images/hang9.png"),
    PhotoImage(file="images/hang10.png"),
    PhotoImage(file="images/hang11.png"),
]


# Function to start a new game
def newGame():
    global the_word_withSpaces
    global numberOfGuesses
    numberOfGuesses = 0

    # Choose a random word from the word_list
    the_word = random.choice(word_list)
    the_word_withSpaces = " ".join(the_word)  # Separate letters with spaces
    lblWord.set(" ".join("_" * len(the_word)))  # Display underscores for letters
    print(the_word_withSpaces)
    print(the_word)


# Function to handle user guesses
def guess(letter):
    global numberOfGuesses
    if numberOfGuesses < 11:
        txt = list(the_word_withSpaces)
        guessed = list(lblWord.get())

        # Check if the guessed letter is in the word
        if the_word_withSpaces.count(letter) > 0:
            for c in range(len(txt)):
                if txt[c] == letter:
                    guessed[c] = letter
                lblWord.set("".join(guessed))  # Update displayed word

                if lblWord.get() == the_word_withSpaces:
                    messagebox.showinfo("Hangman", "You guessed it!")  # User wins
        else:
            numberOfGuesses += 1
            imgLabel.config(image=photos[numberOfGuesses])  # Update hangman image

            # If user reaches maximum number of guesses (11), show a game over message
            if numberOfGuesses == 11:
                messagebox.showwarning("Hangman", "Game Over")


# ---------------------------------------------------------------------------------------------

# messagebox.FunctionName(title, message, options)
# FunctionName − This represents the name of the messagebox function like showinfo, showwarning, showerror, etc.
# title − This represents the title of the messagebox.
# message − This represents the message to be displayed.
# options − This represents the options like default, icon, parent, etc.

# ---------------------------------------------------------------------------------------------

# Label(master, textvariable, font, width)
# master − This represents the parent window.
# textvariable − The text to be displayed on the label.
# font − The font type of the text.
# width − The width of the label.

# ---------------------------------------------------------------------------------------------

# Create a label to display hangman images
imgLabel = Label(window)
imgLabel.grid(row=0, column=0, columnspan=3, padx=10, pady=40)

# Create a label to display the current word with underscores for missing letters
lblWord = StringVar()
Label(window, textvariable=lblWord, font=("consolas 24 bold")).grid(
    row=0, column=3, columnspan=6, padx=10
)

# ---------------------------------------------------------------------------------------------

# Button(master, text, command, font, width)
# master − This represents the parent window.
# text − The text to be displayed on the button.
# command − The function to be called when the button is clicked.
# font − The font type of the text.
# width − The width of the button.
# grid(row, column)

# ---------------------------------------------------------------------------------------------

# Create buttons for each letter of the alphabet
n = 0
for c in ascii_uppercase:
    Button(
        window, text=c, command=lambda c=c: guess(c), font=("Helvetica 18"), width=4
    ).grid(row=1 + n // 9, column=n % 9)
    n += 1

# Create a button to start a new game
Button(
    window, text="New\nGame", command=lambda: newGame(), font=("Helvetica 10 bold")
).grid(row=3, column=8)

# Start a new game when the program starts
newGame()

# Run the event loop (keep displaying the window)
window.mainloop()
