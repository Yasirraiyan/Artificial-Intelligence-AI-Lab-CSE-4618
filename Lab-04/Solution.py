from util import manhattanDistance
from game import Directions
import random, util
from game import Agent

class ReflexAgent(Agent):
    """
    A reflex agent that chooses actions by evaluating the successor state.
    """

    def getAction(self, gameState):
        legalMoves = gameState.getLegalActions()
        scores = [self.evaluationFunction(gameState, action) for action in legalMoves]
        bestScore = max(scores)
        bestIndices = [index for index in range(len(scores)) if scores[index] == bestScore]
        chosenIndex = random.choice(bestIndices)
        return legalMoves[chosenIndex]

    def evaluationFunction(self, currentGameState, action):
        successorGameState = currentGameState.generatePacmanSuccessor(action)
        newPos = successorGameState.getPacmanPosition()
        newFood = successorGameState.getFood()
        newGhostStates = successorGameState.getGhostStates()

        foodList = newFood.asList()
        ghostDistances = [manhattanDistance(newPos, ghost.getPosition()) for ghost in newGhostStates]

        score = successorGameState.getScore()

        if ghostDistances and min(ghostDistances) <= 1:
            score -= 500

        if foodList:
            minFoodDist = min([manhattanDistance(newPos, food) for food in foodList])
            score += 10 / (minFoodDist + 1)

        return score

class MultiAgentSearchAgent(Agent):
    """
    This class provides common elements to all multi-agent searchers.
    """

    def __init__(self, evalFn='scoreEvaluationFunction', depth='2'):
        self.index = 0  # Pacman is always agent index 0
        self.evaluationFunction = util.lookup(evalFn, globals())
        self.depth = int(depth)

class MinimaxAgent(MultiAgentSearchAgent):
    """
    Your minimax agent (question 2)
    """

    def getAction(self, gameState):
        def minimax(agentIndex, depth, state):
            if state.isWin() or state.isLose() or depth == self.depth:
                return self.evaluationFunction(state)

            numAgents = state.getNumAgents()

            if agentIndex == 0:  # Pacman = MAX
                bestScore = float('-inf')
                bestAction = None
                for action in state.getLegalActions(agentIndex):
                    successor = state.generateSuccessor(agentIndex, action)
                    score = minimax(1, depth, successor)
                    if score > bestScore:
                        bestScore = score
                        bestAction = action
                if depth == 0:
                    return bestAction
                else:
                    return bestScore

            else:  # Ghosts = MIN
                nextAgent = agentIndex + 1
                nextDepth = depth
                if nextAgent == numAgents:
                    nextAgent = 0
                    nextDepth += 1

                bestScore = float('inf')
                for action in state.getLegalActions(agentIndex):
                    successor = state.generateSuccessor(agentIndex, action)
                    score = minimax(nextAgent, nextDepth, successor)
                    if score < bestScore:
                        bestScore = score
                return bestScore

        return minimax(0, 0, gameState)

def scoreEvaluationFunction(currentGameState):
    return currentGameState.getScore()
