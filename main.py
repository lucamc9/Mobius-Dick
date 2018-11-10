from utils import *
from WOA import WOA # comment and uncomment below to test your version
#from WOA_hoog import WOA
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import numpy as np

# inits
n_agents = 30
max_iter = 500
n_runs = 30
func_names = ['F3', 'F10', 'F22']

# lower_b, upper_b, dim, bench_f = get_function_details_2D(func_name)
# best_scores = np.zeros(iters)
# for i in range (iters):
#     woa = WOA(n_agents, max_iter, lower_b, upper_b, dim, bench_f)
#     best_score, best_pos, conv_curve = woa.forward()
#     print(best_score)
#     print(best_pos)
#     print("\n")
#     best_scores[i] = best_score
#     print(i)
    # for j in range (3):
    #    print(woa.q.count(j+1))
    #print('Best solution found by WOA: {}'.format(best_score))
# ave = np.average(best_scores)
# std = np.std(best_scores)
# print('Average = {}, std = {}'.format(ave,std))

for func_name in func_names:
       scores = []
       lower_b, upper_b, dim, bench_f = get_function_details(func_name)
       for i in range(n_runs):
              woa = WOA(n_agents, max_iter, lower_b, upper_b, dim, bench_f)
              best_score, best_pos, conv_curve = woa.forward()
              print('Best solution found by WOA run {}: {}'.format(i, best_score))
              scores.append(best_score)

       print('Function: {} -> ave = {}, std = {}'.format(func_name, np.mean(scores), np.std(scores)))

# plot
fig, ax = plt.subplots()
ax.plot(conv_curve)
ax.ticklabel_format(axis='y', style='sci')
ax.set(xlabel='iter', ylabel='leader_score',
       title='Objective Space')
plt.show()
