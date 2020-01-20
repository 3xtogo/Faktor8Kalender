import calendar

import numpy as np

from matplotlib.patches import Rectangle

import matplotlib.pyplot as plt

def plot_calendar(days, months, color):

    plt.figure(figsize=(9, 3))

    # non days are grayed

    ax = plt.gca().axes

    ax.add_patch(Rectangle((29, 2), width=.8, height=.8,

                           color='gray', alpha=.3))

    ax.add_patch(Rectangle((30, 2), width=.8, height=.8,

                           color='gray', alpha=.5))

    ax.add_patch(Rectangle((31, 2), width=.8, height=.8,

                           color='gray', alpha=.5))

    ax.add_patch(Rectangle((31, 4), width=.8, height=.8,

                           color='gray', alpha=.5))

    ax.add_patch(Rectangle((31, 6), width=.8, height=.8,

                           color='gray', alpha=.5))

    ax.add_patch(Rectangle((31, 9), width=.8, height=.8,

                           color='gray', alpha=.5))

    ax.add_patch(Rectangle((31, 11), width=.8, height=.8,

                           color='gray', alpha=.5))

    for d, m, c in zip(days, months, color):

        ax.add_patch(Rectangle((d, m),

                               width=.8, height=.8, color=c))

    plt.yticks(np.arange(1, 13)+.5, list(calendar.month_abbr)[1:])

    plt.xticks(np.arange(1,32)+.5, np.arange(1,32))

    plt.xlim(1, 32)

    plt.ylim(1, 13)

    plt.gca().invert_yaxis()

    # remove borders and ticks

    for spine in plt.gca().spines.values():

        spine.set_visible(False)

    plt.tick_params(top=False, bottom=False, left=False, right=False)

    plt.show()

   

we = [1,1,1,1,1,12,12,12,12,12,12,12,12,12,12,11,11,11,11,11,11,11,11,11,11]

da = [15, 12, 9, 6, 3, 30, 27, 24, 21, 18, 15, 12, 9, 6, 3, 29, 26, 23, 19, 16, 13, 10, 7, 4, 1 ]

standardColor = ['C0' for _ in we]

# here we need a fancy algorithm, that marks days green and red depending on a logic but the calender needs to be smarter too

 

 

 

 

 

plot_calendar(da, we, standardColor)