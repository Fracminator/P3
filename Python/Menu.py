from Scene import Scene
import tkinter as tk
from tkinter import *
import cv2
from Exercise1 import Exercise1
from Exercise2 import Exercise2
from win32 import win32gui


class Menu(Scene):

    def __init__(self, sceneManager, camera):
        super().__init__(sceneManager, camera)
        self.camera = camera
        self.width = 1280
        self.height = 720
        self.root = tk.Tk()
        self.root.geometry("+0+0")
        self.canvas = Canvas(self.root, height=self.height, width=self.width, bg="white")
        self.img = PhotoImage(file="exe1.png")
        self.img2 = PhotoImage(file="exe2.png")
        self.image1x = 740
        self.image1y = 260
        self.image2x = 270
        self.image2y = 225
        self.setupScene()
        self.image1height = 425
        self.image1width = 380
        self.image2height = 467
        self.image2width = 246
        self.xdiff1 = self.image1width / 2
        self.ydiff1 = self.image1height / 2
        self.xdiff2 = self.image2width / 2
        self.ydiff2 = self.image2height / 2
        self.ptx = self.image1x + (self.image1width / 2)
        self.pty = self.image1y + (self.image1height / 2)
        self.ptx1 = self.image2x + (self.image2width / 2)
        self.pty1 = self.image2y + (self.image2height / 2)
        self.radius = 30
        self.xscore = 0
        self.yscore = 0
        self.scorethreshold = 50

    def setupScene(self):
        self.canvas.pack()
        label1 = Label(self.root, text="Welcome to our shoulder rehabilitation program!", bg="white", font=("times", 20))
        label1.place(x=400, y=40)
        label2 = Label(self.root, text="Please select an exercise, by moving your hand:", bg="white", font=("times", 20))
        label2.place(x=400, y=75)
        self.canvas.create_image(self.image1x, self.image1y, anchor=NW, image=self.img)
        self.canvas.create_image(self.image2x, self.image2y, anchor=NW, image=self.img2)
        self.circle = self.canvas.create_oval(0, 0, 30, 30)

    # Overrides superclass update() function
    def update(self):
        # Can insert custom code here
        frame = self.camera.getFrame()
        framehsv = self.camera.convertToHSV(frame)
        framemask = self.camera.Masking(framehsv)
        framehsvmedian = self.camera.medianBlur(framemask, 5)
        framehsvmedianerosion = self.camera.erosion(framehsvmedian, 5)
        # cv2.imshow('hsv', framehsv); cv2.imshow('mask', framemask); cv2.imshow('median', framehsvmedian); cv2.imshow('erosion', framehsvmedianerosion)
        avgx, avgy = self.camera.getCenterPixelCV(framehsvmedianerosion)
        # flags, hcursor, (avgx, avgy) = win32gui.GetCursorInfo()
        # avgx = avgx * 2.5
        # avgy = avgy * 2.5
        self.canvas.move(self.circle, avgx, avgy)
        # self.create_circle(avgx, avgy, self.radius, self.canvas)
        print("x: " + str(avgx))
        print("y: " + str(avgy))

        # Asks if the current (X,Y) userinput is within the image's bounding box. Should probably be split up into multiple if statements.
        if avgx > self.ptx - self.xdiff1 and avgx < self.ptx + self.xdiff1 and avgy > self.pty - self.ydiff1 and avgy < self.pty + self.ydiff1:
            self.xscore += 1
            print(self.xscore)
        if avgx > self.ptx1 - self.xdiff2 and avgx < self.ptx1 + self.xdiff2 and avgy > self.pty1 - self.ydiff2 and avgy < self.pty1 + self.ydiff2:
            self.yscore += 1
            print(self.yscore)

        if self.xscore == self.scorethreshold:
            cv2.destroyAllWindows()
            self.sceneManager.setActiveScene("Exercise1")
            # self.canvas.destroy()
            # self.root.destroy()
            self.xscore = self.yscore = 0
            # return
        elif self.yscore == self.scorethreshold:
            cv2.destroyAllWindows()
            self.sceneManager.setActiveScene("Exercise2")
            # self.canvas.destroy()
            # self.root.destroy()
            self.xscore = self.yscore = 0
            # return

        self.canvas.update_idletasks()
        self.root.update_idletasks()
        self.root.update()
        self.canvas.move(self.circle, -avgx, -avgy)


