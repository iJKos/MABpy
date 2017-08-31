import pandas as pd

from MAB.base import IteractionModel

class Game(IteractionModel):

    _gamelogs = []
    _iter = 0
    _sum_reward = 0
    _sum_regret = 0
    _sum_best_action = 0

    def __init__(self, gameenviroment, agent, verbose = 0):
        self.gameEnviroment = gameenviroment
        self.agent = agent
        self._verbose = verbose
        pass


    def Reset(self):
        self.gameEnviroment.init()
        self._gamelogs = []
        self._iter = 0
        self._sum_reward = 0
        self._sum_regret = 0
        self._sum_best_action = 0

    def Play(self, max_iter):
        self.Reset()

        if self._verbose:
            print("Init Game enviroment")

        while not self.gameEnviroment.done and self._iter<=max_iter:

            if self._verbose:
                print("Game Step")

            state = self.gameEnviroment.publicState
            action=self.agent.MakeDecision(state)
            reward=self.gameEnviroment.getReward(action)
            self.agent.Learn(action,reward,state)

            best_action = self.gameEnviroment.getBestAction()
            best_reward = self.gameEnviroment.getBestReward()

            regret = best_reward-reward
            best_action_flag = 1 if action==best_action else 0
            self._sum_regret+=regret
            self._sum_reward += reward
            self._sum_best_action += best_action_flag


            self._gamelogs.append({"Iter":self._iter
                                   ,"Reward":reward
                                   ,"Action":action
                                   ,"Best_action_flag": best_action_flag
                                   ,"Regret": best_reward - reward
                                   ,"Sum_best_action": self._sum_best_action
                                   ,"Sum_reward":self._sum_reward
                                   ,"Sum_regret":self._sum_regret
                                   ,"Avg_reward": self._sum_reward/(self._iter+1)
                                   ,"Avg_regret": self._sum_regret/(self._iter+1)
                                   ,"Avg_best_action": self._sum_best_action / (self._iter + 1)
                                   })

            self._iter += 1

        return self.GetGameLogs()

    def GetGameLogs(self):
        return pd.DataFrame.from_dict(self._gamelogs)


class Competition(IteractionModel):

    _gamelogs = []
    _games = {}

    def __init__(self, gameenviroment, agent, verbose=0):
        self.gameEnviroment = gameenviroment
        self.agent = agent
        self._verbose = verbose
        pass

    def Reset(self):
        super().Reset()

    def GetGameLogs(self):
        super().GetGameLogs()

    def Play(self, max_iter):
        super().Play(max_iter)