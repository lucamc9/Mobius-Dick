"""
NAT - Assignment2
Luca G.McArthur s14422321
Gabriel Hoogervorst s1505156

This script defines the benchmark functions that will serve as fitness functions
for WOA.

"""

import numpy as np

def get_function_details(func_name):

    if func_name == 'F1':
        lower_b = -100
        upper_b = 100
        dim = 30
        bench_f = Bench_Function('F1')

    elif func_name == 'F3':
        lower_b = -100
        upper_b = 100
        dim = 30
        bench_f = Bench_Function('F3')

    elif func_name == 'F10':
        lower_b = -32
        upper_b = 32
        dim = 30
        bench_f = Bench_Function('F10')

    elif func_name == 'F22':
        lower_b = 0
        upper_b = 10
        dim = 4
        bench_f = Bench_Function('F22')

    return lower_b, upper_b, dim, bench_f

def get_function_details_2D(func_name):

    if func_name == 'F1':
        lower_b = -100
        upper_b = 100
        dim = 2
        bench_f = Bench_Function('F1')

    elif func_name == 'F3':
        lower_b = -100
        upper_b = 100
        dim = 2
        bench_f = Bench_Function('F3')

    elif func_name == 'F10':
        lower_b = -32
        upper_b = 32
        dim = 2
        bench_f = Bench_Function('F10')

    elif func_name == 'F22':
        lower_b = -32
        upper_b = 32
        dim = 2
        bench_f = Bench_Function('F22')

    return lower_b, upper_b, dim, bench_f

class Bench_Function:

    def __init__(self, func_name):
        self.func_name = func_name

    def get_fitness(self, x):
        if self.func_name == 'F1':
            fitness = np.sum(x**2, 0)

        elif self.func_name == 'F3':
            dim = x.shape[0]
            fitness = 0
            for i in range(dim+1):
                fitness += np.sum(np.transpose(x).ravel()[:i])**2

        elif self.func_name == 'F10':
            dim = x.shape[0]
            fitness = -20*np.exp(-0.2*np.sqrt(np.sum(x**2, 0)/dim)) - np.exp(np.sum(np.cos(2*np.pi*x), 0)/dim) + 20 + np.exp(1)

        elif self.func_name == 'F22':
            a_sh = np.array([[4, 4, 4, 4],
                             [1, 1, 1, 1],
                             [8, 8, 8, 8],
                             [6, 6, 6, 6],
                             [3, 7, 3, 7],
                             [2, 9, 2, 9],
                             [5, 5, 3, 3],
                             [8, 1, 8, 1],
                             [6, 2, 6, 2],
                             [7, 3.6, 7, 3.6]])
            c_sh = np.array([.1, .2, .2, .4, .4, .6, .3, .7, .5, .5])
            fitness = 0
            for i in range(7):
                fitness -= (np.dot((x-a_sh[i,:]), np.transpose((x-a_sh[i,:]))) + c_sh[i])**(-1)


        return fitness
