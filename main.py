from tkinter import *
import tkinter.messagebox as box
import random

def arithmetic():
  import tkinter as tk

  def evaluation():
    aa = integera.get()
    bb = integerb.get()

    if aa == '':
      sollab["text"] = 'Fill out Integer A.'

    elif bb == '':
      sollab["text"] = 'Fill out Integer B.'

    elif aa == "0":
      sollab["text"] = 'Enter in anything but a zero.'

    elif bb == "0":
      sollab["text"] = 'Enter in anything but a zero.'
    
    else:
      a = float(aa)
      b = float(bb)

      div = a / b
      divsol = f"Division : {a} ÷ {b} = {div}\n"

      sub = a - b
      subsol = f"Subtraction : {a} - {b} = {sub}\n"

      mult = a * b
      multsol = f"Multiplication : {a} * {b} = {mult}\n"

      add = a + b
      addsol = f"Addition : {a} + {b} = {add}\n"

      exp = a ** b
      expsol = f"Exponential : {a} ** {b} = {exp}\n"

      sollab["text"] = f'{addsol} {subsol} {multsol} {divsol} {expsol}'

  mathwin = Tk()

  mathwin.title("Arithmetic Evaluation!")

  aritmeticentry = Frame(master=mathwin)

  integera = Entry(master=aritmeticentry, width=10)
  integerb = Entry(master=aritmeticentry, width=10)

  alabel = Label(master=aritmeticentry, text="Integer A = ")
  blabel = Label(master=aritmeticentry, text="Integer B = ")

  integera.grid(row=0, column=1, sticky="e")
  integerb.grid(row=1, column=1, sticky="e")

  alabel.grid(row=0, column=0, sticky="w")
  blabel.grid(row=1, column=0, sticky="w")

  evalbut = Button(master=mathwin, text="Evaluate!", command=evaluation)
  sollab = Label(master=mathwin)

  aritmeticentry.grid(row=0, column=0, padx=10)
  evalbut.grid(row=0, column=1, pady=10)
  sollab.grid(row=2, column=0)

  mathwin.mainloop()

arithmetic()
