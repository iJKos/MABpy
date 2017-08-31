import numpy as np

from MAB.base import Agent

class DummyAgent(Agent):

    def __init__(self,verbose=0):
        super().__init__(verbose)
        pass

    def MakeDecision(self, Params):
        actionList = Params["ActionRange"]
        return np.random.random_integers(low=0,high=len(actionList)-1)
