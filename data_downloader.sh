IPS=""

for ip in ${IPS}; do
	if ping -c 1 ${ip} > /dev/null; then
		#rsync -e "ssh -i ~/.ssh/aws.pem" ubuntu@${ip}:/home/ubuntu/result_MINI.csv ./data/${ip}_MINI.csv
		#rsync -e "ssh -i ~/.ssh/aws.pem" ubuntu@${ip}:/home/ubuntu/result_SMALL.csv ./data/${ip}_SMALL.csv
		rsync -e "ssh -i ~/.ssh/aws.pem" ubuntu@${ip}:/home/ubuntu/result_STANDARD.csv ./data/${ip}_STANDARD.csv
	else
		echo ${ip} not reachable
	fi
done
