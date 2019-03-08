import gym
import gym_dummy

num_episodes = 20
max_steps = 100

env = gym.make('dummy-v0')
for i_episode in range(num_episodes):
    o = env.reset()
    total_reward = 0
    for t in range(max_steps):
        action = env.action_space.sample()
        observation, reward, done, info = env.step(action)
        total_reward += reward
        if done or t + 1 == max_steps:
            print("Episode finished after {:3} timesteps with total reward {:3.1f}".format(t+1, total_reward))
            break
