import pandas as pd
import os
import itertools

filenames = os.listdir(os.getcwd())
csvs = []
for fn in filenames:
    if fn[-4:] == '.csv':
        if 'MINI' in fn:
            ds = 'MINI'
        elif 'SMALL' in fn:
            ds = 'SMALL'
        elif 'STANDARD' in fn:
            ds = 'STANDARD'
        else:
            raise Exception("Unknown dataset")
        csv = pd.read_csv(fn, names=['benchmark', 'optimisations',
                                     'avg time', 'max dev time',
                                     'size'])
        csv['dataset'] = ds
        csvs.append(csv)
merged = pd.concat(csvs)

# we should not have more than one line per benchmark/optimisations/dataset
merged.drop_duplicates(subset=['benchmark', 'optimisations', 'dataset'],
                       keep='first', inplace=True)

# split into program/dataset
for prg, ds in itertools.product(merged['benchmark'].unique(),
                                 merged['dataset'].unique()):
    csv = merged[(merged['benchmark'] == prg) &
                 (merged['dataset'] == ds)]
    csv.to_csv('./merged/{}_{}.csv'.format(prg.replace('/','_'), ds), index=False)
print("Upload file to remote location with: aws s3 sync merged/ s3://polybench/")
