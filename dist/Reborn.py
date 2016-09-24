# coding=utf-8
import threading

import configparser
import lib_StoryScript


class Game():
    """
    故事脚本：.ss
    已编译故事脚本：.css
    """

    def __init__(self):
        self.isRunning = True
        self.data = {}
        self.data['var'] = {}
        self.data['story'] = {}
        # TODO(miswanting):读取设置
        self.config = configparser.ConfigParser()
        with open('Config.cfg', 'r') as configfile:
            self.config.read(configfile)
        # TODO(miswanting):读取故事
        # TODO(miswanting):读取存档
        # TODO(miswanting):显示主界面
        print('1.新的篇章')
        print('2.旧的回忆')
        print('3.记忆碎片')
        print('4.系统设置')
        print('5.离开游戏')
        # TODO(miswanting):读取用户输入
        self.startInputStar()
        # TODO(miswanting):进入游戏逻辑

    def startInputStar(self):
        def inputStar():
            while self.isRunning:
                cmd = input()
                print(cmd)
                if cmd == 'exit':
                    self.isRunning = False
                    self.display.isRunning = False
        star = threading.Thread(name='inputStar', target=inputStar)
        star.start()
if __name__ == '__main__':
    A = Game()
