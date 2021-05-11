# Miscrosoft's OpenAI Gym Python Package

Gym is a toolkit for developing and comparing reinforcement learning algorithms. Gym provides the environment; you provide the algorithm.


For documentation and example uses please visit this [link](https://gym.openai.com/).


## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install **gym**.


In terminal or command prompt:


```bash
pip install gym
```

or in Jupyter:


```python
!pip install gym
```


or if you prefer building from source:


```bash
git clone https://github.com/openai/gym
cd gym
pip install -e .
```


## Usage

```python
import gym
from gym import envs
```

## Demo

Our demo for how this package can be used can be found at the following [link](https://www.youtube.com/watch?v=S5fegcYwdOM).


#### Other Examples:

Below are some links to videos of some environments being simulated:

[SpaceInvaders-v0](https://gym.openai.com/videos/2019-10-21--mqt8Qj1mwo/SpaceInvaders-v0/original.mp4)

[Ant-v2](https://gym.openai.com/videos/2019-10-21--mqt8Qj1mwo/Ant-v2/original.mp4)

## Functionality

This package primarily functions as an easy to use and manage way of setting up differing environments to train active agents with a reward system.
By handling the 2D and 3D visualization, it allows users to focus more on developing the right reinforcement learning algorithm.

#### Basics
Reinforcement learning conists of two basic concepts:

* *Environment* - A task or simulation that is constructed that needs interaction to solve.

* *Agent* - An AI algorithm that is developed to interact with the environment.

![image info](https://miro.medium.com/max/674/0*6yvI8Ul2ETKO-Ils.png)

The illustration above shows a simplified diagram of how the agent and environment interact.  The environment provides the agent its state and reward system.  
The agent will then send an action to the environment.  The environment will respond with a change in the state and reward the agent based on the reward system criteria.  
The agent will continue to respond and provide actions to maximize its rewards as it begins optimizing its machine learning process.