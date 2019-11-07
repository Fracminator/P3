from abc import ABC  # Abstraction


class Scene(ABC):

    def __init__(self, managers):
        self.sceneManager = managers[0]
        self.inputManager = managers[1]

    def getInput(self, string):
        return self.inputManager.getInput(string)

    def getSceneManager(self):
        return self.sceneManager

    def update(self):
        # This function is meant to be overriden by every subclass.
        pass
