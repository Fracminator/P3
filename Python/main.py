from SceneManager import SceneManager
from Camera import Camera
from Menu import Menu
from Exercise1 import Exercise1
from Exercise2 import Exercise2



# Define the managers, which handle the inputs and the scenes. This needs to be done before mostly everything
sceneManager = SceneManager()

# Create the necessary inputs
camera = Camera()


# exerciseScene = Exercise([], sceneManager, camera)
menuScene = Menu(sceneManager, camera)
exercise1Scene = Exercise1([], sceneManager, camera)
exercise2Scene = Exercise2([], sceneManager, camera)
# sceneManager.addScene(exerciseScene, "Exercise")
sceneManager.addScene(menuScene, "Menu")
sceneManager.addScene(exercise1Scene, "Exercise1")
sceneManager.addScene(exercise2Scene, "Exercise2")
sceneManager.setActiveScene("Menu")


# Main loop
while True:
    sceneManager.update()
