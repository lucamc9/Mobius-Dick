import numpy as np
from utils import *

test = np.array([1, 2, 5, 7, 2, 2, 2, 2, 2, 2, 5, 6, 7, 8, 4, 5, 6, 0.2, 0.5, 9, 7, 8, 4, 4, 5, 4, 2, 0.3, 0.3, 0.6])
func_names = ['F3', 'F10']

for func_name in func_names:
    lower_b, upper_b, dim, bench_f = get_function_details(func_name)
    fitness = bench_f.get_fitness(test)
    print('Func {}, Fitness = {}'.format(func_name, fitness))
