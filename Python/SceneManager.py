from Scene import Scene


class SceneManager:

    def __init__(self):
        self.scenes = []
        self.activeScene = Scene

    def addScene(self, scene, name):
        self.scenes.append((scene, name))  # Add scene to scenes

    def setActiveScene(self, sceneName):
        for scene in self.scenes:
            if scene[1] == sceneName:
                self.activeScene = scene[0]
                return
        print("ERROR: setActiveScene failed, as the specified scene is not part of the scene list. Did you forgot to run .addScene(scene) on it?")

    def removeScene(self, sceneName):
        for i in range(0, len(self.scenes) - 1):
            if self.scenes[i][1] == sceneName:
                self.scenes.pop(i)
        print(self.scenes)

    def getActiveScene(self):
        return self.activeScene

    def update(self):
        self.activeScene.update()