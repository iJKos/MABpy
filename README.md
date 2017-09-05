Multi-Armed Bandits python library
==================================  

MABpy was created as easy-to-use and extend library for Multi-Armed
Bandits (MAB) problem. According to [wikipedia](https://en.wikipedia.org/wiki/Multi-armed_bandit)
>In probability theory, the multi-armed bandit problem (sometimes 
called the K- or N-armed bandit problem) is a problem in which a 
gambler at a row of slot machines (sometimes known as "one-armed 
bandits") has to decide which machines to play, how many times 
to play each machine and in which order to play them. When played, 
each machine provides a random reward from a probability 
distribution specific to that machine. The objective of 
the gambler is to maximize the sum of rewards earned through 
a sequence of lever pulls.

MABpy provides a hopefully simple API to allow you to explore, test, and use strategies.


Installation
------------
Library is available on [Pypi repository](https://pypi.python.org/pypi/MABpy) 
```sh
pip install MABpy
```

Usage
-----
For basic usage you have to:

1. Import GameEngine, Agents and Enviroment
 
```python
from MAB import GameEngine,ActionRewardAgents as Agents,SimpleMAB
```

2. Init enviroment (bernoulli, for example)
 
```python
Enviroment = SimpleMAB.BernoulliEnviroment([0.1,0.1,0.1,0.1,0.6,0.6,0.6,0.9])
```

3. Init some agents to solve MAB enviroment

```python
agents = {
"Optimistic" : Agents.SimpleAgent(optimistic=1),
"Simple" : Agents.SimpleAgent(optimistic=0),
"Random" : Agents.RandomAgent(),
"enGreedy" : Agents.enGreedyAgent(c=0.5,d=0.9),
"UCB" : Agents.UCB1Agent()
}
```

4.  Start the Game  

```python
Max_steps = 5000
Repeats_count = 20

game = GameEngine.Game(Enviroment, agents,verbose=0)
logs = game.Play(Max_steps,Repeats_count)

```
5. Voila, you got some logs to analyze. 

Logs is pandas DataFrame with columns: 
* information: 'Action', 'Agent','Iter', 'N_repeat'
* action: 'Best_action_flag', 'Avg_best_action', 'Sum_best_action'
* reward: 'Sum_reward', 'Avg_reward', 'Reward'
* regret: 'Regret', 'Avg_regret', 'Sum_regret'
* pseudo_regret: 'Sum_pseudo_regret', 'Avg_pseudo_regret'

See more use-cases in [notebook folder](https://github.com/iJKos/MABpy/tree/master/notebooks)

Modules description
------------------
* base
* GameEngine
* SimpleMAB
* ActionRewardAgents


Documentation
-------------
For extensive documentation see the docs folder or [read it on readthedocs](http://mabpy.readthedocs.io/en/latest/)

License
-------
The MabPy is available as open source under the terms of the [MIT License.
](https://opensource.org/licenses/MIT)

Authors
-------

* **iJKos** - JK.Ermakov (at) gmail 

Contribute
----------
This project is currently open to contributions. In fact, we encourage anyone and everyone to contribute!

Note
----


