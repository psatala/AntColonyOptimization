class Node:
    name = ""
    longitude = 0.0
    lattitude = 0.0
    links = []
    def __init__(self, name, longitude, lattitude):
        self.name = name
        self.longitude = longitude
        self.lattitude = lattitude
        self.links = []

