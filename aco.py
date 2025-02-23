from constants import *
from ant import Ant
import numpy as np

if mode == INTERACTIVE:
    from visualization import Vis
    import cv2

def aco(nodes, startNodeName, endNodeName, metric, vis):
    
    #ants initialization
    ants = []
    for i in range(N_ANTS):
        ants.append(Ant())

    #pheromone initialization
    pheromone = {}
    for key, value in nodes.items():
        for link in value.links:
            pheromone[link.name] = PHEROMONE_INITIALIZATION_VALUE

    #set up probabilities for nodes
    probabilitiesForAllNodes = {}
    for key in nodes:
        probabilitiesForAllNodes[key] = None


    #init numpy arrays to store results
    minPathLength = np.zeros(N_EPOCHS)
    averagePathLength = np.zeros(N_EPOCHS)
    maxPathLength = np.zeros(N_EPOCHS)


    for i in range(N_EPOCHS):

        #reset all ants
        for j in range(N_ANTS):
            ants[j].clear()

        #set new probabilities for nodes
        for key in probabilitiesForAllNodes:
            probabilitiesForCurrentNode = []

            sum = 0.0
            for link in nodes[key].links:
                #calculate probability for a given link based on metric
                if metric == DIJKSTRA:
                    chance = (pheromone[link.name] ** ALPHA) * ((1.0 / link.length) ** BETA)
                else:
                    chance = pheromone[link.name] ** ALPHA

                probabilitiesForCurrentNode.append(chance)
                sum += chance

            for j in range(len(probabilitiesForCurrentNode)):
                if sum != 0:
                    probabilitiesForCurrentNode[j] /= sum
                else:
                    probabilitiesForCurrentNode[j] = 1.0 / len(nodes[key].links)

            probabilitiesForAllNodes[key] = probabilitiesForCurrentNode


        #generate solutions
        for j in range(N_ANTS):

            #init
            currentNodeName = startNodeName
            nSteps = 0
            
            #main loop
            while currentNodeName != endNodeName and nSteps <= len(nodes):
                
                #choose link given probability
                indexOfChosenLink = np.random.choice(len(nodes[currentNodeName].links), p=probabilitiesForAllNodes[currentNodeName])
                
                #add link to list
                ants[j].listOfLinks.append(nodes[currentNodeName].links[indexOfChosenLink])
                
                #add distance according to metric
                if metric == DIJKSTRA:
                    ants[j].pathLength += nodes[currentNodeName].links[indexOfChosenLink].length
                else:
                    ants[j].pathLength += 1

                #update of step count and name of current node
                nSteps += 1
                currentNodeName = nodes[currentNodeName].links[indexOfChosenLink].secondEndpoint



        #get statistics
        minPathLength[i] = INFINITY
        maxPathLength[i] = -INFINITY
        sumPathLength = 0

        for j in range(N_ANTS):
            sumPathLength += ants[j].pathLength
            minPathLength[i] = min(minPathLength[i], ants[j].pathLength)
            maxPathLength[i] = max(maxPathLength[i], ants[j].pathLength)

        averagePathLength[i] = float(sumPathLength) / float(N_ANTS)



        #pheromone update

        #evaporation
        for key in pheromone:
            pheromone[key] *= (1 - PHEROMONE_EVAPORATION_COEFFICIENT)

        #new pheromone
        for j in range(N_ANTS):
            for link in ants[j].listOfLinks:
                pheromone[link.name] += (Q / ants[j].pathLength)

        if mode == INTERACTIVE:
            if i < N_EPOCHS-1:
                if not vis.visualize(pheromone, startNodeName, endNodeName, False):
                    cv2.destroyAllWindows()
                    return minPathLength, averagePathLength, maxPathLength, False
            else:
                if not vis.visualize(pheromone, startNodeName, endNodeName, True):
                    cv2.destroyAllWindows()
                    return minPathLength, averagePathLength, maxPathLength, False

    return minPathLength, averagePathLength, maxPathLength, True
