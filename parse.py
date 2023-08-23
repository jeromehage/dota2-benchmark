import numpy as np
import os
import pandas as pd

from wifps import *

tests = [p for p in os.listdir() if os.path.isdir(p)]

results = pd.DataFrame()
k = 0
plot = True

for i, test in enumerate(tests):

    fig_path = os.path.join(test, 'fig')
    if not os.path.exists(fig_path):
        os.mkdir(fig_path)

    samples = [p for p in os.listdir(test)
               if os.path.isfile(os.path.join(test, p))
               and os.path.splitext(p)[-1] == '.csv']
    
    for j, sample in enumerate(samples):
        data = pd.read_csv(os.path.join(test, sample))

        frame_time = data['msBetweenPresents'].values / 1000
        fps = frame_rate(frame_time, 1)
        intervals = [10, 5, 2, 1, 0.5]

        # save data
        results.loc[k, 'test'] = i
        results.loc[k, 'hw'] = test
        results.loc[k, 'sample'] = j
        results.loc[k, 'worst_frame'] = frame_time.max()
        results.loc[k, 'max_fps'] = fps.max()
        results.loc[k, 'avg_fps'] = fps.mean()
        results.loc[k, 'avg_fr'] = 1 / frame_time.mean()
        results.loc[k, '1%_low'] = np.percentile(fps, 1)

        for intr in intervals:    
            wifps = worst_interval_FPS(frame_time, intr)[0]
            results.loc[k, 'wifps_{}'.format(intr)] = wifps

        # plots
        if plot:
            fig, ax = worst_interval_FPS_plot(frame_time, intervals)
            name = '{}.png'.format(''.join(os.path.splitext(sample)[:-1]))
            fname = os.path.join(fig_path, name)
            fig.set_size_inches((16, 9))
            fig.savefig(fname)
            plt.close(fig)

        print(test, sample)
        k += 1

results.to_csv('results.csv')
