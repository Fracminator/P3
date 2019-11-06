class SceneManager:
    __scenes = []
    __activeScene = None

    def __init__(self):
        place = "holder"

    def addscene(self, scene):
        self.__scenes.append(scene)  # Add scene to scenes

    def changeactivescene(self, scene):
        if self.__scenes.__contains__(scene):
            self.__activeScene = scene

    def getactivescene(self):
        return self.activeScene
