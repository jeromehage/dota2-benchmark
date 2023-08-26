import pandas as pd
import numpy as np
import seaborn as sns
from matplotlib import pyplot as plt
sns.set_theme(style = 'whitegrid')

data = pd.read_csv('results.csv', index_col = 0)

# preview
print(data.groupby('hw').mean()[['avg_fps', '1%_low']].sort_values(['avg_fps', '1%_low']))

data.sort_values(by = 'avg_fps', inplace = True)

# plot
fig, ax = plt.subplots(figsize = (9, 5))

plots = [
    ('avg_fps', 'Average', 'blue'),
    ('wifps_10', 'Worst 10s', 'yellow'),
    ('1%_low', '1% low', 'orange'),
    ]

for name, label, color in plots:
    bar = sns.barplot(
        data = data, x = name, y = 'hw',
        label = label,
        color = color, alpha = 0.7,
        capsize = 0.4, errwidth = 1,
        ax = ax,
        )

# fix bar labels
sns.despine(left = True, bottom = True)
ax.bar_label(ax.containers[0], fmt = '%.1f', padding = 10)
ax.bar_label(ax.containers[1], fmt = '%.1f', padding = 10)
ax.bar_label(ax.containers[2], fmt = '%.1f', padding = -40)

ax.legend(ncol = 1, loc = 3, frameon = True)

fig.suptitle('Dota 2 FPS benchmark')
ax.set_title('Match ID: 7233123840, 22:05 > 23:25')
ax.set_ylabel('Configuration')
ax.set_xlabel('FPS')
fig.show()
