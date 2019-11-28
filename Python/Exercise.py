from Scene import Scene
import cv2
from MyCircle import *
import numpy as np
import math

class Exercise(Scene):

    def __init__(self, coordinates, sceneManager, camera):
        super().__init__(sceneManager, camera)  # Call the initializing function of the superclass, aka Scene.
        self.coordinates = coordinates
        self.score = 0
        # Properties
        self.windowWidth = 1920 / 2
        self.windowHeight = 1080 / 2
        self.window = GraphWin("Window", self.windowWidth, self.windowHeight)

        # These four can be changed without destroying anything (hopefully)
        self.leftShoulder = Point(300, 200)  # The coordinates of both shoulders
        self.rightShoulder = Point(400, 200)
        self.armLength = 175  # The length of the arms
        self.reps = 2  # The amount of repetitions

        # Setting the center coordinates of the specific circles
        center = Point(self.leftShoulder.x, self.leftShoulder.y)
        center2 = Point(self.rightShoulder.x, self.rightShoulder.y)
        center3 = Point(self.rightShoulder.x + self.armLength, self.rightShoulder.y)
        center4 = Point(self.leftShoulder.x - self.armLength, self.leftShoulder.y)

        self.circle = MyCircle(center)
        self.circle2 = MyCircle(center2)
        self.circle3 = MyCircle(center3)
        self.circle4 = MyCircle(center4)

        # Booleans
        self.exercise1 = False
        self.exercise2 = True
        self.keepAppRunning = True

    def moveCircles(self):
        y = self.circle.getCenter().y
        movement = 0.1
        speed = 0.001
        count = 0
        if y == 200:
            while count < self.armLength:
                y -= movement
                self.circle.move(0, -movement)
                self.circle2.move(0, -movement)
                time.sleep(speed)
                count += movement
        else:
            while count < self.armLength:
                y += movement
                self.circle.move(0, +movement)
                self.circle2.move(0, +movement)
                time.sleep(speed)
                count += movement

    def rotate(self, origin, point, angle):
        """
        Rotate a point counterclockwise by a given angle around a given origin.

        The angle should be given in radians.
        """
        ox, oy = origin
        px, py = point

        qx = ox + math.cos(angle) * (px - ox) - math.sin(angle) * (py - oy)
        qy = oy + math.sin(angle) * (px - ox) + math.cos(angle) * (py - oy)
        return qx, qy

    def moveCircles2(self):
        oxl = self.leftShoulder.x
        oyl = self.leftShoulder.y
        y3 = self.circle3.getCenter().y  # The coordinates for the green circle
        x3 = self.circle3.getCenter().x
        y4 = self.circle4.getCenter().y
        x4 = self.circle4.getCenter().x
        speed = 0.01

        for x in range(0, self.reps + 1, 1):
            print(x)
            if x == self.reps:
                break
            if self.rightShoulder.y + 1 > y3 > self.rightShoulder.y - 1 and x < self.reps:
                print("GO")
                for angle in np.arange(0, 90.2, 0.2):
                    rx3 = x3
                    ry3 = y3
                    rx4 = x4
                    ry4 = y4
                    origin3 = (self.rightShoulder.x, self.rightShoulder.y)
                    circleCenter3 = (rx3, ry3)
                    origin4 = (oxl, oyl)
                    circleCenter4 = (rx4, ry4)
                    newX3, newY3 = self.rotate(origin3, circleCenter3, math.radians(-0.2))
                    newX4, newY4 = self.rotate(origin4, circleCenter4, math.radians(0.2))
                    x3 = newX3  # new old point
                    y3 = newY3  # new old point
                    x4 = newX4
                    y4 = newY4
                    xMove3 = x3 - rx3
                    yMove3 = y3 - ry3
                    xMove4 = x4 - rx4
                    yMove4 = y4 - ry4
                    self.circle3.move(xMove3, yMove3)
                    self.circle4.move(xMove4, yMove4)
                    time.sleep(speed)

            if self.rightShoulder.x + 1 > x3 > self.rightShoulder.x - 1:

                for angle in np.arange(0, 90.2, 0.2):
                    rx3 = x3
                    ry3 = y3
                    rx4 = x4
                    ry4 = y4
                    origin3 = (self.rightShoulder.x, self.rightShoulder.y)
                    circleCenter3 = (rx3, ry3)
                    origin4 = (oxl, oyl)
                    circleCenter4 = (rx4, ry4)
                    newX3, newY3 = self.rotate(origin3, circleCenter3, math.radians(0.2))
                    newX4, newY4 = self.rotate(origin4, circleCenter4, math.radians(-0.2))
                    x3 = newX3  # new old point
                    y3 = newY3  # new old point
                    x4 = newX4
                    y4 = newY4
                    xMove3 = x3 - rx3
                    yMove3 = y3 - ry3
                    xMove4 = x4 - rx4
                    yMove4 = y4 - ry4
                    self.circle3.move(xMove3, yMove3)
                    self.circle4.move(xMove4, yMove4)
                    time.sleep(speed)

    # Overrides superclass update() function
    def update(self):
        framehsv = self.camera.getFrameHSV()
        cv2.imshow("HSV", framehsv)
        mask = self.camera.Masking(framehsv)
        cv2.imshow("Mask", mask)
        median = self.camera.medianBlur(mask, 5)
        cv2.imshow("Median", median)
        erosion = self.camera.erosion(median, 5)
        cv2.imshow("Erosion", erosion)
        cv2.waitKey(1)

        if self.exercise1:
            self.circle.drawOnCanvas(self.window)
            self.circle2.drawOnCanvas(self.window)

            endCount = 0

            while self.keepAppRunning:
                self.moveCircles()
                endCount += 0.5
                if endCount == self.reps:
                    break
        if self.exercise2:

            self.circle3.drawOnCanvas(self.window)
            self.circle4.drawOnCanvas(self.window)
            while self.keepAppRunning:
                self.moveCircles2()
                break

    def validate(self, avgx, avgy, ptx, pty):
        if avgx > ptx - 25 and avgx < ptx + 25 and avgy > pty - 25 and avgy < pty + 25:
            self.score += 1

