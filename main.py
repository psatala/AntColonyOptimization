from input import input as fileinput
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
        if not USE_OPENCV:
            print("OpenCV is required to run interactively - set USE_OPENCV to True")
            randomChoice = True
        if not SHOW_MAP:
            print("Showing the map is required to run interactively - set SHOW_MAP to True")
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

    if USE_OPENCV:
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
        if mode == BFS:
            distance = bfs(nodes, startNodeName)
        else:
            distance = dijkstra(nodes, startNodeName)

        if randomChoice:
            while startNodeName == endNodeName or (mode == DIJKSTRA and distance[endNodeName] < 1000) or (mode == BFS and distance[endNodeName] < 3):
                endNodeName = random.choice(list(nodes.keys()))

        #print info about selected nodes
        print(i, startNodeName, endNodeName)

        optimalSolution.append(distance[endNodeName])

        #calculate aco
        if USE_OPENCV:
            currentMinPathLength, currentAveragePathLength, currentMaxPathLength, ok = aco(nodes, startNodeName, endNodeName, mode, vis)
            if not ok:
                break
        else:
            currentMinPathLength, currentAveragePathLength, currentMaxPathLength, ok = aco(nodes, startNodeName, endNodeName, mode, 0)

        if not randomChoice:
            cv2.waitKey(0)
        
        #add to final results
        minPathLength.append(currentMinPathLength)
        averagePathLength.append(currentAveragePathLength)
        maxPathLength.append(currentMaxPathLength)

    #draw plot
    createSummary(minPathLength, averagePathLength, maxPathLength, optimalSolution, seed, mode)




if __name__ == "__main__":
    main()