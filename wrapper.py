from curses import wrapper
import curses

def main(stdscr):
    # Clear screen
    stdscr.clear()
    screen = curses.initscr()
    screen.border(0)
    # Mach eine neue box (height, width, begin_y, begin_x)
    box1 = curses.newwin(19,175 ,40,2)
    box1.box()
    box1.addstr(1,1,"Hello World of Curses!")

    screen.refresh()
    box1.refresh()

    #screen.getch()


    stdscr.refresh()
    stdscr.getkey()

wrapper(main)
