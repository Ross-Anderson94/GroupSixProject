from tkinter import *
import pygame
from pygame import *
import os

master = Tk()
master.geometry("500x500")
master.configure(background='red')


def playSong():
    mixer.music.play()


def pauseSong():
    mixer.music.pause()


def resumeSong():
    mixer.music.resume()


def stopSong():
    mixer.music.stop()


def musicPlayer():
    newWindow = Toplevel(master)
    newWindow.geometry("200x200")


play = Button(master, text="play")
play.config(font=('arial', 20), bg="blue", fg="white")
play.grid(row=1, column=0)

pause = Button(master, text="pause")
pause.config(font=('arial', 20), bg="blue", fg="white")
pause.grid(row=1, column=1)

stop = Button(master, text="resume")
stop.config(font=('arial', 20), bg="blue", fg="white")
stop.grid(row=1, column=2)

stop = Button(master, text="stop")
stop.config(font=('arial', 20), bg="blue", fg="white")
stop.grid(row=1, column=3)

mainloop()
