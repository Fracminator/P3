from SceneManager import SceneManager
from Camera import Camera
from Exercise import Exercise
from Menu import Menu



# Define the managers, which handle the inputs and the scenes. This needs to be done before mostly everything
sceneManager = SceneManager()

# Create the necessary inputs
camera = Camera()


exerciseScene = Exercise([], sceneManager, camera)
menuScene = Menu(sceneManager, camera)
sceneManager.addScene(exerciseScene, "Exercise")
sceneManager.addScene(menuScene, "Menu")
sceneManager.setActiveScene("Exercise")


# Main loop
while True:
    sceneManager.update()
