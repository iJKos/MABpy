import numpy as np

from MABpy.base import Agent

class RandomAgent(Agent):
    """
    Choose random action and never learn
    """
    def _makeDesicion(self,context=None):
        return np.random.random_integers(low=0,high=self._envParams["N_bandits"]-1)


class SimpleAgent(Agent):

    def __init__(self,optimistic=0,verbose=0,):
        super().__init__(verbose)
        self._optimistic = optimistic
        pass

    def initEnviromentParams(self, params):
        super().initEnviromentParams(params)

        self._qreward = [self._optimistic for i in self._envParams["ActionRange"] ]
        self._qtry = [0 for i in self._envParams["ActionRange"]]
        self._iter = 0

    def _makeDesicion(self,context=None):
        return np.argmax(self._qreward)

    def _learn(self,action,reward,context=None):
        self._iter+=1
        self._qtry[action]+=1
        self._qreward[action] = (self._qreward[action]*(self._qtry[action]-1)+reward) / self._qtry[action]


class eGreedyAgent(SimpleAgent):


    def __init__(self, greedy=0.1, optimistic=0,verbose=0):
        super().__init__(optimistic,verbose)
        self._greedy = greedy

        if greedy>=1 or greedy<=0:
            raise ValueError("greedy must be between 0 and 1")

    def _makeDesicion(self,context=None):
        action = super()._makeDesicion()
        e = np.random.rand()
        return action if e>self._greedy else  np.random.random_integers(low=0,high=self._envParams["N_bandits"]-1)

class enGreedyAgent(SimpleAgent):


    def __init__(self, c=0.1, d=1.0, optimistic=0,verbose=0):
        super().__init__(optimistic,verbose)
        self._c = c
        self._d = d

        if d>1 or d<=0:
            raise ValueError("greedy must be between 0 and 1")

    def _makeDesicion(self,context=None):
        action = super()._makeDesicion()
        e = np.random.rand()
        en = self._c*self._envParams["N_bandits"]/(self._d*self._d*(self._iter+1))
        en = 1 if en >1 else en
        return action if e>en else  np.random.random_integers(low=0,high=self._envParams["N_bandits"]-1)

class UCB1Agent(SimpleAgent):

    def __init__(self, optimistic=0, c=1.5, verbose=0):
        super().__init__(optimistic, verbose)
        self._c = c

    def _makeDesicion(self):
        if self._iter<self._envParams["N_bandits"]:
            return self._iter
        return np.argmax(self._qreward + self._c* np.sqrt(2*np.log(self._iter+1)/self._qtry) )

class UCB2Agent(SimpleAgent):

    def __init__(self, optimistic=0, a=0.01, verbose=0):
        super().__init__(optimistic, verbose)
        self._a = a

        if a>1 or a<=0:
            raise ValueError("a must be between 0 and 1")

    def initEnviromentParams(self, params):
        super().initEnviromentParams(params)
        self._r = [0 for i in self._envParams["ActionRange"]]

    def _makeDesicion(self):
        if self._iter<self._envParams["N_bandits"]:
            return self._iter


        if self._iter>self._envParams["N_bandits"]:
            if self._steps_to_play>0:
                self._steps_to_play-=1
                return self._action_to_play
            else:
                self._r[self._action_to_play]+=1



        action = np.argmax(self._qreward + self._af(self._iter+1,self._r) )

        self._steps_to_play = self._tf(self._r[action]+1)-self._tf(self._r[action]) -1
        self._action_to_play = action

        return action

    def _af(self,n,r):
        return np.sqrt( (1+self._a)*np.log(np.e*n/self._tf(r))/(2*self._tf(r)) )

    def _tf(self,r):
        return np.ceil( np.power (1+self._a,r))