from node import Node
from link import Link


def input(filepath):
    
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
            
            #add node
            if len(splitLine) > 4 and readingNodes:
                node = Node(name=splitLine[0], longitude=float(splitLine[2]), lattitude=float(splitLine[3]))
                nodes[splitLine[0]] = node

            #add link
            if len(splitLine) > 5 and readingLinks:
                link = Link(name=splitLine[0], firstEndpoint=splitLine[2], secondEndpoint=splitLine[3], length=float(splitLine[5]))
                nodes[link.firstEndpoint].links.append(link)
                link = Link(name=splitLine[0], firstEndpoint=splitLine[3], secondEndpoint=splitLine[2], length=float(splitLine[5]))
                nodes[link.firstEndpoint].links.append(link)
                

    return nodes
