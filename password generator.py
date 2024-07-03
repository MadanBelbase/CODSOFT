from tkinter import *
import string
import random


def generator():
   small_alphabets=string.ascii_lowercase
   capital_alphabets=string.ascii_uppercase
   numbers=string.digits
   special_charecters=string.punctuation

   all=small_alphabets+capital_alphabets+numbers+special_charecters
   password_length=int(Length_Box.get())

   if choice.get()==1:
        passwordfield.insert(0,random.sample(small_alphabets,password_length))

   if choice.get()==2:
        passwordfield.insert(0,random.sample(small_alphabets+capital_alphabets,password_length))

   if choice.get()==3:
        passwordfield.insert(0,random.sample(all,password_length))


    

root = Tk()
root.config(bg = 'aqua')
choice = IntVar()
Font = ('arial',13,'bold')
passwordLabel = Label(root,text = 'Password Generator ', font = ('times new roman',20),bg = 'aqua',fg = 'white')
passwordLabel.grid(pady=10)

weakreadioButton = Radiobutton(root,text = 'week',value = 1,variable = choice,font = Font) 
weakreadioButton.grid(pady=10)

weakreadioButton = Radiobutton(root,text = 'Medium',value = 2,variable = choice,font = Font) 
weakreadioButton.grid(pady=10)

weakreadioButton = Radiobutton(root,text = 'Strong',value = 3,variable = choice,font = Font) 
weakreadioButton.grid(pady=5)

lengthLabel = Label(root,text = 'Password Length ', font = ('times new roman',20),bg = 'aqua',fg = 'white')

Length_Box=Spinbox(root,from_ = 8,to_=18,width=8,font=Font)
Length_Box.grid(pady=5)

GenerateButton = Button(root,text = 'Generate Password',font=Font,command=generator)
GenerateButton.grid(pady =5)

passwordfield=Entry(root,width=25,bd=2,font=Font)
passwordfield.grid(pady=6)



root.mainloop()