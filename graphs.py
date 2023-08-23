import pandas as pd
import numpy as np
import seaborn as sns
from matplotlib import pyplot as plt
sns.set_theme(style = 'whitegrid')

data = pd.read_csv('results.csv', index_col = 0)

# preview
print(data.groupby('hw').mean()[['avg_fps', '1%_low']].sort_values(['avg_fps', '1%_low']))

# ordering
hw_name = {
    'gskill_28c14': '2800 CL14 DR DC',
    'gskill_32c14_sc': '3200 CL14 DR SC',
    'gskill_32c14': '3200 CL14 DR DC',
    'king_32c22_sc': '3200 CL22 JEDEC DR SC',
    'gskill_36c16': '3600 CL16 DR DC',
    'gskill_36c18': '3600 CL18 DR DC',
    'gskill_40c22': '4000 CL22 DR DC',
    }

#data.sort_values(['avg_fps', '1%_low'], inplace = True)

data['hw'] = data['hw'].astype('category')
data['hw'] = data['hw'].cat.set_categories(hw_name.keys())
data.sort_values('hw', inplace = True)

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
ax.set_xlim((100, 180))
sns.despine(left = True, bottom = True)
ax.bar_label(ax.containers[0], fmt = '%.1f', padding = 20)
ax.bar_label(ax.containers[0], fmt = '%.1f', padding = 120, label_type = 'center',
              labels = [hw_name[l.get_text()] for l in bar.get_yticklabels()])
ax.bar_label(ax.containers[1], fmt = '%.1f', padding = -38)
ax.bar_label(ax.containers[2], fmt = '%.1f', padding = -50)
ax.set_yticks([])

ax.legend(ncol = 1, loc = 3, bbox_to_anchor = (-0.008, 0.0), frameon = True)

fig.suptitle('Dota 2 FPS vs DDR4 RAM - 3D V-Cache CPU')
ax.set_title('Match ID: 7233123840, 22:05 > 23:25, 5800X3D, A2000 12GB')
ax.set_ylabel('RAM configuration')
ax.set_xlabel('FPS (8 samples)')
fig.show()
