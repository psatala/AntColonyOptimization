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




def main():
    filepath = "nobel-eu.txt"
    readingNodes = False
    readingLinks = False
    nodes = {}
    with open(filepath) as fp:
        for line in fp:
            splitLine = line.split()

            #beginnings and ends of sections
            if len(splitLine) > 0 and splitLine[0] == "NODES":
                readingNodes = True
            if len(splitLine) > 0 and splitLine[0] == "LINKS":
                readingLinks = True
            if len(splitLine) > 0 and splitLine[0] == ")":
                readingNodes = False
                readingLinks = False
            
            if len(splitLine) > 4 and readingNodes:
                node = Node(name=splitLine[0], longitude=float(splitLine[2]), lattitude=float(splitLine[3]))
                nodes[splitLine[0]] = node
                #print(id(node.links))

            if len(splitLine) > 5 and readingLinks:
                link = Link(name=splitLine[0], firstEndpoint=splitLine[2], secondEndpoint=splitLine[3], length=float(splitLine[5]))
                #print(type(nodes[link.endpoints[0]].links), link.endpoints[1])
                nodes[link.firstEndpoint].links.append(link)
                nodes[link.secondEndpoint].links.append(link)
                print(id(nodes[link.firstEndpoint].links))

    pass



if __name__ == "__main__":
    main()