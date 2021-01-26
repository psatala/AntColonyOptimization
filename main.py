from input import input
from bfs import bfs
from aco import aco
from constants import BFS

def main():
    #read from file
    filepath = "nobel-eu.txt"
    nodes = input(filepath)

    #BFS algorithm
    distance = bfs(nodes, "Warsaw")
    for key, value in distance.items():
        print(str(key) + ": " + str(value))
    
    aco(nodes, "Warsaw", "London", BFS)



if __name__ == "__main__":
    main()