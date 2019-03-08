import gym
from gym import spaces
import numpy as np


class DummyEnv(gym.Env):
    """
    DummyEnv - The simplest possible implementation of an OpenAI gym environment
    """
    def __init__(self):
        self.episode_over = False
        self.action_space = gym.spaces.Discrete(2)
        self.state = np.zeros(3)
        self.observation_space = self.state
        self.reward_range = (-1, 1000)
        self.start_state = 0
        self.goal_state = 10

    def step(self, action):
        """

        Parameters
        ----------
        action :

        Returns
        -------
        ob, reward, episode_over, info : tuple
            ob (object) :
                an environment-specific object representing your observation of
                the environment.
            reward (float) :
                amount of reward achieved by the previous action. The scale
                varies between environments, but the goal is always to increase
                your total reward.
            episode_over (bool) :
                whether it's time to reset the environment again. Most (but not
                all) tasks are divided up into well-defined episodes, and done
                being True indicates the episode has terminated. (For example,
                perhaps the pole tipped too far, or you lost your last life.)
            info (dict) :
                 diagnostic information useful for debugging. It can sometimes
                 be useful for learning (for example, it might contain the raw
                 probabilities behind the environment's last state change).
                 However, official evaluations of your agent are not allowed to
                 use this for learning.
        """
        # take action
        if action == 0:
            # reduce state, limited by zero
            self.state[0] = max(self.start_state, self.state[0] - 1)
        elif action == 1:
            # increase state, limited by goal_state
            self.state[0] = min(self.goal_state, self.state[0] + 1)
        else:
            raise("action not defined")

        # end episode after reaching goal state
        episode_over = self.state[0] == self.goal_state

        # get reward at
        reward = self.reward_range[1] * int(self.state[0] == self.goal_state)
        # add some random negative reward noise to make it optimal to get to goal state fast
        reward += self.reward_range[0] * np.random.random()

        # observation is state plus random noise
        # Note, only first entry in the state vector is actually informative
        ob = self.state + 2 * np.random.random() - 1.0
        return ob, reward, episode_over, {}

    def reset(self):
        self.state = np.zeros(3)
        self.state[0] = self.start_state
        return self.state

    def render(self, mode='human', close=False):
        pass

    def close(self):
        pass

    def seed(self, seed=None):
        pass
