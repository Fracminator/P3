from Scene import Scene


class SceneManager:

    def __init__(self):
        self.__scenes = []
        self.__activeScene = Scene

    def addScene(self, scene, name):
        self.__scenes.append((scene, name))  # Add scene to scenes

    def setActiveScene(self, sceneName):
        for scene in self.__scenes:
            if scene[1] == sceneName:
                self.__activeScene = scene[0]
                return
        print("ERROR: setActiveScene failed, as the specified scene is not part of the scene list. Did you forgot to run .addScene(scene) on it?")

    def getActiveScene(self):
        return self.__activeScene

    def update(self):
        self.__activeScene.update()