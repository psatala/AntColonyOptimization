class Node:
    name = ""
    longitude = 0.0
    lattitude = 0.0
    imgX = 0
    imgY = 0
    links = []
    def __init__(self, name, longitude, lattitude, imgX, imgY):
        self.name = name
        self.longitude = longitude
        self.lattitude = lattitude
        self.imgX = imgX
        self.imgY = imgY
        self.links = []

