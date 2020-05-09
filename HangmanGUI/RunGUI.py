# Sumedha Kolli

from tkinter import *

class RunGUI:
    def __init__(self):
        root = Tk()
        root.title("Sumi's Bistro")
        root.geometry("500x575")
        self.myFrame = Frame(root)
        self.myFrame.grid()
        self.label1 = Label(self.myFrame, text="Choose a Menu Option")
        self.label1.grid(row=0, column=0, sticky=E)
        self.textfield = Entry(self.myFrame)
        self.textfield.grid(row=0, column=1, sticky=W)
        root.update()
        self.button = Button(self.myFrame, text="Enter")# , # command=self.buttonClicked)
        self.button.grid(row=1, column=0, columnspan=2)

def main():
    rGUI = RunGUI()
    rGUI.myFrame.mainloop()


main()
