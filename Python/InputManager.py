from Camera import Camera


class InputManager:
    __inputs = []
    output = "holder"

    def getinput(self, requestedname):
        place = "holder"
        # TODO: loop through all indexes of inputs, check the tuple inside to find the input connected
        #  to the string received as an argument. Then return the input object connected to said string.

        for input in self.__inputs:
            if input[1] == requestedname:
                return input[0]
        print("Your requested name is not valid: " + requestedname)
        return

    def createcamera(self, name):
        camera = Camera()
        self.__inputs.append((camera, name))
