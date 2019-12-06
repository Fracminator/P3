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
        self.leftShoulder = [508, 420]  # The coordinates of both shoulders
        self.rightShoulder = [800, 420]
        self.leftCircle = self.leftShoulder.copy()
        self.rightCircle = self.rightShoulder.copy()
        self.armLength = 400  # The length of the arms
        self.reps = 2  # The amount of repetitions

        self.direction = "up"
        self.keepAppRunning = True

        self.movement = 5
        self.count = 0

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

    # Overrides superclass update() function
    def update(self):

        # frame = self.camera.getFrame()
        frame = self.camera.getFrame()
        width, height, channels = frame.shape
        overlay = frame.copy()

        # left
        frameLeft = self.camera.getFrameLeft()
        frameLeft = self.camera.convertToHSV(frameLeft)
        frameLeft = self.camera.Masking(frameLeft)
        frameLeft = self.camera.medianBlur(frameLeft, 5)
        frameLeft = self.camera.erosion(frameLeft, 5)
        # cv2.imshow('hsv', framehsv)
        # cv2.imshow('mask', framemask)
        # cv2.imshow('median', framehsvmedian)
        cv2.imshow('erosion left', frameLeft)
        self.avgxLeft, self.avgyLeft = self.camera.getCenterPixelCV(frameLeft)

        # right
        frameRight = self.camera.getFrameRight()
        frameRight = self.camera.convertToHSV(frameRight)
        frameRight = self.camera.Masking(frameRight)
        frameRight = self.camera.medianBlur(frameRight, 5)
        frameRight = self.camera.erosion(frameRight, 5)
        # cv2.imshow('hsv', framehsv)
        # cv2.imshow('mask', framemask)
        # cv2.imshow('median', framehsvmedian)
        cv2.imshow('erosion right', frameRight)
        self.avgxRight, self.avgyRight = self.camera.getCenterPixelCV(frameRight)
        self.avgxRight = int(self.avgxRight + (1280 / 2))

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

        # flags, hcursor, (avgx, avgy) = win32gui.GetCursorInfo()
        cv2.circle(output, (self.avgxLeft, self.avgyLeft), 10, (0, 0, 255), thickness=2, lineType=8, shift=0)
        cv2.circle(output, (self.avgxRight, self.avgyRight), 10, (0, 0, 255), thickness=2, lineType=8, shift=0)


        cv2.imshow("Frame", output)
        cv2.waitKey(1)
        self.moveCircles()
        self.validate()

    def validate(self):
        left = False
        right = False
        # Left shoulder
        # flags, hcursor, (avgx, avgy) = win32gui.GetCursorInfo()
        if self.avgxLeft > self.leftCircle[0] - self.radius and self.avgxLeft < self.leftCircle[0] + self.radius and self.avgyLeft > self.leftCircle[1] - self.radius and self.avgyLeft < self.leftCircle[1] + self.radius:
            left = True

        # Right shoulder
        if self.avgxRight > self.rightCircle[0] - self.radius and self.avgxRight < self.rightCircle[0] + self.radius and self.avgyRight > self.rightCircle[1] - self.radius and self.avgyRight < self.rightCircle[1] + self.radius:
            right = True

        if left and right:
            self.score += 1
            print("Score: " + str(self.score))