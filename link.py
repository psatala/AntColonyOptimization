class Link:
    name = ""
    firstEndpoint = ""
    secondEndpoint = ""
    length = 0
    def __init__(self, name, firstEndpoint, secondEndpoint, length):
        self.name = name
        self.firstEndpoint = firstEndpoint
        self.secondEndpoint = secondEndpoint
        self.length = length

