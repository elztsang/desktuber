import tkinter as tk
from PIL import Image, ImageTk
import time
import random # I can use this to make it randomly blink.
import pynput
from pynput.keyboard import Key, Listener


class tuber():
    def __init__(self):

        self.window = tk.Tk()

        # bind events to keypresses
        self.window.bind('<KeyPress>', self.on_press)
        self.window.bind('<KeyRelease>', self.on_release)
        # placeholder image
        # I could replace the gif blink mechanism with just switching between two images.

        # self.talk = tk.PhotoImage(file='assets/talk.png')
        # self.idle = tk.PhotoImage(file='assets/idle.png')
        # self.talk_blink = tk.PhotoImage(file='assets/talk_blink.png')
        idle = Image.open('assets/idle.png')
        talk = Image.open('assets/talk.png')
        blink = Image.open('assets/blink.png')

        resized_idle = idle.resize((128,128))
        resized_talk = talk.resize((128,128))
        resized_blink = blink.resize((128,128))


        self.idle = ImageTk.PhotoImage(resized_idle)
        self.talk = ImageTk.PhotoImage(resized_talk)
        self.blink = ImageTk.PhotoImage(resized_blink)

        self.img = self.idle

        # timestamp to check whether to advance frame
        self.timestamp = time.time()

        # set focushighlight to black when the window does not have focus
        self.window.config(highlightbackground='green')

        # make window frameless
        self.window.overrideredirect(True)

        # make window draw over all others
        self.window.attributes('-topmost', True)

        # turn black into transparency
        self.window.wm_attributes('-transparentcolor', 'green')

        # create a label as a container for our image
        self.label = tk.Label(self.window, bd=0, bg='green')

        # create a window of size 128x128 pixels, at coordinates 0,0
        self.window.geometry('128x128+0+0')
        # self.img = ImageTk.PhotoImage(self.img.resize(128, 128))

        # add the image to our label
        self.label.configure(image=self.img)

        # give window to geometry manager (so it will appear)
        self.label.pack()

        self.window.resizable(True, True)

        # run self.update() after 0ms when mainloop starts
        self.window.after(0, self.update)
        self.window.mainloop()

    def update(self):

        # create a random interval for blinking
        newTime = random.randrange(3, 5)

        # move right by one pixel
        # self.x += 1
        print("update called")

        # advance frame if 50ms have passed
        if time.time() > self.timestamp + newTime:
            print("blink1 ", time.time())
            # self.timestamp = time.time()
            # advance the frame by one, wrap back to 0 at the end
            # self.frame_index = (self.frame_index + 1) % len(self.blink)
            # self.img = self.blink[self.frame_index]
            self.img = self.blink
        if time.time() > self.timestamp + newTime + 0.15:
            print("blink2 ", time.time())
            self.timestamp = time.time()
            # advance the frame by one, wrap back to 0 at the end
            # self.frame_index = (self.frame_index + 1) % len(self.blink)
            # self.img = self.blink[self.frame_index]
            self.img = self.idle

        # self.img = self.blink[0]

        # create the window
        self.window.geometry('128x128+0+0')
        # add the image to our label
        self.label.configure(image=self.img)
        # give window to geometry manager (so it will appear)
        self.label.pack()

        # call update again after 10ms
        self.window.after(100, self.update) #original value was 10

    def on_press(self, event):
        # if key.char.isalpha() or key.char.isdigit():
        #     print("KEY PRESSED!!")
        self.img = self.talk

    def on_release(self, event):
        self.img = self.idle

    # with Listener(
    #     on_pres=on_press,
    #     on_release=on_release) as listener:
    #     print("listener initialized")
    #     listener.join()

tuber()