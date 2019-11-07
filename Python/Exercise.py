from Scene import Scene
import cv2


class Exercise(Scene):

    coordinates = []

    def __init__(self, coordinates, managers):
        super().__init__(managers)  # Call the initializing function of the superclass, aka Scene.
        self.coordinates = coordinates
        self.camera = super().getInput("Camera")

    # Overrides superclass update() function
    def update(self):
        cv2.imshow("Camera output", self.camera.getFrame())
        cv2.waitKey(0)
        self.sceneManager.setActiveScene("Menu")  # sceneManager was inherited from the superclass.

    def validate(self, coordinates, step):
        place = "holder"
