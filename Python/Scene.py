from abc import ABC  # Abstraction


class Scene(ABC):

    def __init__(self, managers):
        self.sceneManager = managers[0]
        self.inputManager = managers[1]

    def __getInput(self, string):
        return self.inputManager.getInput(string)

    def update(self):
        pass
