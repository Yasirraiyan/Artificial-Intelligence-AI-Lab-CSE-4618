from game import *
from learningAgents import ReinforcementAgent
from featureExtractors import *
import random, util, math

class QLearningAgent(ReinforcementAgent):
    def __init__(self, **args):
        ReinforcementAgent.__init__(self, **args)
        self.qValues = util.Counter()

    def getQValue(self, state, action):
        return self.qValues[(state, action)]

    def computeValueFromQValues(self, state):
        legalActions = self.getLegalActions(state)
        if not legalActions:
            return 0.0
        return max([self.getQValue(state, a) for a in legalActions])

    def computeActionFromQValues(self, state):
        legalActions = self.getLegalActions(state)
        if not legalActions:
            return None
        maxQ = self.computeValueFromQValues(state)
        bestActions = [a for a in legalActions if self.getQValue(state, a) == maxQ]
        return random.choice(bestActions)

    def getAction(self, state):
        legalActions = self.getLegalActions(state)
        if not legalActions:
            return None
        if util.flipCoin(self.epsilon):
            return random.choice(legalActions)
        else:
            return self.computeActionFromQValues(state)

    def update(self, state, action, nextState, reward):
        sample = reward + self.discount * self.computeValueFromQValues(nextState)
        self.qValues[(state, action)] = (1 - self.alpha) * self.getQValue(state, action) + self.alpha * sample

    def getPolicy(self, state):
        return self.computeActionFromQValues(state)

    def getValue(self, state):
        return self.computeValueFromQValues(state)

class PacmanQAgent(QLearningAgent):
    def __init__(self, epsilon=0.05,gamma=0.8,alpha=0.2,numTraining=0, **args):
        args['epsilon'] = epsilon
        args['gamma'] = gamma
        args['alpha'] = alpha
        args['numTraining'] = numTraining
        self.index = 0
        QLearningAgent.__init__(self, **args)

    def getAction(self, state):
        action = QLearningAgent.getAction(self,state)
        self.doAction(state,action)
        return action

class ApproximateQAgent(PacmanQAgent):
    def __init__(self, extractor='IdentityExtractor', **args):
        self.featExtractor = util.lookup(extractor, globals())()
        PacmanQAgent.__init__(self, **args)
        self.weights = util.Counter()

    def getWeights(self):
        return self.weights

    def getQValue(self, state, action):
        features = self.featExtractor.getFeatures(state, action)
        return sum(self.weights[f] * value for f, value in features.items())

    def update(self, state, action, nextState, reward):
        features = self.featExtractor.getFeatures(state, action)
        difference = (reward + self.discount * self.computeValueFromQValues(nextState)) - self.getQValue(state, action)
        for f, value in features.items():
            self.weights[f] += self.alpha * difference * value

    def final(self, state):
        PacmanQAgent.final(self, state)
        if self.episodesSoFar == self.numTraining:
            pass
