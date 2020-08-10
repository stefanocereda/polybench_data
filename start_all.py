PROGRAMS = [
    #"datamining/correlation/correlation",
    #"datamining/covariance/covariance",
    #"linear-algebra/blas/gemm/gemm",
    #"linear-algebra/blas/gemver/gemver",
    #"linear-algebra/blas/gesummv/gesummv",
    #"linear-algebra/blas/symm/symm",
    #"linear-algebra/blas/syr2k/syr2k",
    #"linear-algebra/blas/syrk/syrk",
    #"linear-algebra/blas/trmm/trmm",
    #"linear-algebra/kernels/2mm/2mm",
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
    #"linear-algebra/solvers/trisolv/trisolv",
    #"medley/deriche/deriche",
    #"medley/floyd-warshall/floyd-warshall",
    #"medley/nussinov/nussinov",
    #"stencils/adi/adi",
    #"stencils/fdtd-2d/fdtd-2d",
    #"stencils/heat-3d/heat-3d",
    #"stencils/jacobi-1d/jacobi-1d",
    #"stencils/jacobi-2d/jacobi-2d",
    #"stencils/seidel-2d/seidel-2d"
]

IPS = [
    '3.17.178.50',
    '3.15.16.221',
    '3.19.79.203',
    '18.219.227.220',
    '18.191.204.4',
    '18.216.216.92',
    '18.189.20.89',
    '3.14.147.237',
    '3.23.96.9',
    '18.219.152.32',
]
assert len(PROGRAMS) == len(IPS)

username=input("git username: ")
password=input("git password: ")

import os
import subprocess

for prg, ip in zip(PROGRAMS, IPS):
    os.system('scp -oStrictHostKeyChecking=no -i ~/.ssh/aws.pem setup_and_start.sh ubuntu@{}:/home/ubuntu/'.format(ip))
    os.system('ssh -oStrictHostKeyChecking=no -i ~/.ssh/aws.pem ubuntu@{} "nohup ./setup_and_start.sh {} {} {}" &'.format(ip, prg, username, password))
