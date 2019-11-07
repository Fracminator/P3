from Scene import Scene


class Menu(Scene):

    def __init__(self, managers):
        super().__init__(managers)

    # Overrides superclass update() function
    def update(self):
        print("test")
