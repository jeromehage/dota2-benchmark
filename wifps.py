import numpy as np
from matplotlib import pyplot as plt

def frame_rate(frames, interval = 1.0):
    """Calculates frame rate, equal to FPS if interval is 1.0"""
    N = len(frames)
    i, j = 0, 0
    out = []
    while i < N:
        while sum(frames[i: j]) < interval and j < N:
            j += 1
        if j < N:
            frac = (interval - sum(frames[i: j - 1])) / frames[j - 1]
            out += [j - i - 1 + frac]
        i += 1
    return np.array(out)

def worst_interval_FPS(frame_time, interval_length = 10):
    """finds the worst average FPS in windows of a specified length (in seconds)"""
    rate = frame_rate(frame_time, interval_length)
    fps = rate / interval_length
    return fps.min(), fps.argmin()

def worst_interval_FPS_plot(frame_time, intervals = [1, 2, 5, 10]):
    """plot WIFPS for different window sizes"""

    frames = np.array(frame_time)
    time = frames.cumsum()
    fps = frame_rate(frames, 1)

    # metric
    metrics = []
    for intr in intervals:    
        wifps = worst_interval_FPS(frames, intr)
        start = frames[:wifps[1]].sum()
        end = start + intr
        metrics += [(intr, wifps[0], start, end)]

    # main
    fig, ax = plt.subplots()
    ax.plot(time, 1 / frames, label = 'FPS instant', color = 'tab:blue')
    ax.plot(time[-len(fps):], fps, label = 'FPS', color = 'tab:pink')

    perc = np.percentile(fps, 1)
    ax.axhline(y = perc, color = 'tab:orange', linewidth = 2,
               label = '1% lows = {}'.format(np.round(perc, 1)))

    ax.axhline(y = fps.mean(), color = 'tab:green', linewidth = 2,
               label = 'avg = {}'.format(np.round(fps.mean(), 1)))

    for intr, val, start, end in metrics:
        ax.hlines(y = val, xmin = start, xmax = end,
                  color = 'tab:red', zorder = 20, linewidth = 3,
                  label = 'WIFPS({}s) = {}'.format(intr, np.round(val, 1)))

    fig.suptitle('Worst Interval FPS')
    ax.legend()
    return fig, ax

if __name__ == '__main__':

    import scipy.stats as st

    # setup data
    parts = [(5, 1000),
             (25, 100),
             (50, 200),
             (20, 600),
             (200, 20),
             (25, 290)]

    data = []
    for sc, sz in parts:
        data += [st.invgamma.rvs(a = 5, loc = 10, scale = sc, size = sz)]

    frames_ms = np.concatenate(data)
    frame_time = frames_ms / 1000

    ## main
    plt.hist(frames_ms, bins = 20)
    plt.title('frame time (ms)')
    plt.show()

    fig, ax = worst_interval_FPS_plot(frame_time)
    fig.show()
