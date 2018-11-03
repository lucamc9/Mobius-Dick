import numpy as np
from utils import *

test = np.array([[1, 1, 1, 1], [2, 3, 4, 5], [5, 5, 5, 5]])
func_names = ['F1', 'F3', 'F10', 'F22']

for func_name in func_names:
    lower_b, upper_b, dim, bench_f = get_function_details(func_name)
    fitness = bench_f.get_fitness(test)
    print('Func {}, Fitness = {}'.format(func_name, fitness))
