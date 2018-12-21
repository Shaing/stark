import sys
from pynput.mouse import Button, Controller

def get_mu_pos(M):
    # Read pointer position
    print('The current pointer position is {0}'.format(
        M.position))

def main(argv):
    mouse = Controller()

    if argv[1] == '-g':
        get_mu_pos(mouse)
    elif len(argv) > 3 and argv[1] == '-s':
        # Set pointer position
        mouse.position = (argv[2], argv[3])
        print('Now we have moved it to {0}'.format(
            mouse.position))

        # Move pointer relative to current position
        # mouse.move(5, -5)

        # # Press and release
        # mouse.press(Button.left)
        # mouse.release(Button.left)

        # # Double click; this is different from pressing and releasing
        # # twice on Mac OSX
        click_times = 1 if len(argv) == 4 else argv[4]
        mouse.click(Button.left, int(click_times))

        # # Scroll two steps down
        # mouse.scroll(0, 2)
    else:
        print('Nothing happened.')

if __name__ == '__main__':
    if len(sys.argv) == 1:
        print('-g, get current position.')
        print('-s [x] [y] [click counts=1], set current position and move to click counts(default is 1).')
        print('i.e.')
        print('\t -g . It will return two numbers about x and y.')
        print('\t -s 1242 143 1. which you set -g to get current position and click counts at third.')
    elif len(sys.argv) > 1:
        main(sys.argv)
