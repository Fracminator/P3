from SceneManager import SceneManager
from InputManager import InputManager
from Exercise import Exercise
from Menu import Menu

# Define the managers, which handle the inputs and the scenes. This needs to be done before mostly everything
sceneManager = SceneManager()
inputManager = InputManager()
managers = [sceneManager, inputManager]

# Create the necessary inputs
inputManager.createCamera("Camera")


exerciseScene = Exercise([], managers)
menuScene = Menu(managers)
sceneManager.addScene(exerciseScene, "Exercise")
sceneManager.addScene(menuScene, "Menu")
sceneManager.setActiveScene("Exercise")

# Main loop
while True:
    sceneManager.getActiveScene().update()
