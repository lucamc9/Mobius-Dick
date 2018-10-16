import numpy as np

def get_function_details(func_name):
    if func_name == 'F1':
        lower_b = -100
        upper_b = 100
        dim = 30
        bench_f = Bench_Function('F1')
    return lower_b, upper_b, dim, bench_f

class Bench_Function:

    def __init__(self, func_name):
        self.func_name = func_name

    def get_fitness(self, x):
        if self.func_name == 'F1':
            return np.sum(x**2)
