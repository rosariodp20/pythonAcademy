from tkinter import *
from tkinter import messagebox

tkWindow = Tk()  
tkWindow.geometry('400x150')  
tkWindow.title('PythonExamples.org - Tkinter Example')

def click_me():  
    messagebox.showinfo('Message', 'You clicked the Submit button!')

button = Button(tkWindow,
	text = 'Submit',
	command = click_me())  
button.pack()  
  
tkWindow.mainloop()