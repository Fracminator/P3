from graphics import *
import time


class MyCircle:
    def __init__(self, center):
        self.circle = Circle(center, 10) # Where to change the size of the circle

    def drawOnCanvas(self, canvas):
        self.circle.setFill(color_rgb(0, 255, 0)) # Setting the color of the circle
        self.circle.draw(canvas)

    def getCenter(self):
        return self.circle.getCenter()

    def setCenterX(self, x):
        self.circle.getCenter().x = x

    def setCenterY(self, y):
        self.circle.getCenter().y = y

    def move(self, x, y):
        self.circle.move(x, y)

    def moveALittle(self):
        y = self.circle.getCenter().y
        movement = 0.1
        speed = 0.001
        count = 0
        if y == 50:
            while count < 50:
                y += movement
                self.circle.move(0, +movement)
                time.sleep(speed)
                count += movement
        else:
            while count < 50:
                y -= movement
                self.circle.move(0, -movement)
                time.sleep(speed)
                count += movement
