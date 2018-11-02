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
        lower_b = -32
        upper_b = 32
        dim = 30
        bench_f = Bench_Function('F10')
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
        dim = 30
        bench_f = Bench_Function('F3')

    elif func_name == 'F4':
        lower_b = -100
        upper_b = 100
        dim = 30
        bench_f = Bench_Function('F4')

    elif func_name == 'F6':
        lower_b = -100
        upper_b = 100
        dim = 30
        bench_f = Bench_Function('F6')

    elif func_name == 'F10':
        lower_b = -32
        upper_b = 32
        dim = 30
        bench_f = Bench_Function('F10')

    return lower_b, upper_b, dim, bench_f

class Bench_Function:

    def __init__(self, func_name):
        self.func_name = func_name

    def get_fitness(self, x):
        if self.func_name == 'F1':
            return np.sum(x**2)
        if self.func_name == 'F3':
            dim = x.shape[1]
            o = 0
            for i in range(dim):
                o += np.sum(x[:,1:i])**2
            return o
        if self.func_name == 'F4':
            return np.sum(x**2)
        if self.func_name == 'F6':
            return np.sum(x**2)
        if self.func_name == 'F10':
            return np.sum(x**2)
