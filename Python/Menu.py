from Scene import Scene
import tkinter as tk
from tkinter import*
import cv2
from Exercise import Exercise


class Menu(Scene):

    def __init__(self, sceneManager, camera):
        super().__init__(sceneManager, camera)
        self.camera = camera
        self.width = 1280
        self.height = 720
        self.root = tk.Tk()
        self.canvas = Canvas(self.root, height=self.height, width=self.width, bg="white")
        self.img = PhotoImage(file="exe1.png")
        self.img2 = PhotoImage(file="exe2.png")
        self.setupScene()
        self.image1x = 170
        self.image1y = 260
        self.image2x = 840
        self.image2y = 225
        self.image1height = 425
        self.image1width = 380
        self.image2height = 467
        self.image2width = 246
        self.ptx = self.image1x + (self.image1width / 2)
        self.pty = self.image1y + (self.image1height / 2)
        self.ptx1 = self.image2x + (self.image2width / 2)
        self.pty1 = self.image2y + (self.image2height / 2)
        self.radius = 30
        self.xscore = 0
        self.yscore = 0

    def setupScene(self):
        self.canvas.pack()
        label1 = Label(self.root, text="Welcome to our shoulder rehabilitation program!", bg="white", font=("times", 20))
        label1.place(x=400, y=40)
        label2 = Label(self.root, text="Please select an exercise, by moving your hand:", bg="white", font=("times", 20))
        label2.place(x=400, y=75)
        self.canvas.create_image(170, 260, anchor=NW, image=self.img)
        self.canvas.create_image(840, 225, anchor=NW, image=self.img2)

    # Overrides superclass update() function
    def update(self):
        # Can insert custom code here
        framehsv = self.camera.getFrameHSV()
        framemask = self.camera.Masking(framehsv)
        framehsvmedian = self.camera.medianBlur(framemask, 5)
        framehsvmedianerosion = self.camera.erosion(framehsvmedian, 5)
        cv2.imshow('mask', framemask)
        cv2.imshow('median', framehsvmedian)
        cv2.imshow('erosion', framehsvmedianerosion)
        avgx, avgy = self.camera.getCenterPixel(framehsvmedianerosion)
        avgx = avgx * 2.5
        avgy = avgy * 2.5
        self.create_circle(avgy, avgx, self.radius, self.canvas)
        print(avgy)
        print(avgx)
        xdiff1 = self.image1width / 2
        ydiff1 = self.image1height / 2
        xdiff2 = self.image2width / 2
        ydiff2 = self.image2height / 2
        if avgx > self.ptx - xdiff1 and avgx < self.ptx + xdiff1 and avgy > self.pty - ydiff1 and avgy < self.pty + ydiff1:
            self.xscore += 1
            print(self.xscore)
        if avgx > self.ptx1 - xdiff2 and avgx < self.ptx1 + xdiff2 and avgy > self.pty1 - ydiff2 and avgy < self.pty1 + ydiff2:
            self.yscore += 1
            print(self.yscore)
        if self.xscore == 5 or self.yscore == 5:
            cv2.destroyAllWindows()
            exerciseScene = Exercise([], self.sceneManager, self.camera)
            self.sceneManager.addScene(exerciseScene, "Exercise")
            self.sceneManager.setActiveScene("Exercise")
            self.canvas.destroy()
            self.root.destroy()
            return

        self.canvas.update_idletasks()
        self.root.update_idletasks()
        self.root.update()

    def create_circle(self, x, y, r, canvasName):  # center coordinates, radius
        x0 = x
        y0 = y
        x1 = x + r
        y1 = y + r
        return canvasName.create_oval(x0, y0, x1, y1)


