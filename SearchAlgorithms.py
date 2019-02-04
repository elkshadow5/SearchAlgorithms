class GridPoint:
    def __init__(self, let, color):
        self.let = let
        self.color = color
        self.neighbors = []
    
    def addNeighbors(self, neighbor):
        self.neighbors.append(neighbor)
    
    def __repr__(self):
        return self.let + " --- " + "[" + ', '.join(self.neighbors) + "]"


class Search:
    def __init__(self):
        #basic list of colors to try. Will only work if enough colors fro problem
        self.colors = ["red", "green","blue","cyan","yellow","magenta","black"]
        self.map = [("r1", "r2"), ("r1", "r3"), ("r2", "r4"), ("r3", "r4")]
        self.grid = []
        added = []
        for adj in self.map:
            for grdpt in adj:
                if grdpt not in added:
                    added.append(grdpt)
                    self.grid.append(GridPoint(grdpt,"black"))
        for grdpt in self.grid:
            for adj in self.map:
                if grdpt.let == adj[0]:
                    grdpt.addNeighbors(adj[1])
                elif grdpt.let == adj[1]:
                    grdpt.addNeighbors(adj[0])
    
    # SEARCH ALGORITHMS #
    def breadth(self):
        return 0
    
    def depth(self):
        return 0
    
    def idfs(self):
        return 0
    
    def printState(self):
        for pt in self.grid:
            print(pt)
            print()  # new line


search = Search()
search.printState()
