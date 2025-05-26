import util
  class SearchProblem:
   
 def getStartState(self):
       
        util.raiseNotDefined()

    def isGoalState(self, state):
      
        util.raiseNotDefined()

    def getSuccessors(self, state):
     
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
       
        util.raiseNotDefined()


def tinyMazeSearch(problem):
  
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    
    startingNode = problem.getStartState()
    if problem.isGoalState(startingNode):
        return []
    
   
    dfsstack = util.Stack()
    visitedNodes = []
    
    dfsstack.push((startingNode, []))
    

    while not dfsstack.isEmpty():
        currentNode, actions = dfsstack.pop()
        if currentNode not in visitedNodes:
            visitedNodes.append(currentNode)

            if problem.isGoalState(currentNode):
                return actions
            
            for nextNode, action, cost in problem.getSuccessors(currentNode):
                nwAction = actions + [action]
                dfsstack.push((nextNode, nwAction))

    #util.raiseNotDefined()

def breadthFirstSearch(problem):
   
    startingNode = problem.getStartState()
    if problem.isGoalState(startingNode):
        return []
    
   
    bfsQueue = util.Queue()
    visitedNodes = []
    
    bfsQueue.push((startingNode, []))
    

    while not bfsQueue.isEmpty():
        currentNode, actions = bfsQueue.pop()
        if currentNode not in visitedNodes:
            visitedNodes.append(currentNode)

            if problem.isGoalState(currentNode):
                return actions
            
            for nextNode, action, cost in problem.getSuccessors(currentNode):
                nwAction = actions + [action]
                bfsQueue.push((nextNode, nwAction))
    
    #util.raiseNotDefined()

def uniformCostSearch(problem):
 
    startingNode = problem.getStartState()
    util.raiseNotDefined()

def nullHeuristic(state, problem=None):

    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
  
    util.raiseNotDefined()


