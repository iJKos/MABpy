from abc import abstractmethod, ABCMeta


class IteractionModel(object, metaclass=ABCMeta):

    _verbose = 0

    def __init__ (self,verbose=0):
        self._verbose=verbose
        pass

    @abstractmethod
    def Reset(self):
        pass

    @abstractmethod
    def GetGameLogs(self):
        pass

    @abstractmethod
    def Play(self, max_iter):
        pass


class Agent(metaclass=ABCMeta):
    """
    Base agent class. Agent makes decisions based on algorithm
    """
    @abstractmethod
    def __init__(self,verbose=0):
        self.verbose = verbose
        pass

    @abstractmethod
    def MakeDecision(self,Params):
        """
        Main function for decision.
        :param state: Game enviroment params.
        :return:
        action num
        """
        return 0

    def Learn(self,action,reward,state):
        pass


class GameEnviroment(metaclass=ABCMeta):

    done = False
    publicState = {}

    @abstractmethod
    def __init__(self):
        self.init()
        pass

    def init(self):
        self.done = False
        pass

    @abstractmethod
    def getReward(self,action):
        return 0

    @abstractmethod
    def getBestAction(self):
        return 0

    @abstractmethod
    def getBestReward(self):
        return 0