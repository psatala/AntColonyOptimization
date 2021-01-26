class Ant:

    def __init__(self):
        self.pathLength = 0
        self.listOfLinks = []

    def clear(self):
        self.pathLength = 0
        self.listOfLinks.clear()