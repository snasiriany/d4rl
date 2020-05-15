import logging
from d4rl.pointmaze import waypoint_controller
from d4rl.pointmaze import maze_model
import numpy as np
import pickle
import gzip
import h5py
import argparse
import os
import tqdm


def reset_data():
    return {'states': [],
            'actions': [],
            'terminals': [],
            'infos/goal': [],
            'infos/qpos': [],
            'infos/qvel': [],
            }

def append_data(data, s, a, tgt, done, env_data):
    data['states'].append(s)
    data['actions'].append(a)
    data['terminals'].append(done)
    data['infos/goal'].append(tgt)
    data['infos/qpos'].append(env_data.qpos.ravel().copy())
    data['infos/qvel'].append(env_data.qvel.ravel().copy())

def npify(data):
    for k in data:
        if k == 'terminals':
            dtype = np.bool_
        else:
            dtype = np.float32

        data[k] = np.array(data[k], dtype=dtype)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--render', action='store_true', help='Render trajectories')
    parser.add_argument('--noisy', action='store_true', help='Noisy actions')
    parser.add_argument('--maze', type=str, default='hardexp', help='Maze type. small or default')
    parser.add_argument('--data_dir', type=str, default='.', help='Base directory for dataset')
    parser.add_argument('--num_samples', type=int, default=int(2e4), help='Num samples to collect')
    parser.add_argument('--min_traj_len', type=int, default=int(20), help='Min number of samples per trajectory')
    parser.add_argument('--batch_idx', type=int, default=int(-1), help='(Optional) Index of generated data batch')
    args = parser.parse_args()

    if args.maze == 'umaze':
        maze = maze_model.U_MAZE
        max_episode_steps = 150
    elif args.maze == 'open':
        maze = maze_model.OPEN
        max_episode_steps = 150
    elif args.maze == 'medium':
        maze = maze_model.MEDIUM_MAZE
        max_episode_steps = 250
    elif args.maze == 'hardexp':
        maze = maze_model.HARD_EXP_MAZE
        max_episode_steps = 300
    else:
        maze = maze_model.LARGE_MAZE
        max_episode_steps = 600
    controller = waypoint_controller.WaypointController(maze)
    env = maze_model.MazeEnv(maze)

    s = env.reset()
    env.set_target()

    data = reset_data()
    ts, cnt = 0, 0
    for tt in tqdm.tqdm(range(args.num_samples)):
        position = s[0:2]
        velocity = s[2:4]
        act, done = controller.get_action(position, velocity, env._target)
        if args.noisy:
            act = act + np.random.randn(*act.shape)*0.5

        act = np.clip(act, -1.0, 1.0)
        if ts >= max_episode_steps:
            done = True
        append_data(data, s, act, env._target, done, env.sim.data)

        ns, _, _, _ = env.step(act)

        ts += 1
        if done:
            if len(data['actions']) > args.min_traj_len:
                save_data(args, data, cnt)
                cnt += 1
            data = reset_data()
            s = env.reset()
            env.set_target()
            ts = 0
        else:
            s = ns

        if args.render:
            env.render()


def save_data(args, data, idx):
    dir_name = 'maze2d-%s-noisy' % args.maze if args.noisy else 'maze2d-%s' % args.maze
    if args.batch_idx >= 0:
        dir_name = os.path.join(dir_name, "batch_{}".format(args.batch_idx))
    os.makedirs(os.path.join(args.data_dir, dir_name), exist_ok=True)
    file_name = os.path.join(args.data_dir, dir_name, "rollout_{}.h5".format(idx))

    # save rollout to file
    f = h5py.File(file_name, "w")
    f.create_dataset("traj_per_file", data=1)

    # store trajectory info in traj0 group
    npify(data)
    traj_data = f.create_group("traj0")
    traj_data.create_dataset("states", data=data['states'])
    traj_data.create_dataset("images", data=np.zeros((data['states'].shape[0], 2, 2, 3), dtype=np.uint8))
    traj_data.create_dataset("actions", data=data['actions'])

    terminals = data['terminals']
    if np.sum(terminals) == 0:
        terminals[-1] = True

    # build pad-mask that indicates how long sequence is
    is_terminal_idxs = np.nonzero(terminals)[0]
    pad_mask = np.zeros((len(terminals),))
    pad_mask[:is_terminal_idxs[0]] = 1.
    traj_data.create_dataset("pad_mask", data=pad_mask)

    f.close()


if __name__ == "__main__":
    main()