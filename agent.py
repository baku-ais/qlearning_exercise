# coding: UTF-8

import numpy
import cv2
import random
import copy

class Agent:

    def __init__(self, maze_shape):
        self.state = numpy.array([0, 0])
        self.actions = self.__create_actions(maze_shape)
        self.moves = {0: numpy.array([0, -1]), 1: numpy.array([1, 0]), 2: numpy.array([0, 1]), 3: numpy.array([-1, 0])}
        self.acts = {0: "left", 1: "down", 2: "right", 3: "up"}
        self.q = numpy.zeros((4, ) + maze_shape)

    # agentを動作
    def act(self, maze, epsilon, alpha, gamma):
        act_index, next_move = self.__select_action_via_epsilon_greedy(epsilon)
        reward = maze[tuple(self.state + next_move)]
        self.update_q(act_index, next_move, reward, alpha, gamma)
        self.state += next_move

    # q-tableを更新
    def update_q(self, act_index, next_move, reward, alpha, gamma):
        y, x = self.state
        _q = self.q[act_index, y, x]
        self.q[act_index, y, x] = _q + alpha * (reward + gamma * self.__get_max_q(next_move) - _q)

    # agentが終点に到達したかを判断
    def goal(self, maze_shape):
        return numpy.array_equal(self.state, numpy.array(maze_shape) - 1)

    # 環境をリセットし，agentを起点に戻す
    def reset(self):
        self.state = numpy.array([0, 0])

    # 上下左右に移動する動作を生成
    def __create_actions(self, maze_shape):
        actions = []
        maze_h, maze_w = maze_shape
        for j in range(maze_h):
            actions.append([])
            for i in range(maze_w):
                action = [0, 1, 2, 3]
                self.__remove_actions(action, maze_h, maze_w, j, i)
                actions[j].append(action)

        return numpy.array(actions)

    # 迷路の範囲を出る動作を取り除く
    def __remove_actions(self, action, maze_h, maze_w, j, i):
        if i == 0:
            action.remove(0)
        if i == maze_w - 1:
            action.remove(2)
        if j == 0:
            action.remove(3)
        if j == maze_h - 1:
            action.remove(1)

    # epsilon-greedy法により次でとる動作を選択
    def __select_action_via_epsilon_greedy(self, epsilon):
        y, x = self.state
        action = copy.deepcopy(self.actions[y, x])
        if numpy.random.rand() > epsilon:
            mode = '!!!greedy!!!'
            act_index = self.__select_greedy_action(action)
        else:
            mode = '!!!random!!!'
            act_index = self.__select_random_action(action)

        print('%s  state: (%d, %d), action: %s' % (mode, y, x, self.acts[act_index]))

        next_move = self.moves.get(act_index)

        return act_index, next_move

    # 1-epsilonの確率で価値が最大の動作を選択
    def __select_greedy_action(self, action):
        y, x = self.state
        _max = self.q[action, y, x].max()
        _indexes = list(numpy.argwhere(self.q[action, y, x] == _max))
        random.shuffle(_indexes)
        return action[int(_indexes[0])]

    # epsilonの確率でランダムで動作を選択(探索)
    def __select_random_action(self, action):
        random.shuffle(action)
        return action[0]

    # 最大の行動価値を出力
    def __get_max_q(self, move):
        y, x = self.state + move
        move = self.actions[y, x]
        return self.q[move, y, x].max()
