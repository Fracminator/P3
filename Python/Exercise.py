from Scene import Scene
import cv2
from MyCircle import *
import math


class Exercise1(Scene):

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

        self.circle = MyCircle(center)
        self.circle2 = MyCircle(center2)

        self.direction = "up"
        self.firstTimeRunning = True
        self.keepAppRunning = True

        self.movement = 1
        self.speed = 0.001
        self.count = 0

    def moveCircles(self):
        y = self.circle.getCenter().y

        if self.direction == "up":
            y -= self.movement
            self.circle.move(0, -self.movement)
            self.circle2.move(0, -self.movement)
            time.sleep(self.speed)
            self.count += self.movement

            if self.count > self.armLength:
                self.direction = "down"
                self.count = 0
        elif self.direction == "down":
            y += self.movement
            self.circle.move(0, +self.movement)
            self.circle2.move(0, +self.movement)
            time.sleep(self.speed)
            self.count += self.movement

            if self.count > self.armLength:
                self.direction = "up"
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

    # Overrides superclass update() function
    def update(self):
        if self.firstTimeRunning:
            self.circle.drawOnCanvas(self.window)
            self.circle2.drawOnCanvas(self.window)
            self.firstTimeRunning = False

        cv2.imshow("Frame", self.camera.getFrame())
        self.moveCircles()

    def validate(self, avgx, avgy, ptx, pty):
        if avgx > ptx - 25 and avgx < ptx + 25 and avgy > pty - 25 and avgy < pty + 25:
            self.score += 1

