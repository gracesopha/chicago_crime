'''
Grace Sopha
final project for open source programming - this program will analyze the crime data and visualize it
'''
import time
from tkinter import *
from data import *
from plots import *

# mm/dd/yy format
print ("date:",time.strftime("%x"))

# create root window
root = Tk()
#disallow resizing of window
root.geometry('300x150')
root.resizable(False, False)
root.title('Chicago Crime Data')                      
  
# frame inside root window
frame = Frame(root)                 
frame.pack()

#prompt user
label = Label(frame, text='Please choose a graph to visualize:')
#add to root
label.pack()
  
#create buttons
button1 = Button(frame, text ='Top 5 Crimes', command = types)
button2 = Button(frame, text ='Location of Crimes', command=location)
button3 = Button(frame, text ='Arrests', command=arrests)
button4 = Button(frame, text ='Quit Program' , command = root.destroy)
#add to root
button1.pack() ; button2.pack() ; button3.pack() ; button4.pack()                 
  
# Tkinter event loop
root.mainloop()   