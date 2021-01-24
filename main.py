from input import input
from bfs import bfs

def main():
    #read from file
    filepath = "nobel-eu.txt"
    nodes = input(filepath)

    #BFS algorithm
    distance = bfs(nodes, "Warsaw")
    for key, value in distance.items():
        print(str(key) + ": " + str(value))




if __name__ == "__main__":
    main()