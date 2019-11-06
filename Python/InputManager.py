from Camera import Camera


class InputManager:
    __inputs = []

    def getinput(self, requestedname):
        for input in self.__inputs:
            if input[1] == requestedname:
                return input[0]
        print("Your requested name is not valid: " + requestedname)
        return

    def createcamera(self, name):
        camera = Camera()
        self.__inputs.append((camera, name))
