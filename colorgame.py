import tkinter
from tkinter import messagebox
import random


colours = ['Red','Blue','Green','Pink','Black','Yellow','Orange','White','Purple','Brown']
score = 0

timeleft = 30


def Game(event):
    if timeleft ==30:
        countdown()
    nextColour()

def nextColour():

    global score
    global timeleft

    if timeleft >0:
        e.focus_set()
        if e.get().lower() == colours[1].lower():
            score += 1
        e.delete(0,tkinter.END)
        random.shuffle(colours)
        label.config(fg =str(colours[1]),text=str(colours[0]))

        scoreLabel.config(text ="score: "+str(score))

def countdown():
    global timeleft

    if timeleft > 0:
        timeleft -=1
        timeLabel.config(text ="Time Left: "+str(timeleft))
        timeLabel.after(1000,countdown)
    elif timeleft==0:
        messagebox.showinfo('score is-',score)


        
    
       
    

root = tkinter.Tk()
root.title("COLOUR GAME")
root.geometry("500x300")
instructions =tkinter.Label(root,text="Type in the colour of the words, and not the word text!",font =('Helvetica',12))
instructions.pack()

scoreLabel = tkinter.Label(root,text="press enter to start",font=('Helvetica',12))
scoreLabel.pack()

timeLabel = tkinter.Label(root,text="Time left: "+ str(timeleft), font=('Helvetica',12))
timeLabel.pack()

label =tkinter.Label(font=('Helvetica',60))
label.pack()


e = tkinter.Entry(root)

root.bind('<Return>',Game)
e.pack()
e.focus_set()
root.mainloop()














        

    
