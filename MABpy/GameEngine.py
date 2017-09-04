import pandas as pd

from MABpy.base import IteractionModel, Agent

class Game(IteractionModel):
    """
    Base Game class.

    Attributes:
        _gamelogs - game logs
        _agents - agents

    """
    _gamelogs = []
    _agents = {}

    def __init__(self, gameenviroment, agent, verbose = 0):
        super().__init__( verbose)

        self.gameEnviroment = gameenviroment

        if isinstance(agent, Agent):
            self._agents["agent"] = agent
        elif isinstance(agent, dict):
            self._agents = agent

        self._gamelogs = []

        pass


    def Reset(self):
        self._gamelogs = []

    def Play(self, max_iter, repeats = 1):

        for n_repeat in range(repeats):

            for agent_name,agent in self._agents.items():

                iter = 0
                sum_reward = 0
                sum_regret = 0
                sum_best_action = 0
                self.gameEnviroment.reset()
                agent.initEnviromentParams(self.gameEnviroment.params)
                best_avg_reward = self.gameEnviroment.getBestAvgReward()

                if self._verbose:
                    print("Agent %s game %d of %d" % (agent_name, n_repeat,repeats))

                while not self.gameEnviroment.done and iter<max_iter:

                    action=agent.MakeDecision()
                    reward=self.gameEnviroment.getReward(action)
                    agent.Learn(action,reward)

                    best_action = self.gameEnviroment.getBestAction()
                    best_reward = self.gameEnviroment.getBestReward()

                    best_action_flag = 1 if action==best_action else 0
                    sum_reward += reward
                    regret = best_reward - reward
                    sum_pseudo_regret = best_avg_reward * (iter+1) - sum_reward
                    sum_regret += regret
                    sum_best_action += best_action_flag


                    self._gamelogs.append({"Iter":iter
                                           ,"Reward":reward
                                           ,"Action":action
                                           ,"Best_action_flag": best_action_flag
                                           ,"Regret": regret
                                           ,"Sum_best_action": sum_best_action
                                           ,"Sum_reward":sum_reward
                                           ,"Sum_regret":sum_regret
                                           ,"Sum_pseudo_regret": sum_pseudo_regret
                                           ,"Avg_reward": sum_reward/(iter+1)
                                           ,"Avg_regret": sum_regret/(iter+1)
                                           ,"Avg_pseudo_regret": sum_pseudo_regret / (iter + 1)
                                           ,"Avg_best_action": sum_best_action / (iter + 1)
                                           ,"Agent" : agent_name
                                           ,"N_repeat": n_repeat
                                           })

                    iter += 1

        return self.GetGameLogs()

    def GetGameLogs(self):
        return pd.DataFrame.from_dict(self._gamelogs)

