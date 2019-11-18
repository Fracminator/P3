from Scene import Scene
import cv2


class Exercise(Scene):

    def __init__(self, coordinates, sceneManager, camera):
        super().__init__(sceneManager, camera)  # Call the initializing function of the superclass, aka Scene.
        self.coordinates = coordinates

    # Overrides superclass update() function
    def update(self):
        frame = self.camera.getFrame()
        # frame = cv2.imread("filterinput.png")
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        median = self.camera.medianBlur(gray, 5)
        erosion = self.camera.erosion(median, 5)
        cv2.imshow("Input", gray)
        cv2.imshow("median", median)
        cv2.imshow("erosion", erosion)
        self.camera.Masking()

        # cv2.imshow("frame", frame)
        cv2.waitKey(1)
        # self.sceneManager.setActiveScene("Menu")  # sceneManager was inherited from the superclass.

    def validate(self, coordinates, step):
        place = "holder"
