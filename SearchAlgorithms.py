import copy

class GridPoint:
    def __init__(self, let, color):
        self.let = let
        self.color = color
        self.neighbors = []
    
    def addNeighbors(self, neighbor):
        self.neighbors.append(neighbor)

    def hasConflict(self):
        for neighbor in self.neighbors:
            if neighbor.color==self.color:
                return True
        return False
    
    def __repr__(self):
        returnString = self.let+" --- ["
        for neighbor in self.neighbors:
            returnString = returnString+neighbor.let+" "
        returnString+="]"
        return returnString


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
                    for neighbor in self.grid:
                        if neighbor.let==adj[1]:
                            grdpt.addNeighbors(neighbor)
                elif grdpt.let == adj[1]:
                    for neighbor in self.grid:
                        if neighbor.let==adj[0]:
                            grdpt.addNeighbors(neighbor)
    
    # SEARCH ALGORITHMS #
    def breadth(self):
        #USE THIS GRID! Keeps from messing up the later searches
        grid = copy.deepcopy(self.grid)
        return 0
    
    def depth(self):
        grid = copy.deepcopy(self.grid)
        stack = []
        closed = []
        stack.append(grid[0])
        while len(stack)>0:
            point = stack.pop()
            closed.append(point)
            for neighbor in point.neighbors:
                if neighbor not in closed and neighbor not in stack:
                    stack.append(neighbor)
            colorToTry = 0
            point.color = self.colors[colorToTry]
            while point.hasConflict():
                print(point.color)
                colorToTry=colorToTry+1
                point.color = self.colors[colorToTry]

        print("Depth first search result:")
        for point in grid:
            print(str(point)+" color: "+point.color)  
    
    def idfs(self):
        grid = copy.deepcopy(self.grid)
        return 0

    
    def printState(self):
        for pt in self.grid:
            print(pt)
            print()  # new line


search = Search()
search.printState()
search.depth()
