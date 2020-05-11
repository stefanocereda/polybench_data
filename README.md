# PolyBench compiler autotuning dataset 
This repository contains the dataset we used for the paper "A Collaborative Filtering Approah for the Automatic Tuning of Compiler Optimisations" available at https://arxiv.org/abs/2005.04092

## Optimisations
We following the approach used in https://github.com/amirjamez/COBAYN, and all the files have the same format used in COBAYN.
We consider 7 binary GCC flags:
-funsafe-math-optimisations
-fno-guess-branch-probability
-fno-ivopts
-fno-tree-loop-optimise
-fno-inline-functions
-funroll-all-loops
-O2 or -O3
For a total of 128 possible combinations.

## Instance
To collect the PolyBench dataset, we use an Amazon EC2 a1.medium instance, which is equipped with a single ARMv8 gravitron processor and 2GB of ram, Ubuntu Server 18.04 and PolyBench 4.2.1.

## Execution times
The exec_times.csv file contains the execution time obtained by each benchmark available in PolyBench when compiled with each combination of optimisations.
The first column contains the benchmark name, columns 2-8 specify the enabled compiler optimisations: X means the optimisation was turned off.
We then report the execution times obtained using the MINI_DATASET, SMALL_DATASET, STANDARD_DATASET and LARGE_DATASET as defined in PolyBench. The fifth execution time column is zero as we did not use the EXTRALARGE_DATASET.
The last column contains the execution time.
We timed the execution using the PolyBench timing and enabling the FIFO scheduler.

## MICA metrics
We also collected MICA metrics (https://github.com/boegel/MICA) using Intel PIN 3.10.
We report these values in micaTable.csv, each line contains the benchmark name, the dataset size (mini, small, standard) and the values of the MICA metrics
