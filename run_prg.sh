PROGRAM=$1
OPTIONS=$2

cd ~/polybench-c-4.2.1-beta

# compile
gcc-10 -O2 ${OPTIONS} -I utilities -I ${PROGRAM} utilities/polybench.c ${PROGRAM}.c -DPOLYBENCH_LINUX_FIFO_SCHEDULER -DPOLYBENCH_TIME -DMINI_DATASET -o out -lc -lm

 # run
./utilities/time_benchmark.sh ./out > log

# store result
avg=$(cat log | grep Normalized | grep -o '[0-9.]*')
max_dev=$(cat log | grep deviation | grep -o '[0-9.]*' | tail -1)
file_size=$(stat -c %s ./out)

cd ~
echo ${PROGRAM},${OPTIONS},${avg},${max_dev},${file_size} >> result.csv
