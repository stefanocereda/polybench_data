PROGRAM=$1
OPTIONS=$2

cd ~/polybench-c-4.2.1-beta

# compile
gcc -O2 -lc ${OPTIONS} -I utilities -I ${PROGRAM} utilities/polybench.c ${PROGRAM}.c -DPOLYBENCH_TIME -DPOLYBENCH_LINUX_FIFO_SCHEDULER -DPOLYBENCH_CYCLE_ACCURATE_TIMER -DSTANDARD_DATASET -o out

 # run
./utilities/time_benchmark.sh ./out > log

# store result
avg=$(cat log | grep Normalized | grep -o '[0-9.]*')
max_dev=$(cat log | grep deviation | grep -o '[0-9.]*' | tail -1)

cd ~
echo ${PROGRAM},${OPTIONS},${avg},${max_dev} >> result.csv