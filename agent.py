# coding: UTF-8

import numpy
import cv2
import random
import copy

class Agent:

    def __init__(self, maze_shape):
        # agentの状態と行動を格納する変数を定義
        self.state = numpy.array([0, 0])
        self.actions = self.__create_actions(maze_shape)

        # 行動と状態の座標変化をマッピング
        self.moves = {0: numpy.array([0, -1]),
                      1: numpy.array([1, 0]),
                      2: numpy.array([0, 1]),
                      3: numpy.array([-1, 0])}
        
        # 学習時各行動をスクリーン上で表示するために各行動の名前を定義
        self.acts = {0: "left", 1: "down", 2: "right", 3: "up"}

        # q-tableを要素が全部0である配列で初期化
        # q-tableの次元は：動作空間の次元数 × 状態空間の次元数
        

    # agentを動作
    def act(self, maze, epsilon, alpha, gamma):
        # epsilon-greedy法により次でとる動作を選択
        act_index, next_move = self.__select_action_via_epsilon_greedy(epsilon)
        
        # 環境から次の動作の報酬を獲得
        reward = maze[tuple(self.state + next_move)]

        # q-tableを更新
        self.update_q(act_index, next_move, reward, alpha, gamma)

        # 動作を実行し，状態を更新
        self.state += next_move

    # q-tableを更新
    def __update_q(self, act_index, next_move, reward, alpha, gamma):
        # 状態のindexを取得
        

        # 過去のq値を一時的に変数q_に保存


        # 行動価値関数の更新式によってq-tableを更新
        # maxQはself.__get_max_q(next_move)を利用

        

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

    # epsilon-greedy法で次の動作とそのindexを獲得
    def __select_action_via_epsilon_greedy(self, epsilon):
        # 現在の状態において，取りうる行動の配列を取得し，変数actionに保存
        

        # ifの場合はQ値最大の動作を選択し，elseの場合でランダムで動作を選択
        if
            mode = '!!!greedy!!!'
            act_index = self.__select_greedy_action(action)
        else:
            mode = '!!!random!!!'
            act_index = self.__select_random_action(action)

        print('%s  state: (%d, %d), action: %s' % (mode, y, x, self.acts[act_index]))

        # 動作のindexから動作を確認
        next_move = self.moves.get(act_index)

        return act_index, next_move

    # 1-epsilonの確率で価値が最大の動作を選択
    def __select_greedy_action(self, action):
        
        return act_index

    # epsilonの確率でランダムで動作を選択(探索)
    def __select_random_action(self, action):
        
        return act_index

    # 次の状態において最大の行動価値を出力
    def __get_max_q(self, move):
        
        return max_q
