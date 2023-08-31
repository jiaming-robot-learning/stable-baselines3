# This file is here just to define MlpPolicy/CnnPolicy
# that work for PPO
from stable_baselines3.common.policies import ActorCriticCnnPolicy, ActorCriticPolicy, MultiInputActorCriticPolicy, ActorCriticCnnAuxPolicy

MlpPolicy = ActorCriticPolicy
CnnPolicy = ActorCriticCnnPolicy
MultiInputPolicy = MultiInputActorCriticPolicy
CnnAuxPolicy = ActorCriticCnnAuxPolicy