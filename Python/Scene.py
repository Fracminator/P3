from abc import ABC  # Abstraction


class Scene(ABC):

    def __init__(self, managers):
        place = "holder"
        self.scenemanager = managers[0]
        self.inputmanager = managers[1]

    def __getinput(self, string):
        return self.inputmanager.getinput(string)

    def update(self):
        pass
