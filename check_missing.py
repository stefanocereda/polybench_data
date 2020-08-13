PROGRAMS = [
    "datamining/correlation/correlation",
    "datamining/covariance/covariance",
    "linear-algebra/blas/gemm/gemm",
    "linear-algebra/blas/gemver/gemver",
    "linear-algebra/blas/gesummv/gesummv",
    "linear-algebra/blas/symm/symm",
    "linear-algebra/blas/syr2k/syr2k",
    "linear-algebra/blas/syrk/syrk",
    "linear-algebra/blas/trmm/trmm",
    "linear-algebra/kernels/2mm/2mm",
    "linear-algebra/kernels/3mm/3mm",
    "linear-algebra/kernels/atax/atax",
    "linear-algebra/kernels/bicg/bicg",
    "linear-algebra/kernels/doitgen/doitgen",
    "linear-algebra/kernels/mvt/mvt",
    "linear-algebra/solvers/cholesky/cholesky",
    "linear-algebra/solvers/durbin/durbin",
    "linear-algebra/solvers/gramschmidt/gramschmidt",
    "linear-algebra/solvers/ludcmp/ludcmp",
    "linear-algebra/solvers/lu/lu",
    "linear-algebra/solvers/trisolv/trisolv",
    "medley/deriche/deriche",
    "medley/floyd-warshall/floyd-warshall",
    "medley/nussinov/nussinov",
    "stencils/adi/adi",
    "stencils/fdtd-2d/fdtd-2d",
    "stencils/heat-3d/heat-3d",
    "stencils/jacobi-1d/jacobi-1d",
    "stencils/jacobi-2d/jacobi-2d",
    "stencils/seidel-2d/seidel-2d"
]
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
import pandas as pd

tot_missing = 0
tot_done = 0

for prg in PROGRAMS:
    try:
        dataset = pd.read_csv('./data/merged/{}.csv'.format(prg.replace('/','_')))
        dataset.set_index(['benchmark', 'dataset', 'optimisations'], inplace=True)
    except:
        dataset = None

    for ds in ['MINI', 'SMALL']:
        missing = 0

        for n_flags in range(len(FLAGS)+1):
            for opts_enabled in itertools.combinations(FLAGS, n_flags):
                opt_str = ''
                for opt in opts_enabled:
                    opt_str += opt
                    opt_str += ' '
                if dataset is None or (prg, ds, opt_str) not in dataset.index:
                    missing += 1
                else:
                    tot_done +=1
        tot_missing += missing
        print('{},{},{}'.format(prg, ds, missing))

print("Missing {} samples out of {}, we are at {}%".format(tot_missing,
                                                           tot_missing+tot_done, tot_done/(tot_done+tot_missing)*100))
