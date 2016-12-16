from curses import wrapper
import curses
import os
import sys,time,random


def main(stdscr):
    # Clear screen
    stdscr.clear()
    screen = curses.initscr()
    screen.border(0)
    ymax, xmax = screen.getmaxyx()
    ylow, xlow = screen.getbegyx()
    # legt ein neuens Feld an (height, width, begin_y, begin_x)
    box1 = curses.newwin(int(ymax *0.3) ,xmax - 4,int(ymax - ymax * 0.31  ),xlow + 2)
    box2 = curses.newwin(int(ymax *0.6) ,xmax - 4,int(ylow + 2),xlow + 2)  




    box1.box()
    box2.box()
    screen.refresh()
    # Läd die Box beu
    box1.refresh()
    box2.refresh()

    stdscr.refresh()
    stdscr.getkey()

wrapper(main)
