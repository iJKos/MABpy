from MABpy.base import GameEnviroment
import numpy as np


class DummyEnviroment(GameEnviroment):

    def __init__(self, n_bandits):
        super().__init__(n_bandits)
        self._bestAvgReward = n_bandits-1

    def _getReward(self, action):
        return action



class GaussianEnviroment(GameEnviroment):

    _mu = []
    _sigma = []

    def __init__(self, n_bandits, min_mu=0, max_mu=1, min_sigma=1, max_sigma=1):
        super().__init__(n_bandits)
        self._mu = np.random.uniform(min_mu,max_mu,n_bandits)
        self._sigma = np.random.uniform(min_sigma, max_sigma, n_bandits)
        self._bestAvgReward = np.max(self._mu)

    def _getReward(self, action):
        return np.random.normal(self._mu[action],self._sigma[action],1)[0]



class BernoulliEnviroment(GameEnviroment):

    _p = []

    def __init__(self, n_bandits):
        super().__init__(n_bandits)
        self._p = np.random.uniform(size=n_bandits)
        self._bestAvgReward =  np.max(self._p)

    def __init__(self, p):
        super().__init__(len(p))
        self._p = p
        self._bestAvgReward =  np.max(self._p)


    def _afterGetReward(self,rewards,action):
        self._bestAction = np.argmax(self._p)
        self._bestReward = 1
        pass

    def _getReward(self, action):
        return 1 if np.random.rand()<=self._p[action] else 0
