from Scene import Scene


class Menu(Scene):

    def __init__(self, sceneManager, camera):
        super().__init__(sceneManager, camera)

    # Overrides superclass update() function
    def update(self):
        print("test")
