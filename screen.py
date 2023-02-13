# from PIL import Image, ImageTk
# from tkinter import Tk, BOTH
# from tkinter.ttk import Frame, Label, Style
import os 
import tkinter as tk
from tkinter import *
from PIL import ImageTk,Image
import pyttsx3
def text_to_speech(user_text):
    engine = pyttsx3.init()
    engine.say(user_text)
    engine.runAndWait()

# print(1)
text_to_speech('Authentication Successful!')
text_to_speech('Welcome!')
text_to_speech('Please browse through your options..')
# print(2)
# text_to_speech('Welcome')

def quit(*args):
    root.destroy()

root = Tk()
root.attributes("-fullscreen", True)
root.configure(background='black')
root.bind("<Escape>", quit)
root.bind("x", quit)

titl=Label(root,text="Smart College!!", bd=20, bg="black", fg="green", 
	font=('arial', 48),relief=RIDGE).pack(side=TOP, fill=X)
a=Label(root,text="Welcome to the Facial Recognition", bg="black", fg="yellow", 
	font=("arial", 56)).pack()
a=Label(root,text="Attendance System", bg="black", fg="yellow", 
	font=("arial", 56)).pack()

ri = Image.open("face_registration.png")
r = ImageTk.PhotoImage(ri)
label1 = Label(root, image=r)
label1.image = r
label1.place(x=180, y=300)

ai = Image.open("face_login.png")
a = ImageTk.PhotoImage(ai)
label2 = Label(root, image=a)
label2.image = a
label2.place(x=980, y=300)
