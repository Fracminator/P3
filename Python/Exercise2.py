from Scene import Scene
import cv2
import numpy as np
import math
import time
from win32 import win32gui

# TODO: While making this, inaccurately assumed that the circles were placed in the shoulders, as with exercise1. This means all of this is wrong, as they're placed in shoulder +/- armlength.
# fix :(

class Exercise2(Scene):

    def __init__(self, coordinates, sceneManager, camera):
        super().__init__(sceneManager, camera)  # Call the initializing function of the superclass, aka Scene.
        self.coordinates = coordinates
        self.score = 0
        # Properties

        # These four can be changed without destroying anything (hopefully)
        self.leftShoulder = [635, 550]  # The coordinates of both shoulders
        self.rightShoulder = [1000, 550]
        self.leftCircle = self.leftShoulder.copy()
        self.rightCircle = self.rightShoulder.copy()
        self.armLength = 400  # The length of the arms
        self.reps = 2  # The amount of repetitions

        self.direction = "up"
        self.keepAppRunning = True

        self.movement = 5
        self.count = 0

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

    def moveCircles(self):

        if self.direction == "up":
            self.leftCircle[1] -= self.movement
            self.rightCircle[1] -= self.movement
            self.count += self.movement

            if self.count > self.armLength:
                self.direction = "down"
                self.count = 0

        elif self.direction == "down":
            self.leftCircle[1] += self.movement
            self.rightCircle[1] += self.movement
            self.count += self.movement

            if self.count > self.armLength:
                self.direction = "up"
                self.count = 0

        y3 = self.rightCircle.getCenter().y  # The coordinates for the green circle
        x3 = self.rightCircle.getCenter().x
        y4 = self.leftCircle.getCenter().y
        x4 = self.leftCircle.getCenter().x
        speed = 0.01

        for x in range(0, self.reps + 1, 1):
            print(x)
            if x == self.reps:
                break
            if self.rightCircle[1] + 1 > y3 > self.rightCircle[1] - 1 and x < self.reps:
                print("GO")
                for angle in np.arange(0, 90.2, 0.2):
                    rx3 = x3
                    ry3 = y3
                    rx4 = x4
                    ry4 = y4
                    origin3 = (self.rightCircle[0], self.rightCircle[1])
                    circleCenter3 = (rx3, ry3)
                    origin4 = (self.leftCircle[0], self.leftCircle[1])
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
                    self.rightCircle[0] += xMove3
                    self.rightCircle[1] += yMove3
                    self.leftCircle[0] += xMove4
                    self.leftCircle[1] += yMove4

            if self.rightCircle[0] + 1 > x3 > self.rightCircle[0] - 1:

                for angle in np.arange(0, 90.2, 0.2):
                    rx3 = x3
                    ry3 = y3
                    rx4 = x4
                    ry4 = y4
                    origin3 = (self.rightCircle[0], self.rightCircle[1])
                    circleCenter3 = (rx3, ry3)
                    origin4 = (self.leftCircle[0], self.leftCircle[1])
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
                    self.rightCircle[0] += xMove3
                    self.rightCircle[1] += yMove3
                    self.leftCircle[0] += xMove4
                    self.leftCircle[1] += yMove4

    # Overrides superclass update() function
    def update(self):

        # frame = self.camera.getFrame()
        frame = self.camera.getFrame()
        frame = cv2.resize(frame, (1280, 720))
        overlay = frame.copy()

        xLeft = int(self.leftCircle[0])
        yLeft = int(self.leftCircle[1])
        xRight = int(self.rightCircle[0])
        yRight = int(self.rightCircle[1])

        self.radius = 75

        # cv2.circle(image, (x, y), size, (B, G, R), thickness, linetype, shift)
        cv2.circle(overlay, (xLeft, yLeft), self.radius, (0, 255, 0), thickness=-1, lineType=8, shift=0)
        cv2.circle(overlay, (xRight, yRight), self.radius, (0, 255, 0), thickness=-1, lineType=8, shift=0)
        output = cv2.addWeighted(overlay, 0.4, frame, 0.6, 0)

        cv2.circle(output, (xLeft, yLeft), self.radius, (0, 255, 0), thickness=6, lineType=8, shift=0)
        cv2.circle(output, (xRight, yRight), self.radius, (0, 255, 0), thickness=6, lineType=8, shift=0)

        flags, hcursor, (avgx, avgy) = win32gui.GetCursorInfo()
        cv2.circle(output, (avgx, avgy), 10, (0, 0, 255), thickness=2, lineType=8, shift=0)


        cv2.imshow("Frame", output)
        cv2.waitKey(1)
        self.moveCircles()
        self.validate()


    def validate(self):
        # Left shoulder
        flags, hcursor, (avgx, avgy) = win32gui.GetCursorInfo()
        if avgx > self.leftCircle[0] - self.radius and avgx < self.leftCircle[0] + self.radius and avgy > self.leftCircle[1] - self.radius and avgy < self.leftCircle[1] + self.radius:
            self.score += 1
            print(self.score)

        # Right shoulder
        if avgx > self.rightCircle[0] - self.radius and avgx < self.rightCircle[0] + self.radius and avgy > self.rightCircle[1] - self.radius and avgy < self.rightCircle[1] + self.radius:
            self.score += 1
            print(self.score)