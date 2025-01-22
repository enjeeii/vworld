# -*- coding: utf-8 -*-
import curses

_game = None
_role = [1, 1, '☺']

def init(h, l, y, x):
    global _game
    _game = curses.newwin(h, l, y, x)
    _game.box()

def clear():
    _game.clear()

def refresh():
    _game.addstr(*_role)
    _game.refresh()

def go_left():
    _role[1] -= 1

def go_right():
    _role[1] += 1

def go_up():
    _role[0] -= 1

def go_down():
    _role[0] += 1
