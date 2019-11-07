from Scene import Scene


class Exercise(Scene):

    coordinates = []

    def __init__(self, coordinates, managers):
        super().__init__(managers)  # Call the initializing function of the superclass, aka Scene.
        self.coordinates = coordinates

    def update(self):
        place = "holder"

    def validate(self, coordinates, step):
        place = "holder"
