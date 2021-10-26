from .kitchen_envs import *
from gym.envs.registration import register

# Whole dataset with undirected demonstrations. No demonstration completely
# solves the task, but each demonstration partially solves different
# components of the task.
register(
    id='kitchen-2-mixed-v0',
    entry_point='d4rl.kitchen_2:KitchenMicrowaveKettleBottomBurnerLightV0',
    max_episode_steps=100000, #280,
    kwargs={
        'ref_min_score': 0.0,
        'ref_max_score': 4.0,
        'dataset_url': 'http://rail.eecs.berkeley.edu/datasets/offline_rl/kitchen/kitchen_microwave_kettle_bottomburner_light-v0.hdf5',
    }
)

### SINGLE TASK -- FIXED envs

register(
    id='kitchen-2-BB-v0',
    entry_point='d4rl.kitchen_2:KitchenBottomBurnerV0',
    max_episode_steps=50,
    kwargs={
        'ref_min_score': 0.0,
        'ref_max_score': 4.0,
        'dataset_url': 'http://rail.eecs.berkeley.edu/datasets/offline_rl/kitchen/kitchen_microwave_kettle_bottomburner_light-v0.hdf5',
    }
)
register(
    id='kitchen-2-TB-v0',
    entry_point='d4rl.kitchen_2:KitchenTopBurnerV0',
    max_episode_steps=50,
    kwargs={
        'ref_min_score': 0.0,
        'ref_max_score': 4.0,
        'dataset_url': 'http://rail.eecs.berkeley.edu/datasets/offline_rl/kitchen/kitchen_microwave_kettle_bottomburner_light-v0.hdf5',
    }
)
register(
    id='kitchen-2-LS-v0',
    entry_point='d4rl.kitchen_2:KitchenLightSwitchV0',
    max_episode_steps=50,
    kwargs={
        'ref_min_score': 0.0,
        'ref_max_score': 4.0,
        'dataset_url': 'http://rail.eecs.berkeley.edu/datasets/offline_rl/kitchen/kitchen_microwave_kettle_bottomburner_light-v0.hdf5',
    }
)
register(
    id='kitchen-2-SC-v0',
    entry_point='d4rl.kitchen_2:KitchenSlideCabinetV0',
    max_episode_steps=50,
    kwargs={
        'ref_min_score': 0.0,
        'ref_max_score': 4.0,
        'dataset_url': 'http://rail.eecs.berkeley.edu/datasets/offline_rl/kitchen/kitchen_microwave_kettle_bottomburner_light-v0.hdf5',
    }
)
register(
    id='kitchen-2-HC-v0',
    entry_point='d4rl.kitchen_2:KitchenHingeCabinetV0',
    max_episode_steps=50,
    kwargs={
        'ref_min_score': 0.0,
        'ref_max_score': 4.0,
        'dataset_url': 'http://rail.eecs.berkeley.edu/datasets/offline_rl/kitchen/kitchen_microwave_kettle_bottomburner_light-v0.hdf5',
    }
)
register(
    id='kitchen-2-MW-v0',
    entry_point='d4rl.kitchen_2:KitchenMicrowaveV0',
    max_episode_steps=50,
    kwargs={
        'ref_min_score': 0.0,
        'ref_max_score': 4.0,
        'dataset_url': 'http://rail.eecs.berkeley.edu/datasets/offline_rl/kitchen/kitchen_microwave_kettle_bottomburner_light-v0.hdf5',
    }
)
register(
    id='kitchen-2-KET-v0',
    entry_point='d4rl.kitchen_2:KitchenKettleV0',
    max_episode_steps=50,
    kwargs={
        'ref_min_score': 0.0,
        'ref_max_score': 4.0,
        'dataset_url': 'http://rail.eecs.berkeley.edu/datasets/offline_rl/kitchen/kitchen_microwave_kettle_bottomburner_light-v0.hdf5',
    }
)


### SINGLE TASK -- RANDOMIZED START envs

register(
    id='kitchen-2-BB-rand-v0',
    entry_point='d4rl.kitchen_2:KitchenBottomBurnerRandV0',
    max_episode_steps=70,
    kwargs={
        'ref_min_score': 0.0,
        'ref_max_score': 4.0,
        'dataset_url': 'http://rail.eecs.berkeley.edu/datasets/offline_rl/kitchen/kitchen_microwave_kettle_bottomburner_light-v0.hdf5',
    }
)
register(
    id='kitchen-2-TB-rand-v0',
    entry_point='d4rl.kitchen_2:KitchenTopBurnerRandV0',
    max_episode_steps=70,
    kwargs={
        'ref_min_score': 0.0,
        'ref_max_score': 4.0,
        'dataset_url': 'http://rail.eecs.berkeley.edu/datasets/offline_rl/kitchen/kitchen_microwave_kettle_bottomburner_light-v0.hdf5',
    }
)
register(
    id='kitchen-2-LS-rand-v0',
    entry_point='d4rl.kitchen_2:KitchenLightSwitchRandV0',
    max_episode_steps=70,
    kwargs={
        'ref_min_score': 0.0,
        'ref_max_score': 4.0,
        'dataset_url': 'http://rail.eecs.berkeley.edu/datasets/offline_rl/kitchen/kitchen_microwave_kettle_bottomburner_light-v0.hdf5',
    }
)
register(
    id='kitchen-2-SC-rand-v0',
    entry_point='d4rl.kitchen_2:KitchenSlideCabinetRandV0',
    max_episode_steps=70,
    kwargs={
        'ref_min_score': 0.0,
        'ref_max_score': 4.0,
        'dataset_url': 'http://rail.eecs.berkeley.edu/datasets/offline_rl/kitchen/kitchen_microwave_kettle_bottomburner_light-v0.hdf5',
    }
)
register(
    id='kitchen-2-HC-rand-v0',
    entry_point='d4rl.kitchen_2:KitchenHingeCabinetRandV0',
    max_episode_steps=70,
    kwargs={
        'ref_min_score': 0.0,
        'ref_max_score': 4.0,
        'dataset_url': 'http://rail.eecs.berkeley.edu/datasets/offline_rl/kitchen/kitchen_microwave_kettle_bottomburner_light-v0.hdf5',
    }
)
register(
    id='kitchen-2-MW-rand-v0',
    entry_point='d4rl.kitchen_2:KitchenMicrowaveRandV0',
    max_episode_steps=70,
    kwargs={
        'ref_min_score': 0.0,
        'ref_max_score': 4.0,
        'dataset_url': 'http://rail.eecs.berkeley.edu/datasets/offline_rl/kitchen/kitchen_microwave_kettle_bottomburner_light-v0.hdf5',
    }
)
register(
    id='kitchen-2-KET-rand-v0',
    entry_point='d4rl.kitchen_2:KitchenKettleRandV0',
    max_episode_steps=70,
    kwargs={
        'ref_min_score': 0.0,
        'ref_max_score': 4.0,
        'dataset_url': 'http://rail.eecs.berkeley.edu/datasets/offline_rl/kitchen/kitchen_microwave_kettle_bottomburner_light-v0.hdf5',
    }
)