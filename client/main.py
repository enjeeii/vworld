# -*- coding: utf-8 -*-
import curses
import time
#
# import game
# import hint

GAME_HEIGHT = 20
GAME_LENGTH = 40
FRAME = 25


class IPanel():
    def enter(self): pass
    def exit(self): pass
    def draw(self): pass

class MainPanel(IPanel):
    def __init__(self, w, left):
        self.w = w

        self.w.addstr(1, left, '目标: 得分！')
        self.w.addstr(2, left, 'Q: 退出')
        self.w.addstr(3, left, 'R: 重新开始')
        self.w.addstr(4, left, 'P: 暂停')

    def enter(self):
        self.w.refresh()

    def exit(self):
        self.w.clear()

class Role():
    def __init__(self, y, x, max_y, max_x):
        self.char = 'a'
        self.max_y = max_y
        self.max_x = max_x

        self.y = y
        self.x = x

    def draw(self):
        return self.y, self.x, self.char

    def up(self):
        self.y = self.y - 1 if self.y > 1 else self.y

    def down(self):
        self.y = self.y + 1 if self.y < self.max_y - 2 else self.y

    def left(self):
        self.x = self.x - 1 if self.x > 1 else self.x

    def right(self):
        self.x = self.x + 1 if self.x < self.max_x - 2 else self.x

class GamePanel(IPanel):
    def __init__(self, w):
        self.w = w
        self.role = Role(int(GAME_HEIGHT/2), int(GAME_LENGTH/2), GAME_HEIGHT, GAME_LENGTH)

    def enter(self):
        pass

    def exit(self):
        pass

    def draw(self):
        self.w.clear()

        self.w.addstr(*self.role.draw())
        self.w.box()

        self.w.refresh()

class Scene():
    def __init__(self):
        self.panels = []

    def push(self, panel):
        panel.enter()
        self.panels.append(panel)

    def pop(self):
        if len(self.panels):
            p = self.panels.pop()
            p.exit()

    def draw(self):
        for p in self.panels:
            p.draw()


def main(ss):
    # 隐藏光标
    curses.curs_set(0)

    game_top = int((curses.LINES - GAME_HEIGHT) * 0.8)
    game_left = int((curses.COLS - GAME_LENGTH) * 0.4)

    main_panel = MainPanel(ss, game_left)
    game_panel = GamePanel(curses.newwin(GAME_HEIGHT, GAME_LENGTH, game_top, game_left))

    scene = Scene()
    scene.push(main_panel)
    scene.push(game_panel)

    while True:
        scene.draw()
        ch = ss.getch()
        if ch == ord('q') or ch == ord('Q'):
            break
        if ch == curses.KEY_LEFT:
            game_panel.role.left()
        if ch == curses.KEY_RIGHT:
            game_panel.role.right()
        if ch == curses.KEY_UP:
            game_panel.role.up()
        if ch == curses.KEY_DOWN:
            game_panel.role.down()

if __name__ == '__main__':
    curses.wrapper(main)
