from input import input as fileinput
from bfs import bfs
from aco import aco
from dijkstra import dijkstra
from constants import *
from plot import createSummary

import numpy as np
import random
import time

if mode == INTERACTIVE:
    from visualization import Vis
    import cv2

def main():

    if mode == INTERACTIVE and SHOW_MAP:
        print("Choose mode:")
        print("i - interactive city choice")
        print("r - random city choice")
        c = input("Mode: ")
        while c != 'r' and c != 'i':
            print("Invalid choice - enter either 'r' or 'i'")
            c = input("Mode: ")

        if c == 'r':
            randomChoice = True
        else:
            randomChoice = False
    else:
        randomChoice = True

    #seed
    if USE_TIME_AS_SEED:
        seed = int(round(time.time()))
    else:
        seed = SEED
    random.seed(seed)


    #read from file
    filepath = "nobel-eu.txt"
    nodes = fileinput(filepath)

    if mode == INTERACTIVE:
        vis = Vis(nodes)


    minPathLength = []
    averagePathLength = []
    maxPathLength = []
    optimalSolution = []

    for i in range(N_RUNS):

        #select start and end at random (must be different)
        if randomChoice:
            startNodeName = random.choice(list(nodes.keys()))
            endNodeName = startNodeName
        else:
            startNodeName, endNodeName, ok = vis.getCities()
            if not ok:
                break

        #calculate optimal
        if metric == BFS:
            distance = bfs(nodes, startNodeName)
        else:
            distance = dijkstra(nodes, startNodeName)

        if randomChoice:
            while startNodeName == endNodeName or (metric == DIJKSTRA and distance[endNodeName] < 1000) or (metric == BFS and distance[endNodeName] < 3):
                endNodeName = random.choice(list(nodes.keys()))

        #print info about selected nodes
        print(i, startNodeName, endNodeName)

        optimalSolution.append(distance[endNodeName])

        #calculate aco
        if mode == INTERACTIVE:
            currentMinPathLength, currentAveragePathLength, currentMaxPathLength, ok = aco(nodes, startNodeName, endNodeName, metric, vis)
            if not ok:
                break
        else:
            currentMinPathLength, currentAveragePathLength, currentMaxPathLength, ok = aco(nodes, startNodeName, endNodeName, metric, 0)

        if not randomChoice:
            cv2.waitKey(0)
        
        #add to final results
        minPathLength.append(currentMinPathLength)
        averagePathLength.append(currentAveragePathLength)
        maxPathLength.append(currentMaxPathLength)

    #draw plot
    if len(minPathLength) > 0:
        createSummary(minPathLength, averagePathLength, maxPathLength, optimalSolution, seed, metric)




if __name__ == "__main__":
    main()