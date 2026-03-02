'''
tkinter Basics
'''

from tkinter import *

# window = Tk() #instantiate an instance of a window
# window.geometry('600x500')
# window.title("First GUI Program")

# window.config(background='black')


# window.mainloop() #places window on computer screen. listens for events

'''
Labels
'''

# window = Tk()
# window.geometry('420x420')


# label = Label(window, 
#               text = "Hello World",  #text in the label
#               font = ('Arial', 40, 'bold'), # font in the label
#               fg = 'green', #color of the text itself plus the border (i think?)
#               bg = 'black', #color of text's highlight
#               relief=RAISED, #style of the border (e.g. RAISED, SUNKEN, etc.)
#               bd = 10, # border size
#               padx = 20, #horizontal padding
#               pady = 20) #vertical padding
# label.pack() #places label in top center of window
# # label.place(x=100,y=100) #places label more specifically in window

# window.mainloop()

'''
BUTTONS!!!
'''
import os

# window = Tk()
# window.title("Button Clicker")
# window.geometry('420x420')

# count = 0

# label = Label(window,
#               text = count)
# label.pack()
# label.config(font = ('Arial', 75))

# def click():
#   global count
#   count += 1
#   label.config(text = count)

# def clear():
#   global count
#   count = 0
#   label.config(text = count)


# button1 = Button(window, text = 'Click me!!!',)
# button1.config(command = click,
#                font=('Arial', 50),
#                fg = 'white',
#                bg = 'green',
#                activebackground='blue',
#                activeforeground='white',
#                bd = 10,
#                relief = RAISED)
#               #  state=DISABLED) #either ACTIVE or DISABLED
# button1.pack()

# button2 = Button(window, text = 'Reset')
# button2.config(command = clear,
#                font=('Arial', 50),
#                fg = 'white',
#                bg = 'red',
#                activebackground='orange',
#                activeforeground='white',
#                bd = 10,
#                relief = RAISED)
# button2.pack()

# window.mainloop()

'''
User Input
'''

window = Tk()
window.geometry('420x100')

def sub():
  username = entry.get()
  print(username)

def delete():
  entry.delete(0,END) # Deletes entire line of text

submit = Button(window,
                 text = 'submit',
                 command = sub)
submit.pack(side = RIGHT)

delete = Button(window,
                 text = 'delete',
                 command = delete)
delete.pack(side = RIGHT)


entry = Entry()
entry.config(font=('Arial', 75),
             bg='black',
             fg='#00ff00',)
            #  show='*')
# entry.insert(0, 'Spongebob')
entry.pack()


window.mainloop()
