Multi-Armed Bandits python library
==================================  

MABpy was created as easy-to-use and extend library for Multi-Armed
Bandits (MAB) problem. 
 


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

4. start the Game  

```python
Max_steps = 5000
Repeats_count = 20

game = GameEngine.Game(Enviroment, agents,verbose=0)
logs = game.Play(Max_steps,Repeats_count)

```
5. Voila, you got some logs to analyze.


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


Note
----


