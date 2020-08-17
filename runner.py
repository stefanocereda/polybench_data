# all the flags in -O3, start from -O2 in the bash script
FLAGS = [
    "-fgcse-after-reload",
    "-fipa-cp-clone",
    "-floop-interchange",
    "-floop-unroll-and-jam",
    "-fpeel-loops",
    "-fpredictive-commoning",
    "-fsplit-loops",
    "-fsplit-paths",
    "-ftree-loop-distribution",
    "-ftree-loop-vectorize",
    "-ftree-partial-pre",
    "-ftree-slp-vectorize",
    "-funswitch-loops",
    "-fvect-cost-model",
    "-fvect-cost-model=dynamic",
    "-fversion-loops-for-strides"
]


import itertools
import os
import sys
import pandas as pd

prg = sys.argv[1]
ds = sys.argv[2]

try:
    dataset = pd.read_csv('./data/merged/{}_{}.csv'.format(prg.replace('/','_'), ds))
except:
    dataset = None

if dataset is not None:
    dataset.set_index(['benchmark', 'dataset', 'optimisations'], inplace=True)


print(prg, ds)
for n_flags in range(len(FLAGS)+1):
    for opts_enabled in itertools.combinations(FLAGS, n_flags):
        opt_str = ''
        for opt in opts_enabled:
            opt_str += opt
            opt_str += ' '
        if dataset is None or (prg, ds, opt_str) not in dataset.index:
            os.system('./run_prg.sh {} "{}" {}'.format(prg, opt_str, ds))
