#!/usr/bin/env python
# coding: utf-8

# In[2]:


import re as ree
import tkinter as tk
from tkinter import *
from sympy import *
from IPython.display import display, Math
x, y, z = symbols("x y z")
r=2*z/((x+y)-2)
def compare_two_strings(text1, text2):
    global x, y, first, second, simillar_intersevtions
    x = text1
    y = text2

    first = ree.sub("\s", "", x)
    second = ree.sub("\s", "", y)
    #print(first)
    first_bigrams: [str, int] = {}
    for i in range(0, len(first) - 1):
        bigram = first[i: i + 2]
        count = first_bigrams[bigram] + 1 if bigram in first_bigrams.keys() else 1
        first_bigrams[bigram] = count
    simillar_intersevtions = 0
    for i in range(0, len(second) - 1):
        bigram = second[i: i + 2]
        count = first_bigrams[bigram] if bigram in first_bigrams.keys() else 0
        if count > 0:
            simillar_intersevtions += 1

def myclick():
    global x, y, first, second, simillar_intersevtions
    text1 = e.get()
    text2 = e2.get()
    compare_two_strings(text1, text2)
    a1 = (2 * simillar_intersevtions) / ((len(first) + len(second)) - 2)
    mylabel1 = Label(root, text="the similarity between two stirngs is %s" % a1+"%\n"+"and the formula that is used is %s"%display(Math('E = '+latex(r))))
    if len(first) == 0 and len(second) == 0:
        mylabel = Label(root, text="the similarity between two stirngs is %s" % 1)
        return mylabel.pack()

    if first == second:
        mylabel2 = Label(root, text="the similarity between two stirngs is %s" % 1)
        return mylabel2.pack()

    if len(first) == 1 and len(second) == 1:
        mylabel4 = Label(root, text="the similarity between two stirngs is %s" % 1)
        return mylabel4.pack()

    mylabel1.pack()


root = Tk()
root.title("similarity calculator")
e = Entry(root, width=90, borderwidth=7)
e2 = Entry(root, width=90, borderwidth=7)
e.insert(0, "please enter the first text")
e2.insert(0, "please enter the second text")
e.pack()
e2.pack()

mybutton = Button(root, text="click me", command=myclick)
mybutton.pack()
root.mainloop()


# In[ ]:




