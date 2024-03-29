from tkinter import *
from PIL import Image, ImageTk
import os
from tkinter import filedialog
import time
from mutagen.mp3 import MP3
import tkinter.messagebox
from pygame import mixer
mixer.init()

class musicplayer:
    def __init__(self, Tk):
        self.root = Tk
        self.root.title("Music Player")
        self.root.geometry('600x600')
        self.root.configure(background='white')

        # Function to open file
        def OpenFile():
            global filename
            filename = filedialog.askopenfilename()

        # Menu section
        self.menubar = Menu(self.root)
        self.root.configure(menu=self.menubar)
     
        # Submenu
        self.submenu = Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label='File', menu=self.submenu)
        self.submenu.add_command(label='Open', command=OpenFile)
        self.submenu.add_command(label='Save')
        self.submenu.add_command(label='Save As')
        self.submenu.add_command(label='Exit', command=self.root.destroy)
        
        # For Message
        def About():
            tkinter.messagebox.showinfo('About Us', 'Music Player Created By Jagruti')

        self.submenu1 = Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label='Edit', menu=self.submenu1)
        self.submenu1.add_command(label='About', command=About)
        
        # Adding label
        self.label = Label(text="Let's make it", bg='black', fg='white', font=22)
        self.label.place(x=50, y=20)

        def songinfo():
            self.label['text'] = 'Current Music :-' + os.path.basename(filename)
            
        # Music Image
        self.photo = ImageTk.PhotoImage(file='istockphoto-1431567498-612x612.jpg')
        photo = Label(self.root, image=self.photo, bg='white')
        photo.place(x=50, y=100)

        # Label
        self.label1 = Label(self.root, text='Lets play it.', bg='black', fg='white', font=20)
        self.label1.pack(side=BOTTOM, fill=X)

        # Function to play music
        def playmusic():
            try:
                paused
            except NameError:
                try:
                    mixer.music.load(filename)
                    mixer.music.play()
                    self.label1['text'] = 'Music_Playing...'
                    songinfo()
                    length_bar()
                except:
                    tkinter.messagebox.showerror('Error', 'File not found, please find again')
            else:
                mixer.music.unpause()
                self.label1['text'] = 'Music_Playing...'

        # Function to update song length
        def length_bar():
            current_time = mixer.music.get_pos() / 1000
            convert_current_time = time.strftime('%M:%S', time.gmtime(current_time))
            song_mut = MP3(filename)
            song_mut_length = song_mut.info.length
            convert_song_mut_length = time.strftime('%M:%S', time.gmtime(song_mut_length))
            self.lengthbar.config(text=f'Total_Length:-{convert_current_time}/{convert_song_mut_length}')
            self.lengthbar.after(1000, length_bar)

        # Label for song length
        self.lengthbar = Label(self.root, text='Total_Length:-00:00', font=20)
        self.lengthbar.place(x=70, y=527)

        # Play Button Image
        self.photo_button1 = ImageTk.PhotoImage(file='play_img.jpg')
        photo_button1 = Button(self.root, image=self.photo_button1, bd=0, bg='white', command=playmusic, height=120, width=120)
        photo_button1.place(x=50, y=595)

        # Function for pause button
        def pausemusic():
            global mixer
            paused = TRUE
            mixer.music.pause()
            self.label1['text'] = 'Pause_Stopped'

        # Making Pause Button
        self.photo_button2 = ImageTk.PhotoImage(file='pause_img.jpg')
        photo_button2 = Button(self.root, image=self.photo_button2, bd=0, bg='white', command=pausemusic, height=110, width=110)
        photo_button2.place(x=210, y=600)

        # Stop_button
        def stopmusic():
            mixer.music.stop()
            self.label1['text'] = 'Music_Stopped'

        # Making Stop Button
        self.photo_button3 = ImageTk.PhotoImage(file='stop_img.png')
        photo_button3 = Button(self.root, image=self.photo_button3, bd=0, bg='white', command=stopmusic, height=110, width=110)
        photo_button3.place(x=380, y=600)

        # Mute
        def mute():
            self.scale.set(0)
            self.mute = ImageTk.PhotoImage(file='mute2_img.png')
            mute_button = Button(self.root, image=self.mute, command=unmute, bd=0, bg='white', height=30, width=30)
            mute_button.place(x=600, y=700)
            self.label1['text'] = 'Music_mute'

        # Unmute
        def unmute():
            self.scale.set(25)
            self.volimg = ImageTk.PhotoImage(file='volume_img.png')
            volimg = Button(self.root, image=self.volimg, command=mute, bg='white', bd=0, height=30, width=30)
            volimg.place(x=600, y=700)

        # Image of Volume
        self.volimg = ImageTk.PhotoImage(file='volume_img.png')
        volimg = Button(self.root, image=self.volimg, command=mute, bg='white', bd=0, height=30, width=30)
        volimg.place(x=600, y=700)

        # Function for volume bar
        def volume(vol):
            volume = int(vol) / 100
            mixer.music.set_volume(volume)

        # Volume Bar
        self.scale = Scale(self.root, from_=0, to=100, orient='horizontal', bg='grey', length=120, command=volume)
        self.scale.set(25)
        self.scale.place(x=650, y=700)

root = Tk()
obj = musicplayer(root)
root.mainloop()
