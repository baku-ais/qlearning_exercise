# coding: UTF-8

from agent import *
from mazeimage import *

def main():

    # パラメータの初期化
    epsilon = 0.1           # 探索行動を選択する確率
    alpha = 0.2             # 学習率
    gamma = 0.9             # 割引率

    # csvファイルから環境を読み込み
    maze = numpy.loadtxt('./maze_1.csv', delimiter = ',')

    # agentの初期化
    agent = Agent(maze.shape)

    # 迷路の可視化のための準備
    maze_image = MazeImage(maze, 600, 600)

    # 学習開始，300回の学習を行う
    trial = 0
    while True:
        # agentが迷路を解く動画を表示，ESCキーで学習を中止
        if maze_image.show(agent, trial) == 27:
            print('!!!escape!!!')
            break

        # agentが動作し，環境から報酬を獲得
        agent.act(maze, epsilon, alpha, gamma)
        maze_image.save_movie()

        # agentが終点に到達したらリセット
        if agent.goal(maze.shape):
            print('\033[32m' + '!!!goal!!!' + '\033[0m')
            trial += 1
            print('next trial: %d' % (trial+1))
            agent.reset()

        if trial == 300:
            break

    # 学習の過程を動画として保存
    maze_image.save_movie()

    # 学習の結果を画像として表示
    cv2.imwrite('shortest.png', maze_image.shortest_path(agent.q))
    cv2.destroyAllWindows()

if __name__ == "__main__":
    try:
        main()
    except:
        pass
