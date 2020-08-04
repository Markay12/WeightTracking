# InitGraph.py
# Mark Ashinhust, first graph and realization of graphs

import numpy as np
import matplotlib.pyplot as pyplot

# close all previous figures
pyplot.close('all')


# data to plot

august_one_weight = 154.6
august_two_weight = 153.8
august_three_weight = 153.8

dates = ('Aug01', 'Aug02', 'Aug03')
y_pos = np.arange(len(dates))

weight_list = [august_one_weight, august_two_weight, august_three_weight]

# begin to plot

pyplot.barh(y_pos, weight_list, align='center', alpha = 1)
pyplot.yticks(y_pos, dates)

pyplot.xlabel('Tracked Weights')

pyplot.title('Recorded Weights August 2020')

pyplot.show()
