set -x

prg=${1}
username=${2}
pass=${3}
ip=$(ifconfig | grep -Eo 'inet (addr:)?([0-9]*\.){3}[0-9]*' | grep -Eo '([0-9]*\.){3}[0-9]*' | grep -v '127.0.0.1')

wget --content-disposition -c https://downloads.sourceforge.net/project/polybench/polybench-c-4.2.1-beta.tar.gz?r=https%3A%2F%2Fsourceforge.net%2Fprojects%2Fpolybench%2Ffiles%2Flatest%2Fdownload&ts=1597070379

sleep 10

tar xvf polybench-c-4.2.1-beta.tar.gz

sudo add-apt-repository --yes ppa:ubuntu-toolchain-r/test
sudo apt update
sudo apt install --yes gcc-10
git clone --single-branch --branch new-ds https://github.com/stefanocereda/polybench_data

chmod +x ./polybench-c-4.2.1-beta/utilities/time_benchmark.sh

cd ~/polybench_data

sudo python3 runner.py ${1} >log.out 2>log.err

cd ~/polybench_data
mkdir data
mv ~/result.csv ~/polybench_data/data/${ip}.csv
git add data/${ip}.csv

git config user.email "cereda.ste@gmail.com"
git config user.name "Stefano Cereda"
git commit -m "auto upload ${1}"
git push https://${username}:${pass}@github.com/stefanocereda/polybench_data
