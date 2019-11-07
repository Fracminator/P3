from SceneManager import SceneManager
from InputManager import InputManager
from Exercise import Exercise
import cv2

# Define the managers, which handle the inputs and the scenes. This needs to be done before mostly everything.
sceneManager = SceneManager()
inputManager = InputManager()
managers = [sceneManager, inputManager]

inputManager.createCamera("camera")

camera = inputManager.getInput("camera")

coordinates = []
currentScene = Exercise(coordinates, managers)

while True:
    cv2.imshow("name", camera.getFrame())
    cv2.waitKey(0)
    # cv2.destroyAllWindows()