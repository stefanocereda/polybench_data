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
    "-fversion-loops-for-strides"]


import itertools
import os
import sys

prg = sys.argv[1]
print(prg)
for n_flags in range(len(FLAGS)):
    for opts_enabled in itertools.combinations(FLAGS, n_flags):
        opt_str = ''
        for opt in opts_enabled:
            opt_str += opt
            opt_str += ' '
        os.system('./collect.sh {} "{}"'.format(prg, opt_str))
