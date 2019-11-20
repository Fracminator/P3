from Scene import Scene
import tkinter as tk
from tkinter import*


class Menu(Scene):

    def __init__(self, sceneManager, camera):
        super().__init__(sceneManager, camera)
        self.camera = camera
        self.width = 1280
        self.height = 720
        self.root = tk.Tk()
        self.img = PhotoImage(file="exe1.png")
        self.img2 = PhotoImage(file="exe2.png")
        self.setupScene()

    def setupScene(self):
        canvas = Canvas(self.root, height=self.height, width=self.width, bg="white")
        canvas.pack()
        label1 = Label(self.root, text="Welcome to our shoulder rehabilitation program!", bg="white", font=("times", 20))
        label1.place(x=400, y=40)
        label2 = Label(self.root, text="Please select an exercise, by moving your hand:", bg="white", font=("times", 20))
        label2.place(x=400, y=75)
        canvas.create_image(170, 260, anchor=NW, image=self.img)
        canvas.create_image(840, 225, anchor=NW, image=self.img2)

    # Overrides superclass update() function
    def update(self):
        # Can insert custom code here
        self.root.update_idletasks()
        self.root.update()
