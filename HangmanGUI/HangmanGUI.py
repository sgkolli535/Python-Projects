# Sumedha Kolli
# Hangman Graphical User Interface (GUI)

from tkinter import *
import random

class HangmanGUI:
    def __init__(self):
        root = Tk()
        root.title("Hangman GUI")
        root.geometry("400x575")
        self.myFrame = Frame(root)
        self.myFrame.grid()
        self.label1 = Label(self.myFrame, text="Enter a letter")
        self.label1.grid(row=0, column=0, sticky=E)
        self.label1.config(font="Arial 14 bold")
        self.textfield = Entry(self.myFrame)
        self.textfield.grid(row=0, column=1, sticky=W)
        self.textfield.focus()  # places cursor inside text box automatically
        self.textfield.config(bg="blue", fg="yellow")
        root.bind("<Return>", self.buttonClicked)  # allows user to hit return instead of hitting button
        # root.bind("<a>", self.buttonClicked)
        root.update()  # to make button click down in Mac
        self.button = Button(self.myFrame, text="Guess Letter", command=self.buttonClicked)
        self.button.grid(row=1, column=0, columnspan=2)

        self.guessedLetters = []
        self.lettersToGuessLabel = Label(self.myFrame, text=self.getLettersDisplayed())
        self.lettersToGuessLabel.grid(row=2, column=0, columnspan=2)
        self.secretWord = self.getSecretWord()
        # debug line, so dont forget to remove it
        # print(self.secretWord)
        self.displayedWordLabel = Label(self.myFrame, text=self.getDisplayedWord())
        self.displayedWordLabel.grid(row=3, column=0, columnspan=2)
        self.displayedWordLabel.config(fg="green", font="Courier 14")
        self.statusMessageLabel = Label(self.myFrame)
        self.statusMessageLabel.grid(row=4, column=0, columnspan=2)

        self.imageList = []
        self.imageList.append(PhotoImage(file="hangman0.png"))
        self.imageList.append(PhotoImage(file="hangman1.png"))
        self.imageList.append(PhotoImage(file="hangman2.png"))
        self.imageList.append(PhotoImage(file="hangman3.png"))
        self.imageList.append(PhotoImage(file="hangman4.png"))
        self.imageList.append(PhotoImage(file="hangman5.png"))
        self.imageList.append(PhotoImage(file="hangman6.png"))
        self.imageList.append(PhotoImage(file="hangman7.png"))
        self.imageLabel = Label(self.myFrame, image=self.imageList[0])
        self.imageLabel.grid(row=5, column=0, columnspan=2)
        self.imageCounter = 0

    def getLettersDisplayed(self):
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        stringToReturn = ""
        for ch in alphabet:
            if ch in self.guessedLetters:
                stringToReturn += "- "
            else:
                stringToReturn += ch + " "
        return stringToReturn

    def getSecretWord(self):
        inputFile = open("hangmanwords.txt", "r")
        secretList = []
        for word in inputFile:
            secretList.append(word.strip())
        inputFile.close()
        return random.choice(secretList)

    def getDisplayedWord(self):
        display = []
        for ch in self.secretWord:
            if ch.upper() in self.guessedLetters:
                display.append(ch.upper())
            else:
                display.append("_")
        return " ".join(display)

    def buttonClicked(self, event=None):
        # if event is None:
        #     print("The user clicked the button")
        # elif event.char == "a":
        #     print("The user hit the a key")
        # else:
        #     print("The user hit enter")
        # print("Button Clicked!")
        if self.imageCounter != 7:
            textvalue = self.textfield.get()
            self.textfield.delete(0, len(textvalue))  # clears text field after guess
            if len(textvalue) == 1:
                self.guessedLetters.append(textvalue.upper())
                self.lettersToGuessLabel.config(text=self.getLettersDisplayed())
                if textvalue.upper() in self.secretWord.upper():  # the letter user guessed is in secret word
                    self.statusMessageLabel.config(text=textvalue.upper() + " IS in the secret word.")
                    self.displayedWordLabel.config(text=self.getDisplayedWord())
                    if "_" not in self.getDisplayedWord(): # the user won
                        self.statusMessageLabel.config(text="You won! You guessed the secret word!")
                        self.button.config(state=DISABLED)
                        self.imageCounter = 7
                else: # the letter user guessed is not in secret word
                    self.statusMessageLabel.config(text=textvalue.upper() + " is NOT in the secret word.")
                    self.imageCounter += 1
                    self.imageLabel.config(image=self.imageList[self.imageCounter])
                    if self.imageCounter == 7:
                        self.statusMessageLabel.config(text="You lost! The secret word was " + self.secretWord.upper() + ".")
                        self.button.config(state=DISABLED)

def main():
    hgui = HangmanGUI()
    hgui.myFrame.mainloop()

main()
