import cv2  
  

class Vis:

    def __init__(self, nodes):
        self.path = 'doc/images/visMap1.png'
        self.image = cv2.imread(self.path)
        cv2.namedWindow("Map", cv2.WINDOW_NORMAL)
        cv2.resizeWindow('Map', 800,800)
        for key, value in nodes.items():
            cv2.circle(self.image, (value.imgX, value.imgY), 8, (0, 0, 0), -1)
        self.nodes = nodes


    def visualize(self, pheromone):
        tempImg = self.image[:,:].copy()
        maxPheromone = 0
        for key in pheromone:
            if pheromone[key] > maxPheromone:
                maxPheromone = pheromone[key]
        for key, value in self.nodes.items():
            for link in value.links:
                if len(link.name) < 5:
                    color = (pheromone[link.name] + pheromone[link.name+'_reverse']) * 255.0 / maxPheromone
                    thickness = color*2.0 / 255.0 + 4.0
                    if color > 255:
                        color = 255
                    cv2.line(tempImg, (self.nodes[link.firstEndpoint].imgX, self.nodes[link.firstEndpoint].imgY),
                                (self.nodes[link.secondEndpoint].imgX, self.nodes[link.secondEndpoint].imgY), (0, 0, color), int(thickness))
        cv2.imshow("Map", tempImg) 
        cv2.waitKey(0)  
        #cv2.destroyAllWindows()  