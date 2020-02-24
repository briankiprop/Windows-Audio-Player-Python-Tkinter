import time
import tkinter
import tkinter as tk
import os
from tkinter import messagebox
# import mtTkinter as tk
from tkinter.filedialog import askdirectory

import pygame
from PIL import ImageTk, Image

root = tk.Tk()
root.geometry('300x300')
root.title('Audio Player')
root.iconbitmap(r'pics/favicon.ico')
root.maxsize(width=300, height=300)
root.config(bg='grey')

pygame.mixer.init()

listofsongs = []  # array of songs from the folder selected
count = listofsongs.count(all)


# fuction to open a folder and choose file im .mp3 format
def directorychoose():
    filename = askdirectory()
    os.chdir(filename)
    for music in os.listdir(filename):
        if music.endswith('.mp3'):
            listofsongs.append(music)
            listBox = tk.StringVar(root)
            listBox.set('Select Audio To Play')


# global variables initializations for clicks on buttons
music = 0
clicks = 0


# play function
def play():
    global clicks
    clicks += 1
    try:
        if clicks == 1:
            m = listofsongs
            pygame.mixer.music.load(m[0])
            pygame.mixer.music.play()
        elif (clicks % 2) == 0:
            pygame.mixer.music.pause()
        else:
            pygame.mixer.music.unpause()
    except IndexError:
        tk.messagebox.showinfo('Music List', 'Select a folder with Audio files')


# gets to the next song on the click of the button
def next():
    global music
    music += 1
    m = listofsongs
    if music < len(listofsongs):
        pygame.mixer.music.load(m[music])
        pygame.mixer.music.play()
    else:
        music = len(listofsongs)


# gets back one track on click
def previous():
    global music
    music -= 1
    m = listofsongs
    if music >= 0:
        pygame.mixer.music.load(m[music])
        pygame.mixer.music.play()
    else:
        music = 0


# audio spectrum label
lbl1 = tk.Label(root, text='Audio Spectrum', bg='violet', font='calibri 10').pack(pady=3)

# defining  the frame in which the ausi spectrum pic will be passed
frame = tk.Frame(root, border=0, height=200, width=300, bg='grey')
frame.pack(pady=5, padx=5)
path = 'pics/spectrum.png'
img_spectrum = ImageTk.PhotoImage(Image.open(path))
label = tk.Label(frame, image=img_spectrum, height=150).pack()

# button to implement directorychoose function
btn1 = tk.Button(root, text='Select A folder with Music', command=directorychoose).pack()

img = Image.open('pics/previous.png')
img = img.resize((50, 50), Image.ANTIALIAS)
previous_img = ImageTk.PhotoImage(img)
btn3 = tk.Button(root, text='Previous', bg='grey', image=previous_img, command=previous, border=0).pack(side='left',
                                                                                                        padx=20)

img = Image.open('pics/play.png')  # open image
img = img.resize((50, 50), Image.ANTIALIAS)  # resize the image
play_img = ImageTk.PhotoImage(img)

# implementing the play function with a button
btn2 = tk.Button(root, text='PLAY', image=play_img, command=play, bg='grey', border=0).pack(side='left', padx=20)

img = Image.open('pics/next.png')
img = img.resize((50, 50), Image.ANTIALIAS)
next_img = ImageTk.PhotoImage(img)

# the next button
btn4 = tk.Button(root, text='Next', bg='grey', image=next_img, command=next, border=0).pack(side='left', padx=20)

root.mainloop()
