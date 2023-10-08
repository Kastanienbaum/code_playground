'''
Just playing around with multiprocessing package to make use of my 16 CPU cores.
'''

from multiprocessing import Process
import multiprocessing
import random
import os

def info(title):
    print(title)
    print('module name:', __name__)
    print('parent process:', os.getppid())
    print('process id:', os.getpid())

def f(name):
    info('function f')
    print('hello', name)


def math_problem():
    number = 1
    while True:
        number += 1
        if number > 999999:
            number = 0

if __name__ == '__main__':

    NUM_OF_PROCESSES = 2

    multiprocessing.set_start_method('spawn')
    info('main line')
    p = Process(target=f, args=('bob',))
    p.start()
    p.join()
    #math_problem()