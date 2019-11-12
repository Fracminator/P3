from Scene import Scene
import cv2


class Exercise(Scene):

    def __init__(self, coordinates, sceneManager, camera):
        super().__init__(sceneManager, camera)  # Call the initializing function of the superclass, aka Scene.
        self.coordinates = coordinates

    # Overrides superclass update() function
    def update(self):
        frame = self.camera.getFrame()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow("Camera output", gray)
        cv2.waitKey(1)
        # self.sceneManager.setActiveScene("Menu")  # sceneManager was inherited from the superclass.

    def validate(self, coordinates, step):
        place = "holder"
