# PYCALCULATOR
### by _Luca Maria Incarnato_

## Description
The following project is my version of the classic calculator, built with python and its GUI package Tkinter. This is not a scientific calculator, it only execute the basic operations (+, -, *, /) but it can be solved complex expressions with multiple levels of parenthesis. 

## Tools
The strenght of this calculator is in the method responsable of the equation solving: eval(). This method overcame the hardest problem found coding the calculator, i.e. the transcription from string (the buttons name) to integer of the values and the assignment of the operators. The eval() method accepts a string, this means that it is not necessary the transcription, and automatically assigns the operators to the numbers. 

## Killer feature
The killer feature of this calculator is not its UI, that is really basic, but the ability to save in a txt file the expression just solved, using the function solve() and the context manager. In the repository the file test.txt shows some test made on the calculator in wich can be seen all the features of the eval() function: the negative numbers, the floating point, the division by zero exception ...