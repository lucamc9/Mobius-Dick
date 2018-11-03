from utils import get_function_details
from WOA import WOA # comment and uncomment below to test your version
#from WOA_hoog import WOA
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick

n_agents = 30
func_name = 'F3'
max_iter = 500
lower_b, upper_b, dim, bench_f = get_function_details(func_name)

# for i in range (20):

woa = WOA(n_agents, max_iter, lower_b, upper_b, dim, bench_f)
best_score, best_pos, conv_curve = woa.forward()
print('Best solution found by WOA: {}'.format(best_score))

fig, ax = plt.subplots()
ax.plot(conv_curve)
ax.ticklabel_format(axis='y', style='sci')
ax.set(xlabel='iter', ylabel='leader_score',
       title='Objective Space')
plt.show()
