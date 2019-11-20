from Scene import Scene
import tkinter as tk
from tkinter import*




class Menu(Scene):

    def __init__(self, sceneManager, camera):
        super().__init__(sceneManager, camera)
        self.height=720
        self.width=1280
    # Overrides superclass update() function
    def update(self):
        print("test")
        root = tk.Tk()
        canvas = Canvas(root, height=self.height, width=self.width,bg="white")
        canvas.pack()
        label1 = Label(root, text="Welcome to our shoulder rehabilitation program!",bg="white", font=("times",20 )).place(x=400, y=40)
        label2 = Label(root, text="Please select an exercise, by moving your hand:",bg="white", font=("times",20 )).place(x=400, y=70)
        img=PhotoImage(file="exe1.png")
        img2=PhotoImage(file="exe2.png")
        canvas.create_image(170, 260, anchor=NW, image=img)
        canvas.create_image(840,225,anchor=NW,image=img2)

        mainloop()


