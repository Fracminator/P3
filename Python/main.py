from SceneManager import SceneManager
from InputManager import InputManager
from Exercise import Exercise
import cv2

# Define the managers, which handle the inputs and the scenes. This needs to be done before mostly everything.
scenemanager = SceneManager()
inputmanager = InputManager()
managers = [scenemanager, inputmanager]

inputmanager.createcamera("camera")

camera = inputmanager.getinput("camera")

cv2.imshow("name", camera.getframe())
cv2.waitKey(0)
cv2.destroyAllWindows()


coordinates = []
currentScene = Exercise(coordinates, managers)
