from constants import INFINITY

def bfs(nodes, startNodeName):
    #set up distance and visited dicts
    distance = {}
    visited = {}
    for key in nodes:
        distance[key] = INFINITY
        visited[key] = False

    #add starting node
    nodesQueue = [startNodeName]
    distance[startNodeName] = 0
    visited[startNodeName] = True

    #main loop
    for i in range(len(nodes)):
        currentNodeName = nodesQueue[i]
        
        #iterate over neighbours
        for j in range(len(nodes[currentNodeName].links)):
            if not visited[nodes[currentNodeName].links[j].secondEndpoint]:
                nodesQueue.append(nodes[currentNodeName].links[j].secondEndpoint)
                visited[nodes[currentNodeName].links[j].secondEndpoint] = True
                distance[nodes[currentNodeName].links[j].secondEndpoint] = distance[currentNodeName] + 1

    return distance

    