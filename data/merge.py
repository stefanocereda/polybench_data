import pandas as pd
import os

filenames = os.listdir(os.getcwd())
csvs = []
for fn in filenames:
    if fn[-4:] == '.csv':
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

# split into programs
for prg in merged['benchmark'].unique():
    csv = merged[merged['benchmark'] == prg]
    csv.to_csv('./merged/{}.csv'.format(prg.replace('/','_')), index=False)
print("Upload file to remote location with: aws s3 sync merged/ s3://polybench/")
