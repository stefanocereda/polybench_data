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

dataset = pd.read_csv('./data/merged/{}.csv'.format(prg.replace('/','_')))

print(prg)
match_prg = dataset['benchmark'] == prg
for ds in ['MINI', 'SMALL']:
    match_ds = dataset['dataset'] == ds
    match_ds = match_prg & match_ds
    for n_flags in range(len(FLAGS)+1):
        for opts_enabled in itertools.combinations(FLAGS, n_flags):
            opt_str = ''
            for opt in opts_enabled:
                opt_str += opt
                opt_str += ' '
            match_flag = dataset['optimisations'] == opt_str
            match_flag = match_flag & match_ds
            if sum(match_flag) != 1:
                os.system('./run_prg.sh {} "{}" {}'.format(prg, opt_str, ds))
