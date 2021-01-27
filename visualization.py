import cv2  
from constants import *
from datetime import datetime

  

class Vis:

    def __init__(self, nodes):
        self.path = 'doc/images/visMap1.png'
        self.image = cv2.imread(self.path)
        if SHOW_MAP:
            cv2.namedWindow("Map", cv2.WINDOW_NORMAL)
            cv2.resizeWindow('Map', IMAGE_WIDTH, IMAGE_HEIGHT)
        for key, value in nodes.items():
            cv2.circle(self.image, (value.imgX, value.imgY), 8, (0, 0, 0), -1)
        self.nodes = nodes
        if RECORD_VIDEO:
            fourcc = cv2.VideoWriter_fourcc(*'XVID')
            self.video = cv2.VideoWriter("results/"+datetime.now().strftime("%Y_%m_%d_%H_%M_%S") + '.avi',fourcc,10.0,(IMAGE_WIDTH, IMAGE_HEIGHT))
        self.showMap = SHOW_MAP
        self.mapStepTime = 0

    def __del__(self):
        cv2.destroyAllWindows()
        if RECORD_VIDEO:
            self.video.release()


    def visualize(self, pheromone, startNodeName, endNodeName):
        tempImg = self.image[:,:].copy()
        maxPheromone = 0
        for key in pheromone:
            if pheromone[key] > maxPheromone:
                maxPheromone = pheromone[key]
        for key, value in self.nodes.items():
            for link in value.links:
                if len(link.name) < 5:
                    color = (pheromone[link.name] + pheromone[link.name+'_reverse']) * 255.0 / maxPheromone
                    thickness = color*4.0 / 255.0 + 3.0
                    if color > 255:
                        color = 255
                    cv2.line(tempImg, (self.nodes[link.firstEndpoint].imgX, self.nodes[link.firstEndpoint].imgY),
                                (self.nodes[link.secondEndpoint].imgX, self.nodes[link.secondEndpoint].imgY), (0, 0, color), int(thickness))

        suptitle = "Mode: "
        if mode == DIJKSTRA:
            suptitle += "Dijkstra,"
        else:
            suptitle += "BFS,"

        suptitle += " Alpha: " + str(ALPHA) + ", Beta: " + str(BETA) + ", Evaporation: " + str(PHEROMONE_EVAPORATION_COEFFICIENT)
        suptitle2 = "Pheromone init value: " + str(PHEROMONE_INITIALIZATION_VALUE) + ", Q: " + str(Q)
        cv2.putText(tempImg, suptitle, (10, 30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 0, 0), 2)
        cv2.putText(tempImg, suptitle2, (10, 70), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 0, 0), 2)        
        cv2.putText(tempImg, startNodeName+' to '+endNodeName, (10, 120), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0), 2)
        if RECORD_VIDEO:
            self.video.write(tempImg)

        if self.showMap:
            cv2.putText(tempImg, 'Esc - exit', (10, 160), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 0, 0), 2)
            cv2.putText(tempImg, 's - pause', (10, 200), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 0, 0), 2)
            cv2.putText(tempImg, 'd - play', (10, 240), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 0, 0), 2)
            cv2.putText(tempImg, 'f - 1 frame forward', (10, 280), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 0, 0), 2)
            if self.mapStepTime == 0:
                cv2.putText(tempImg, 'Paused', (10, 330), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 0, 0), 2)
            else:
                cv2.putText(tempImg, 'Playing', (10, 330), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 0, 0), 2)
            cv2.imshow("Map", tempImg)
            c = cv2.waitKey(self.mapStepTime)
            if c == 27:
                return False
            if c == 115:
                self.mapStepTime = 0
            if c == 100:
                self.mapStepTime = 5
        return True
