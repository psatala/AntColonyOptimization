from input import input
from bfs import bfs
from aco import aco
from dijkstra import dijkstra
from constants import BFS, N_EPOCHS, N_RUNS, DIJKSTRA
from plot import createSummary

import numpy as np
import random
import time

def main():

    #seed
    seed = int(round(time.time()))
    np.random.seed(seed)


    #read from file
    filepath = "nobel-eu.txt"
    nodes = input(filepath)


    minPathLength = []
    averagePathLength = []
    maxPathLength = []
    optimalSolution = []

    for i in range(N_RUNS):

        #select start and end at random (must be different)
        startNodeName = random.choice(list(nodes.keys()))
        endNodeName = startNodeName
        while startNodeName == endNodeName:
            endNodeName = random.choice(list(nodes.keys()))

        #print info about selected nodes
        print(i, startNodeName, endNodeName)

        #calculate optimal
        distance = bfs(nodes, startNodeName)
        optimalSolution.append(distance[endNodeName])

        #calculate aco
        currentMinPathLength, currentAveragePathLength, currentMaxPathLength = aco(nodes, startNodeName, endNodeName, BFS)
        
        #add to final results
        minPathLength.append(currentMinPathLength)
        averagePathLength.append(currentAveragePathLength)
        maxPathLength.append(currentMaxPathLength)

    #draw plot
    createSummary(minPathLength, averagePathLength, maxPathLength, optimalSolution, seed, BFS)




if __name__ == "__main__":
    main()