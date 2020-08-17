#!/bin/bash

prg=${1}
ds=${2}
username=${3}
pass=${4}
ip=$(ifconfig | grep -Eo 'inet (addr:)?([0-9]*\.){3}[0-9]*' | grep -Eo '([0-9]*\.){3}[0-9]*' | grep -v '127.0.0.1')

wget --content-disposition -c https://downloads.sourceforge.net/project/polybench/polybench-c-4.2.1-beta.tar.gz?r=https%3A%2F%2Fsourceforge.net%2Fprojects%2Fpolybench%2Ffiles%2Flatest%2Fdownload&ts=1597070379
sleep 10
tar xvf polybench-c-4.2.1-beta.tar.gz
chmod +x ./polybench-c-4.2.1-beta/utilities/time_benchmark.sh

sudo add-apt-repository --yes ppa:ubuntu-toolchain-r/test
sudo apt install --yes gcc-10 python3-pandas

git clone --single-branch --branch new-ds https://github.com/stefanocereda/polybench_data
cd ~/polybench_data/data/merged
filename=$(sed 's/\//_/g' <<< $prg)
wget https://polybench.s3.us-east-2.amazonaws.com/${filename}_${ds}.csv

# Use sudo for fifo polybench
cd ~/polybench_data
sudo python3 runner.py ${prg} ${ds} >log.out 2>log.err

cd ~/polybench_data
git pull
cat ~/result_${ds}.csv >> ~/polybench_data/data/${ds}_${filename}.csv
git add data/${ds}_${filename}.csv

git config user.email "cereda.ste@gmail.com"
git config user.name "Stefano Cereda"
git commit -m "auto upload ${filename}"
git push https://${username}:${pass}@github.com/stefanocereda/polybench_data

sleep 10
#sudo poweroff
