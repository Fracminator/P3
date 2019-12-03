from Scene import Scene
import cv2
import math
import time


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

        size = 75

        # cv2.circle(image, (x, y), size, (B, G, R), thickness, linetype, shift)
        cv2.circle(overlay, (xLeft, yLeft), size, (0, 255, 0), thickness=-1, lineType=8, shift=0)
        cv2.circle(overlay, (xRight, yRight), size, (0, 255, 0), thickness=-1, lineType=8, shift=0)
        output = cv2.addWeighted(overlay, 0.4, frame, 0.6, 0)

        cv2.circle(output, (xLeft, yLeft), size, (0, 255, 0), thickness=6, lineType=8, shift=0)
        cv2.circle(output, (xRight, yRight), size, (0, 255, 0), thickness=6, lineType=8, shift=0)

        cv2.imshow("Frame", output)
        cv2.waitKey(1)
        self.moveCircles()


    def validate(self, avgx, avgy, ptx, pty):
        if avgx > ptx - 25 and avgx < ptx + 25 and avgy > pty - 25 and avgy < pty + 25:
            self.score += 1
