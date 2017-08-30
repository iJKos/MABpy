import numpy as np

class MultiArmedBanditBase(object):

    def __init__(self, num_bandits=3, probs=None, payouts=None, live=True,
                 stop_criterion={'criterion': 'regret', 'value': 0.1}):
        return