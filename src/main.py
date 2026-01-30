import tkinter as tk
from PIL import Image, ImageTk
import time
import random # I can use this to make it randomly blink.
import pynput
from pynput import keyboard


class tuber():
    def __init__(self):

        self.window = tk.Tk()

        # bind events to keypresses
        self.window.bind('<KeyPress>', self.on_press)
        self.window.bind('<KeyRelease>', self.on_release)
        self.window.bind("<ButtonPress-1>", self.start_move)
        self.window.bind('<B1-Motion>', self.move_window)

        listener = keyboard.Listener(
            on_press=self.on_press, on_release=self.on_release)
        listener.start()
        # placeholder image
        # I could replace the gif blink mechanism with just switching between two images.

        # self.talk = tk.PhotoImage(file='assets/talk.png')
        # self.idle = tk.PhotoImage(file='assets/idle.png')
        # self.talk_blink = tk.PhotoImage(file='assets/talk_blink.png')
        idle = Image.open('assets/idle.png')
        talk = Image.open('assets/talk.png')
        blink = Image.open('assets/blink.png')
        talk_blink = Image.open('assets/talk_blink.png')

        resized_idle = idle.resize((256,256))
        resized_talk = talk.resize((256,256))
        resized_blink = blink.resize((256,256))
        resized_talk_blink = talk_blink.resize((256,256))


        self.idle = ImageTk.PhotoImage(resized_idle)
        self.talk = ImageTk.PhotoImage(resized_talk)
        self.blink = ImageTk.PhotoImage(resized_blink)
        self.talk_blink = ImageTk.PhotoImage(resized_talk_blink)

        self.isTalking = False

        self.img = self.idle

        # timestamp to check whether to advance frame
        self.timestamp = time.time()

        # set focushighlight to black when the window does not have focus
        # self.window.config(highlightbackground='white')

        # make window frameless
        self.window.overrideredirect(True)

        # make window draw over all others
        self.window.attributes('-topmost', True)

        # turn black into transparency
        self.window.wm_attributes('-transparentcolor', 'gray')
        # self.window.wm_attributes('-transparentcolor', '#2a1863')

        self.window.overrideredirect(True)

        # create a label as a container for our image
        self.label = tk.Label(self.window, bd=0, bg='gray')

        # create a window of size 256x256 pixels, at coordinates 0,0
        self.window.geometry('256x256+0+0')
        # self.img = ImageTk.PhotoImage(self.img.resize(256, 256))

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

        # print("update called")

        # advance frame if 50ms have passed
        if time.time() > self.timestamp + newTime:
            # print("blink1 ", time.time())
            # self.timestamp = time.time()
            # advance the frame by one, wrap back to 0 at the end
            # self.frame_index = (self.frame_index + 1) % len(self.blink)
            # self.img = self.blink[self.frame_index]
            if(self.isTalking == True):
                print("============= talk blink =============")
                self.img = self.talk_blink
            else:
                self.img = self.blink
        if time.time() > self.timestamp + newTime + 0.2: # might need to do some arithmetic/threshold stuff here to make the blink more "stable"
            # print("blink2 ", time.time())
            self.timestamp = time.time()
            # advance the frame by one, wrap back to 0 at the end
            # self.frame_index = (self.frame_index + 1) % len(self.blink)
            # self.img = self.blink[self.frame_index]
            if(self.isTalking == True):
                self.img = self.talk
            else:
                self.img = self.idle

        # self.img = self.blink[0]

        # create the window
        self.window.geometry('256x256')
        # add the image to our label
        self.label.configure(image=self.img)
        # give window to geometry manager (so it will appear)
        self.label.pack()

        # call update again after 10ms
        self.window.after(50, self.update) #original value was 10


    # keyboard events
    def on_press(self, event):
        # if key.char.isalpha() or key.char.isdigit():
        #     print("KEY PRESSED!!")
        self.isTalking = True
        self.img = self.talk

    def on_release(self, event):
        self.isTalking = False
        self.img = self.idle


    # window movement events
    def start_move(self, event):
        global lastx, lasty
        lastx = event.x_root
        lasty = event.y_root

    def move_window(self, event):
        global lastx, lasty
        deltax = event.x_root - lastx
        deltay = event.y_root - lasty
        x = self.window.winfo_x() + deltax
        y = self.window.winfo_y() + deltay
        self.window.geometry("+%s+%s" % (x, y))
        lastx = event.x_root
        lasty = event.y_root

tuber()