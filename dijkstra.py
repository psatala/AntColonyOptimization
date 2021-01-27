from constants import INFINITY


def dijkstra(nodes, startNodeName):
    #set up distance and visited dicts
    distance = {}
    processed = {}
    for key in nodes:
        distance[key] = INFINITY
        processed[key] = False

    #add starting node
    distance[startNodeName] = 0

    #main loop
    for i in range(len(nodes)):
        currentNodeName = startNodeName
        minDist = INFINITY
        for key in nodes:
            if distance[key] < minDist and not processed[key]:
                minDist = distance[key]
                currentNodeName = key
        
        #iterate over neighbours
        for j in range(len(nodes[currentNodeName].links)):
            if distance[nodes[currentNodeName].links[j].secondEndpoint] > distance[currentNodeName] + nodes[currentNodeName].links[j].length:
                distance[nodes[currentNodeName].links[j].secondEndpoint] = distance[currentNodeName] + nodes[currentNodeName].links[j].length
        processed[currentNodeName] = True

    return distance

    