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
        self.windowWidth = 1920
        self.windowHeight = 1080
        self.window = GraphWin("Window", self.windowWidth, self.windowHeight)

        # These four can be changed without destroying anything (hopefully)
        self.leftShoulder = Point(745, 650)  # The coordinates of both shoulders
        self.rightShoulder = Point(1160, 650)
        self.armLength = 600  # The length of the arms
        self.reps = 2  # The amount of repetitions

        # Setting the center coordinates of the specific circles
        centerLeft = Point(self.leftShoulder.x, self.leftShoulder.y)
        centerRight = Point(self.rightShoulder.x, self.rightShoulder.y)

        self.circle = MyCircle(centerLeft)
        self.circle2 = MyCircle(centerRight)
        self.circle.drawOnCanvas(self.window)
        self.circle2.drawOnCanvas(self.window)

        self.direction = "up"
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

        # frame = self.camera.getFrame()
        frame = cv2.imread("input.png")
        overlay = frame.copy()

        # cv2.circle(image, (x, y), size, (B, G, R), thickness, linetype, shift)
        cv2.circle(overlay, (110, 590), 90, (0, 255, 0), thickness=-1, lineType=8, shift=0)
        output = cv2.addWeighted(overlay, 0.4, frame, 0.6, 0)
        cv2.circle(output, (110, 590), 90, (0, 255, 0), thickness=6, lineType=8, shift=0)

        cv2.imshow("Frame", output)
        self.moveCircles()

    def validate(self, avgx, avgy, ptx, pty):
        if avgx > ptx - 25 and avgx < ptx + 25 and avgy > pty - 25 and avgy < pty + 25:
            self.score += 1
