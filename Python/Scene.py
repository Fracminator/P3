from abc import ABC  # Abstraction


class Scene(ABC):

    def __init__(self, sceneManager, camera):
        self.sceneManager = sceneManager
        self.camera = camera

    def getSceneManager(self):
        return self.sceneManager

    def update(self):
        # This function is meant to be overriden by every subclass.
        pass
