from MAB.base import GameEnviroment
import numpy as np

class EnvParams(dict):

    def __init__(self, n_bandits):
        self["N_bandits"] = n_bandits
        self["ActionRange"] = range(self["N_bandits"])
        pass

class NArmedBanditEnviroment(GameEnviroment):

    def __init__(self, n_bandits):
        self.publicState = EnvParams(n_bandits)
        super().__init__()

    def getActionsList(self):
        return range(self.publicState["N_bandits"])

    def getReward(self,action):
        if action>=self.publicState["N_bandits"]:
            raise ValueError("Got action= %d but action must be < N_bandits=%d" % (action, self.publicState["N_bandits"]))


class DummyEnviroment(NArmedBanditEnviroment):

    def getReward(self, action):
        super().getReward(action)
        return action


    def getBestAction(self):
        return self.publicState["N_bandits"]-1


    def getBestReward(self):
        return self.publicState["N_bandits"]



class GaussianEnviroment(NArmedBanditEnviroment):

    _mu = []
    _sigma = []

    def __init__(self, n_bandits, min_mu, max_mu, min_sigma, max_sigma):
        super().__init__(n_bandits)
        #np.random.uniform(min_mu,max_mu,


    def getReward(self, action):
        return super().getReward(action)

    def getBestAction(self):
        return super().getBestAction()

    def getBestReward(self):
        return super().getBestReward()