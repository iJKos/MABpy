from abc import abstractmethod, ABCMeta
import numpy as np

class IteractionModel(object, metaclass=ABCMeta):
    """
    Base class for agents-enviroments iteraction

    Attributes:
        _verbose - verbosity level
    """
    _verbose = 0

    def __init__ (self,verbose=0):
        """
        Class initialization
        :param verbose: verobosity level
        """
        self._verbose=verbose
        pass

    @abstractmethod
    def Reset(self):
        """
        Reset iteraction to init
        """
        pass

    @abstractmethod
    def GetGameLogs(self):
        """
        Get game logs
        :return: game logs
        """
        pass

    @abstractmethod
    def Play(self, max_iter):
        """
        start iteraction
        :param max_iter: maximum iteration number
        :return:
        """
        pass


class Agent(metaclass=ABCMeta):
    """
    Base agent class.
    Agent makes decisions based on algorithm

    Attributes:
        _verbose - verbosity level
        _envParams - enviroment parametes
    """
    _verbose=0
    _envParams = None



    def __init__(self,verbose=0):
        """
        class initisialization with verbosity level
        :param verbose: verbosity level
        """
        self._verbose = verbose
        pass


    def initEnviromentParams(self, params):
        """
        Save enviroment parameters
        :param params: enviroment params
        :return: nothing
        """
        self._envParams = params

    def _beforeMakingDesicion(self,context=None):
        if self._envParams is None:
            raise ValueError("can't make decision, initEnviromentParams first")


    def _afterMakingDesicion(self,action,context=None):
        pass

    @abstractmethod
    def _makeDesicion(self,context=None):
        return 0

    def MakeDecision(self,context=None):
        self._beforeMakingDesicion(context)
        action = self._makeDesicion()
        self._afterMakingDesicion(action,context)
        return action

    def _beforeLearn(self,action,reward,context=None):
        pass

    def _afterLearn(self,action,reward,context=None):
        pass

    def _learn(self,action,reward,context=None):
        pass

    def Learn(self,action,reward,context=None):
        """
        Main learn function
        :param action: action
        :param reward: reward
        :param context: context vector
        :return: nothing
        """
        self._beforeLearn(action,reward,context)
        self._learn(action,reward,context)
        self._afterLearn(action,reward,context)
        pass

class EnvParams(dict):
    """
    base enviroment
    """
    def __init__(self, n_bandits):
        self["N_bandits"] = n_bandits
        self["ActionRange"] = range(self["N_bandits"])
        pass


class GameEnviroment(metaclass=ABCMeta):
    """
    Base class for game enviroment

    Attributes:
        done - flag for end game
        params - public enviroment params
    """
    done = False
    params = None

    _bestAction = None
    _bestReward = None
    _bestAvgReward = 0

    def __init__(self, n_bandits):
        self.params = EnvParams(n_bandits)

    def _beforeGetReward(self,action):
        if action>=self.params["N_bandits"]:
            raise ValueError("Got action= %d but action must be < N_bandits=%d" % (action, self.params["N_bandits"]))

    def _getReward(self,action):
        return 0

    def _afterGetReward(self,rewards,action):
        self._bestAction = np.argmax(rewards)
        self._bestReward = np.max(rewards)
        pass

    def getReward(self,action):
        self._beforeGetReward(action)
        rewards = [self._getReward(a) for a in self.params["ActionRange"]]
        self._afterGetReward(rewards,action)
        return rewards[action]

    def getRewardSample(self,sample_size=100):
        result = []
        for action in self.params["ActionRange"]:
            subresult = []
            for i in range(sample_size):
                subresult.append(self._getReward(action))
            result.append(subresult)
            self.reset()
        return result

    def getBestReward(self):
        return self._bestReward

    def getBestAction(self):
        return self._bestAction

    def getBestAvgReward(self):
        return self._bestAvgReward

    def reset(self):
        self.done = False
        self._bestAction = None
        self._bestReward = None
        pass
