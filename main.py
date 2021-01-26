from input import input
from bfs import bfs
from aco import aco
from constants import BFS, DIJKSTRA
from dijkstra import dijkstra

def main():
    #read from file
    filepath = "nobel-eu.txt"
    nodes = input(filepath)

    #BFS algorithm
    #distance = bfs(nodes, "Warsaw")

    #Dijkstra algorithm
    distance = dijkstra(nodes, "Warsaw")

    for key, value in distance.items():
        print(str(key) + ": " + str(value))
    
    aco(nodes, "Warsaw", "Madrid", DIJKSTRA)



if __name__ == "__main__":
    main()