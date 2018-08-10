#!/usr/bin/python3

from time import time, sleep

def mydecor(f):
    def wrapper(*a, **kw):
        t1 = time()
        rv = f(*a, **kw)
        sleep (.5)
        t2 = time()
        print('time taken: ', t2-t1)

    return wrapper

@mydecor
def hello_handler(arg):
    print('Hello,', arg)

class Commands():
    def hello(self, arg):
        hello_handler(arg)
    def yo(self, arg):
        print('Yo! whatsapp,', arg)
    def exit(self):
        print('Yalla, bye!')

def main():
    cmd = ''
    commands = Commands()
    while 1:
        if cmd == 'exit':
            break
        try:
            cmd, arg = input('> ').split()
        except ValueError:
            print('Try again')
            continue
        if hasattr(commands, cmd):
            getattr(commands, cmd)(arg)
        else:  
            print(cmd, 'does not exist')


if __name__ == '__main__':
    main()

