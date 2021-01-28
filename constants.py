# Metrics
BFS = 0
DIJKSTRA = 1


# Modes - interactive mode requires OpenCV
INTERACTIVE = 0
TEST = 1



# Main settings
mode = INTERACTIVE
N_RUNS = 100
metric = DIJKSTRA

USE_TIME_AS_SEED = False
SEED = 7



# Aco
ALPHA = 1.0
BETA = 1.0
PHEROMONE_EVAPORATION_COEFFICIENT = 0.9
PHEROMONE_INITIALIZATION_VALUE = 1.0
Q = 1.0
N_EPOCHS = 200
N_ANTS = 1000



# Visualization - requires OpenCV:
SHOW_MAP = True
RECORD_VIDEO = False

IMAGE_WIDTH = 965
IMAGE_HEIGHT = 1024
CLICK_PIXEL_DISTANCE = 10



# Other
INFINITY = 10**10