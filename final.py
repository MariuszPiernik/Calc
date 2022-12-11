from decimal import Clamped
import tkinter as tk

class Calculator:
    def _init_(self,win):
        self.equationStrVar = tk.StringVar()
        self.expressionStr = ""
        self.calcKeyboard = [
            ["7","8","9","+"],
            ["4","5","6","-"],
            ["1","2","3","*"],
            ["0","Clear","=","/"]

        ]
        self.prepareGui(win)
    def prepareGui(self,win):
        win.geometry("260x130")
        self.expressionField = tk.Entry(window, textvariable=self.equationStrVar)
        self.expressionField.grid(columnspan=4, ipadx=60)


