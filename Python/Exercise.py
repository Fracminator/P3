from Scene import Scene
import cv2


class Exercise(Scene):

    def __init__(self, coordinates, sceneManager, camera):
        super().__init__(sceneManager, camera)  # Call the initializing function of the superclass, aka Scene.
        self.coordinates = coordinates

    # Overrides superclass update() function
    def update(self):
        frame = self.camera.getFrame()
        '''
        frame = cv2.imread("filterinput.png")
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        median = self.camera.medianBlur(gray)
        median2 = self.camera.medianBlur(median)
        median3 = self.camera.medianBlur(median2)
        cv2.imshow("Camera output gray", gray)
        cv2.imshow("Median x1", median)
        cv2.imshow("Median x2", median2)
        cv2.imshow("Median x3", median3)
        '''
        cv2.imshow("frame", frame)
        cv2.waitKey(1)
        # self.sceneManager.setActiveScene("Menu")  # sceneManager was inherited from the superclass.

    def validate(self, coordinates, step):
        place = "holder"
