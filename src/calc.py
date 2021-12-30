import tkinter as tk

class Calc():
    def __init__(self) -> None:
        pass
            
    #Starting defining all the functions that will be inserted as list element in the main.py
    def one(self):
        return 1

    def two(self):
        return 2
    
    def three(self):
        return 3

    def four(self):
        return 4
    
    def five(self):
        return 5

    def six(self):
        return 6

    def seven(self):
        return 7

    def eight(self):
        return 8

    def nine(self):
        return 9

    def zero(self):
        return 0

    def sum(self, num1, num2):
        return num1+num2

    def sub(self, num1, num2):
        return num1-num2

    def mul(self, num1, num2):
        return num1*num2

    def div(self, num1, num2):
        try:
            return num1/num2
        except ZeroDivisionError:
            return "NaN"