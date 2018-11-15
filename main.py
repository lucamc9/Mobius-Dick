"""
NAT - Assignment2
Luca G.McArthur s14422321
Gabriel Hoogervorst s1505156

This script runs the Whale Optimization Algorithm for a given set of parameters.

"""

from utils import *
from WOA import WOA
from WOA_conceptual import WOA_conceptual
from WOA_mathematical import WOA_mathematical
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import numpy as np

# inits
n_agents = 30
max_iter = 500
n_runs = 30
func_names = ['F3', 'F10', 'F22']

# compute the scores for each function
for func_name in func_names:
       scores = []
       lower_b, upper_b, dim, bench_f = get_function_details(func_name)

       for i in range(n_runs):
          # to run an alternative implementation simply call WOA_conceptual/WOA_mathematical
          woa = WOA(n_agents, max_iter, lower_b, upper_b, dim, bench_f)
          best_score, best_pos, conv_curve = woa.forward()
          print('Best solution found by WOA at run {}: {}'.format(i, best_score))
          scores.append(best_score)

       print('Function: {} -> ave = {}, std = {}'.format(func_name, np.mean(scores), np.std(scores)))

# plot
fig, ax = plt.subplots()
ax.plot(conv_curve)
ax.ticklabel_format(axis='y', style='sci')
ax.set(xlabel='iter', ylabel='leader_score',
       title='Objective Space')
plt.show()
