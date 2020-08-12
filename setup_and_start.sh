prg=${1}
username=${2}
pass=${3}
ip=$(ifconfig | grep -Eo 'inet (addr:)?([0-9]*\.){3}[0-9]*' | grep -Eo '([0-9]*\.){3}[0-9]*' | grep -v '127.0.0.1')

wget --content-disposition -c https://downloads.sourceforge.net/project/polybench/polybench-c-4.2.1-beta.tar.gz?r=https%3A%2F%2Fsourceforge.net%2Fprojects%2Fpolybench%2Ffiles%2Flatest%2Fdownload&ts=1597070379
sleep 10
tar xvf polybench-c-4.2.1-beta.tar.gz
chmod +x ./polybench-c-4.2.1-beta/utilities/time_benchmark.sh

sudo add-apt-repository --yes ppa:ubuntu-toolchain-r/test
sudo apt update
sudo apt install --yes gcc-10 python3-pandas

git clone --single-branch --branch new-ds https://github.com/stefanocereda/polybench_data
cd ~/polybench_data/data/merged
filename=$(sed 's/\//_/g' <<< $prg)
wget https://polybench.s3.us-east-2.amazonaws.com/${filename}.csv

# Use sudo for fifo polybench
cd ~/polybench_data
sudo python3 runner.py ${1} >log.out 2>log.err

cd ~/polybench_data
mv ~/result_MINI.csv ~/polybench_data/data/MINI_${ip}.csv
mv ~/result_SMALL.csv ~/polybench_data/data/SMALL_${ip}.csv
git add data/MINI_${ip}.csv
git add data/SMALL_${ip}.csv

git config user.email "cereda.ste@gmail.com"
git config user.name "Stefano Cereda"
git pull
git commit -m "auto upload ${1}"
git push https://${username}:${pass}@github.com/stefanocereda/polybench_data

sleep 10
sudo poweroff
