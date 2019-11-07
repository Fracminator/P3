class SceneManager:
    __scenes = []
    __activeScene = None

    def __init__(self):
        place = "holder"

    def addScene(self, scene):
        self.__scenes.append(scene)  # Add scene to scenes

    def changeActiveCcene(self, scene):
        if self.__scenes.__contains__(scene):
            self.__activeScene = scene

    def getActiveScene(self):
        return self.activeScene
