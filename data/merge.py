import pandas as pd
import os

filenames = os.listdir(os.getcwd())
csvs = []
for fn in filenames:
    if fn != 'merged.csv' and fn[-4:] == '.csv':
        if 'MINI' in fn:
            ds = 'MINI'
        elif 'SMALL' in fn:
            ds = 'SMALL'
        else:
            raise Exception("Unknown dataset")
        csv = pd.read_csv(fn, names=['benchmark', 'optimisations',
                                     'avg time', 'max dev time',
                                     'size'])
        csv['dataset'] = ds
        csvs.append(csv)
merged = pd.concat(csvs)
merged.to_csv('./merged.csv', index=False)
