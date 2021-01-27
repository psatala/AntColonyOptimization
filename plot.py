import matplotlib.pyplot as plt
from constants import *
from datetime import datetime


def createSummary(minPathLength, averagePathLength, maxPathLength, optimalSolution, seed, mode):
    filename = "results/"+datetime.now().strftime("%Y_%m_%d_%H_%M_%S") + '.png'
    file = open(filename[:-3]+"txt","w")
    file.write("Plot: "+str(filename)+'\n')
    file.write("Optimal solution:\t")
    for i in range(N_RUNS):
        file.write(str(optimalSolution[i])+"\t")
    file.write('\n')
    file.write("Final shortest path length:\t")
    for i in range(N_RUNS):
        file.write(str(minPathLength[i][N_EPOCHS-1])+"\t")
    file.write('\n')
    file.write("Final average path length:\t")
    for i in range(N_RUNS):
        file.write(str(averagePathLength[i][N_EPOCHS-1])+"\t")
    file.write('\n')
    file.write("Final longest path length:\t")
    for i in range(N_RUNS):
        file.write(str(maxPathLength[i][N_EPOCHS-1])+"\t")
    file.write('\n')
    file.write('Seed: '+str(seed)+'\n')
    file.close()

    suptitle = "Mode: "
    if mode == DIJKSTRA:
        suptitle += "Dijkstra,"
    else:
        suptitle += "BFS,"

    suptitle += " Alpha: " + str(ALPHA) + ", Beta: " + str(BETA) + ", Pheromone evaporation coefficient: " + str(PHEROMONE_EVAPORATION_COEFFICIENT) + \
        ", Pheromone init value: " + str(PHEROMONE_INITIALIZATION_VALUE) + ", Q: " + str(Q)

    plotSummary(minPathLength, averagePathLength, maxPathLength, optimalSolution, suptitle, filename)




def plotSummary(min, avgg, max, optimal, suptitle, filename):
    x = range(N_EPOCHS)
    opt = [1 for i in range(N_EPOCHS)]

    #normalize
    for i in range(N_RUNS):
        for j in range(N_EPOCHS):
            min[i][j] /= optimal[i]
            avgg[i][j] /= optimal[i]
            max[i][j] /= optimal[i]


    minVal = avgColumns(min)
    avgVal = avgColumns(avgg)
    maxVal = avgColumns(max)
    plt.plot(x, minVal, label = "Shortest path length")  
    plt.plot(x, avgVal, label = "Average path length") 
    plt.plot(x, maxVal, label = "Longest path length") 
    plt.plot(x, opt, label = "Optimal solution") 

    plt.xlabel('Epoch')
    plt.ylim(0.8, 3)
    plt.ylabel('Path length') 
    plt.title('Average of '+str(N_RUNS)+' runs with a population of '+str(N_ANTS)+' ants')
    plt.suptitle(suptitle)
    plt.legend()
    savePlot(plt, filename)
    plt.show()


def avgColumns(x):
    output = []
    a = len(x)
    b = len(x[0])
    for i in range(b):
        sum = 0
        for j in range(a):
            sum += x[j][i]
        output.append(sum/a)
    return output

def savePlot(plt, filename):
    figure = plt.gcf() # get current figure
    figure.set_size_inches(10.8, 7.2)
    plt.savefig(filename, bbox_inches='tight', dpi=120)

    