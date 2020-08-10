#create ubuntu server 18.04 spot a1.medium instance
wget --content-disposition -c https://downloads.sourceforge.net/project/polybench/polybench-c-4.2.1-beta.tar.gz?r=https%3A%2F%2Fsourceforge.net%2Fprojects%2Fpolybench%2Ffiles%2Flatest%2Fdownload&ts=1597070379
tar xvf polybench-c-4.2.1-beta.tar.gz
sudo add-apt-repository --yes ppa:ubuntu-toolchain-r/test
sudo apt update
sudo apt install --yes gcc-10
