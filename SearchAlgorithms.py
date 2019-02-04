import copy


class GridPoint:
    def __init__(self, let, color):
        self.let = let
        self.color = color
        self.neighbors = []
    
    def addNeighbors(self, neighbor):
        self.neighbors.append(neighbor)
    
    # Returns true if has same color as any of its neighbors
    def hasConflict(self):
        for neighbor in self.neighbors:
            if neighbor.color == self.color:
                return True
        return False
    
    # Returns the name of the node, plus its neighbor nodes
    def __repr__(self):
        returnString = self.let + " --- [ "
        for neighbor in self.neighbors:
            returnString = returnString + neighbor.let + " "
        returnString += "]"
        return returnString
    
    def str(self):
        returnString = self.let + " --- [ "
        for neighbor in self.neighbors:
            returnString = returnString + neighbor.let + " "
        returnString += "]"
        return returnString


class Search:
    def __init__(self, map):
        #basic list of colors to try. Will only work if enough colors for problem
        self.colors = ["red", "green","blue","cyan","yellow","magenta"]
        self.map = map
        self.grid = []
        added = []
        # Create GridPoint Objects
        for adj in self.map:
            for grdpt in adj:
                if grdpt not in added:
                    added.append(grdpt)
                    self.grid.append(GridPoint(grdpt, "black"))
        # Give GridPoints their neighbors
        for grdpt in self.grid:
            for adj in self.map:
                if grdpt.let == adj[0]:
                    for neighbor in self.grid:
                        if neighbor.let == adj[1]:
                            grdpt.addNeighbors(neighbor)
                elif grdpt.let == adj[1]:
                    for neighbor in self.grid:
                        if neighbor.let == adj[0]:
                            grdpt.addNeighbors(neighbor)
    
    def dequeue(self, arr):
        if len(arr) > 0:
            return True, arr.pop(0)
        return False
    
    def enqueue(self, arr, point):
        arr.insert(len(arr), point)
        return True
    
    # SEARCH ALGORITHMS #
    def breadth(self):
        # USE THIS GRID! Keeps from messing up the later searches
        grid = copy.deepcopy(self.grid)
        queue = []
        closed = []
        self.enqueue(queue, grid[0])
        
        # Start going through the queue
        while not self.reachedEndCondition(grid):
            curr_node = queue[0]
            print("\tSearching node " + curr_node.let + "...")
            for neighbor in curr_node.neighbors:
                self.enqueue(queue, neighbor)
            
            # Go through the list of colors until get one so its different
            #  than any of its neighbors' colors
            colorToTry = 0
            curr_node.color = self.colors[colorToTry]
            while curr_node.hasConflict():
                colorToTry += 1
                curr_node.color = self.colors[colorToTry]
            pop = self.dequeue(queue)
            if pop:
                closed.append(pop[1])
        
        # print the results
        print("Breadth first search result:")
        for point in grid:
            print("\t" + point.let + " color: " + point.color)
        
        # end breadth-first search algorithm
    
    def depth(self):
        print("\nDepth first searching: ")
        # Setup. Perform deep copy to preserve main grid
        grid = copy.deepcopy(self.grid)
        stack = []
        closed = []
        stack.append(grid[0])
        
        # Start going through the stack
        while not self.reachedEndCondition(grid):
            #if stack is empty, failed
            if len(stack)==0:
                break
            point = stack.pop()
            closed.append(point)
            print("\tNow working with node " + point.let + "...")
            # Add neighbors to the stack, assuming they haven't been
            #  visited or are already there
            for neighbor in point.neighbors:
                if neighbor not in closed and neighbor not in stack:
                    stack.append(neighbor)
            
            # Go through the list of colors until get one so its different
            #  than any of its neighbors' colors
            colorToTry = 0
            point.color = self.colors[colorToTry]
            while point.hasConflict():
                colorToTry += 1
                point.color = self.colors[colorToTry]
        
        print("Depth first search result:")
        #Print the solution, if found
        self.printSolution(grid)
    
    def idfs(self, minDepth, maxDepth):
        print("\nIterative Depth first searching: ")
        #Setup. Perform deep copy to preserve main grid
        grid = copy.deepcopy(self.grid)

        #Iterate through the various depths
        for depth in range(minDepth,maxDepth) :
            #Before resetting, check to see if solution was found on last iteration
            if self.reachedEndCondition(grid):
                break
            
            #Reset for new depth
            grid = copy.deepcopy(self.grid)
            stack = []
            closed = []
            stack.append(grid[0])
            currentDepth = 0
            print("\tNow working up to a depth of "+str(depth)+":")

            #Start going through the stack
            while not self.reachedEndCondition(grid):
                #if stack is empty, failed
                if len(stack)==0:
                    break
                point = stack.pop()
                closed.append(point)
                print("\t\tNow working with node "+point.let+"...")
                #Add neighbors to the stack, assuming they haven't been
                #  visited, are already there, or depth limit reached
                if currentDepth<depth:
                    for neighbor in point.neighbors:
                        if neighbor not in closed and neighbor not in stack:
                            stack.append(neighbor)
                currentDepth+=1
                
                #Go through the list of colors until get one so its different
                #  than any of its neighbors' colors
                colorToTry = 0
                point.color = self.colors[colorToTry]
                while point.hasConflict():
                    colorToTry+=1
                    point.color = self.colors[colorToTry]

        print("Iterative Depth first search result:")
        #Print solution, if found
        self.printSolution(grid)

    #Print out solution, if found
    def printSolution(self,grid):
        resultFound = "!!!NO SOLUTION FOUND!!!"
        if self.reachedEndCondition(grid):
            resultFound = "Solution found:"
        print("\t"+resultFound)
        for point in grid:
            print("\t"+point.let+" color: "+point.color)

    #Check to see if every point has a color and there are no conflicts
    def reachedEndCondition(self, gridIn):
        for point in gridIn:
            if point.hasConflict() or point.color == "black":
                return False
        return True
    
    def printState(self):
        print("\nMap in:")
        for pt in self.grid:
            print(pt)
        print("")

#Put map here:
    #BASIC TEST
search = Search([("r1", "r2"), ("r1", "r3"), ("r2", "r4"), ("r3", "r4")])
    #ADVANCED TEST
#search = Search([("r1", "r2"), ("r1", "r3"), ("r2", "r4"), ("r3", "r4"),("r3", "r5"),("r5", "r4"),("r5", "r6")])
#Print out the map
search.printState()
# Show the breadth first searching
search.breadth()
#Show the depth first searching
search.depth()
#Show IDFS. First number is minimum depth, second is maximum depth
search.idfs(1,3)
