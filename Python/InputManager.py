from Camera import Camera


class InputManager:
    __inputs = []

    def getInput(self, requestedName):
        # For every input, check if the requestedName matches the name associated with the input.
        # If it does, return the object associated with the input.
        for input in self.__inputs:
            if input[1] == requestedName:
                return input[0]
        print("Your requested name is not valid: " + requestedName)
        return

    def createCamera(self, name):
        camera = Camera()
        self.__inputs.append((camera, name))
