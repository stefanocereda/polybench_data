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
DATASETS = [
    'MINI',
    'SMALL'
]


import pandas as pd

all_dss = []
for prg in PROGRAMS:
    ds = pd.read_csv('./data/merged/{}.csv'.format(prg.replace('/', '_')))
    all_dss.append(ds)

dataset = pd.concat(all_dss)
for flag in FLAGS:
    dataset[flag] = dataset['optimisations'].str.contains(flag)
dataset.drop('optimisations', axis=1, inplace=True)
dataset.fillna(False, inplace=True)
cols = ['benchmark', 'dataset', *FLAGS, 'avg time', 'max dev time', 'size']
dataset = dataset[cols]
dataset.to_csv('./polybech_16.csv', index=False)
