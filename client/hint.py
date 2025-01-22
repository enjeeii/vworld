# -*- coding: utf-8 -*-
import curses

_hint_talk = None
_hint_over = None
_hint_tools = None

def init(h, l, y, x):
    global _hint_talk
    _hint_talk = curses.newwin(int(h*0.2), int(l * 0.8), int(h * 0.7 + y), int(l * 0.1 + x))

    global _hint_over
    _hint_over = curses.newwin(int(h*0.4), int(l * 0.6), int(h * 0.3 + y), int(l * 0.2 + x))

    global _hint_tools
    _hint_tools = curses.newwin(h, int(l * 0.2), y, int(l + x + 2))

def clear():
    _hint_talk.clear()
    _hint_over.clear()
    _hint_tools.clear()

def refresh():
    _hint_talk.box()
    _hint_talk.refresh()
    _hint_over.box()
    _hint_over.refresh()
    _hint_tools.refresh()
