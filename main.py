import gym
import json
import datetime as dt

from stable_baselines.common.policies import MlpPolicy
from stable_baselines.common.vec_env import DummyVecEnv
from stable_baselines import PPO2

from env.SmartGridEnv import SmartGridEnv

import pandas as pd

df = pd.read_excel('./data/RL_data.xlsx')
df = df.sort_values(['Date', 'Hour'])

# The algorithms require a vectorized environment to run
env = DummyVecEnv([lambda: SmartGridEnv(df)])

model = PPO2(MlpPolicy, env, verbose=1)
model.learn(total_timesteps=20000)

obs = env.reset()
for i in range(len(df['Date'].values)):
    action, _states = model.predict(obs)
    obs, rewards, done,  info = env.step(action)
    env.render()
