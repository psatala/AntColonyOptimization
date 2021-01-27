from input import input
from bfs import bfs
from aco import aco
from dijkstra import dijkstra
from constants import *
from plot import createSummary

import numpy as np
import random
import time

if USE_OPENCV:
    from visualization import Vis
    import cv2

def main():

    #seed
    if USE_TIME_AS_SEED:
        seed = int(round(time.time()))
    else:
        seed = SEED
    random.seed(seed)


    #read from file
    filepath = "nobel-eu.txt"
    nodes = input(filepath)

    if USE_OPENCV:
        vis = Vis(nodes)


    minPathLength = []
    averagePathLength = []
    maxPathLength = []
    optimalSolution = []

    for i in range(N_RUNS):

        #select start and end at random (must be different)
        startNodeName = random.choice(list(nodes.keys()))
        endNodeName = startNodeName

        #calculate optimal
        if mode == BFS:
            distance = bfs(nodes, startNodeName)
        else:
            distance = dijkstra(nodes, startNodeName)

        while startNodeName == endNodeName or distance[endNodeName] < 1000:
            endNodeName = random.choice(list(nodes.keys()))

        #print info about selected nodes
        print(i, startNodeName, endNodeName)

        optimalSolution.append(distance[endNodeName])

        #calculate aco
        if USE_OPENCV:
            currentMinPathLength, currentAveragePathLength, currentMaxPathLength, ok = aco(nodes, startNodeName, endNodeName, mode, vis)
            if not ok:
                return
        else:
            currentMinPathLength, currentAveragePathLength, currentMaxPathLength, ok = aco(nodes, startNodeName, endNodeName, mode, 0)
        
        #add to final results
        minPathLength.append(currentMinPathLength)
        averagePathLength.append(currentAveragePathLength)
        maxPathLength.append(currentMaxPathLength)

    #draw plot
    createSummary(minPathLength, averagePathLength, maxPathLength, optimalSolution, seed, mode)




if __name__ == "__main__":
    main()