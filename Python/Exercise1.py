from Scene import Scene
import cv2


class Exercise1(Scene):

    def __init__(self, sceneManager, camera):
        super().__init__(sceneManager, camera)  # Call the initializing function of the superclass, aka Scene.
        self.score = 0
        self.maxScore = 0
        # Properties

        # These four can be changed without destroying anything (hopefully)
        self.leftShoulder = [508, 420]  # The coordinates of both shoulders
        self.rightShoulder = [800, 420]
        self.leftCircle = self.leftShoulder.copy()
        self.rightCircle = self.rightShoulder.copy()
        self.armLength = 400  # The length of the arms
        self.repsMax = 2  # The amount of repetitions
        self.repsCurrent = 0

        self.direction = "up"
        self.hasStarted = False

        self.movement = 5  # Default value is 5
        self.count = 0

    def reset(self):
        self.repsCurrent = 0
        self.hasStarted = False
        self.score = 0
        self.maxScore = 0


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
                self.repsCurrent += 1
                if self.repsCurrent == self.repsMax:
                    cv2.destroyAllWindows()
                    self.reset()
                    self.sceneManager.setActiveScene("Menu")
                    return

    # Overrides superclass update() function
    def update(self):

        frame = self.camera.getFrame()
        overlay = frame.copy()

        # left
        frameLeft = self.camera.getFrameLeft()
        frameLeft = self.camera.convertToHSV(frameLeft)
        frameLeft = self.camera.Masking(frameLeft)
        frameLeft = self.camera.medianBlur(frameLeft, 5)
        frameLeft = self.camera.erosion(frameLeft, 5)

        avgxLeft, avgyLeft = self.camera.getCenterPixelCV(frameLeft)

        # right
        frameRight = self.camera.getFrameRight()
        frameRight = self.camera.convertToHSV(frameRight)
        frameRight = self.camera.Masking(frameRight)
        frameRight = self.camera.medianBlur(frameRight, 5)
        frameRight = self.camera.erosion(frameRight, 5)

        avgxRight, avgyRight = self.camera.getCenterPixelCV(frameRight)
        avgxRight = int(avgxRight + (1280 / 2))

        xLeft = int(self.leftCircle[0])
        yLeft = int(self.leftCircle[1])
        xRight = int(self.rightCircle[0])
        yRight = int(self.rightCircle[1])

        self.radius = 75

        cv2.circle(overlay, (xLeft, yLeft), self.radius, (0, 255, 0), thickness=-1, lineType=8, shift=0)
        cv2.circle(overlay, (xRight, yRight), self.radius, (0, 255, 0), thickness=-1, lineType=8, shift=0)
        output = cv2.addWeighted(overlay, 0.4, frame, 0.6, 0)

        cv2.circle(output, (xLeft, yLeft), self.radius, (0, 255, 0), thickness=6, lineType=8, shift=0)
        cv2.circle(output, (xRight, yRight), self.radius, (0, 255, 0), thickness=6, lineType=8, shift=0)

        cv2.circle(output, (avgxLeft, avgyLeft), 10, (0, 0, 255), thickness=2, lineType=8, shift=0)
        cv2.circle(output, (avgxRight, avgyRight), 10, (0, 0, 255), thickness=2, lineType=8, shift=0)

        if self.maxScore is not 0:
            scorePercentage = int(self.score / self.maxScore * 100)
        else:
            scorePercentage = 100

        cv2.putText(output, "Score: " + str(scorePercentage) + "%",
                    (560, 50),  # Bottom left corner of text
                    cv2.FONT_HERSHEY_SIMPLEX,  # Font
                    1,  # Font scale
                    (0, 0, 0),  # Font color
                    2)  # Line type

        cv2.namedWindow("Frame")
        cv2.moveWindow("Frame", 0, 0)
        cv2.imshow("Frame", output)
        cv2.waitKey(1)

        if self.hasStarted:
            self.moveCircles()
            if self.validate(avgxLeft, avgxRight, avgyLeft, avgyRight):  # If the user successfully has their hands inside of the circles, the score increases.
                self.score += 1
                print("Score: " + str(self.score))

            self.maxScore += 1  # Max Score should count up regardless of the users success.

        else:
            if self.validate(avgxLeft, avgxRight, avgyLeft, avgyRight):
                self.hasStarted = True

    def validate(self, avgxLeft, avgxRight, avgyLeft, avgyRight):
        left = False
        right = False

        # Left shoulder
        if avgxLeft > self.leftCircle[0] - self.radius and avgxLeft < self.leftCircle[0] + self.radius and avgyLeft > self.leftCircle[1] - self.radius and avgyLeft < self.leftCircle[1] + self.radius:
            left = True

        # Right shoulder
        if avgxRight > self.rightCircle[0] - self.radius and avgxRight < self.rightCircle[0] + self.radius and avgyRight > self.rightCircle[1] - self.radius and avgyRight < self.rightCircle[1] + self.radius:
            right = True

        return left == right == True
