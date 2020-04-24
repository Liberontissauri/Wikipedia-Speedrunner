

class Database:
    def __init__(self):
        self.path = []
        self.links = []
    
    def addlink(self,link):
        self.links.append(link)
        self.path.append([link])

    def addpath(self,pathtolink,link):
        if link not in self.links:
            self.addlink(link)

        for path in self.path:
            if path[0] == link:  # Every path's first element is the link of the destination of the path.
                path.append(pathtolink)

    def getpaths(self,link):
        pass # to be added