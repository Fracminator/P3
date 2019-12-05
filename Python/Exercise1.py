from Scene import Scene
import cv2
import math
import time
from win32 import win32gui


class Exercise1(Scene):

    def __init__(self, coordinates, sceneManager, camera):
        super().__init__(sceneManager, camera)  # Call the initializing function of the superclass, aka Scene.
        self.coordinates = coordinates
        self.score = 0
        # Properties

        # These four can be changed without destroying anything (hopefully)
        self.leftShoulder = [635, 550]  # The coordinates of both shoulders
        self.rightShoulder = [1000, 550]
        self.armLength = 400  # The length of the arms
        self.reps = 2  # The amount of repetitions

        self.direction = "up"
        self.keepAppRunning = True

        self.movement = 5
        self.count = 0

    def moveCircles(self):

        if self.direction == "up":
            self.leftShoulder[1] -= self.movement
            self.rightShoulder[1] -= self.movement
            self.count += self.movement

            if self.count > self.armLength:
                self.direction = "down"
                self.count = 0

        elif self.direction == "down":
            self.leftShoulder[1] += self.movement
            self.rightShoulder[1] += self.movement
            self.count += self.movement

            if self.count > self.armLength:
                self.direction = "up"
                self.count = 0

    # Overrides superclass update() function
    def update(self):

        # frame = self.camera.getFrame()
        frame = self.camera.getFrame()
        frame = cv2.resize(frame, (1600, 900))
        overlay = frame.copy()

        xLeft = int(self.leftShoulder[0])
        yLeft = int(self.leftShoulder[1])
        xRight = int(self.rightShoulder[0])
        yRight = int(self.rightShoulder[1])

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
        if avgx > self.leftShoulder[0] - self.radius and avgx < self.leftShoulder[0] + self.radius and avgy > self.leftShoulder[1] - self.radius and avgy < self.leftShoulder[1] + self.radius:
            self.score += 1
            print(self.score)

        # Right shoulder
        if avgx > self.rightShoulder[0] - self.radius and avgx < self.rightShoulder[0] + self.radius and avgy > self.rightShoulder[1] - self.radius and avgy < self.rightShoulder[1] + self.radius:
            self.score += 1
            print(self.score)