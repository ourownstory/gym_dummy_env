from gym.envs.registration import register

register(
    id='dummy-v0',
    entry_point='gym_dummy.envs:DummyEnv',
)
