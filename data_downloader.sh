IPS=''

for ip in ${IPS}; do
	rsync -e "ssh -i ~/.ssh/aws.pem" ubuntu@${ip}:/home/ubuntu/result_MINI.csv ./data/${ip}_MINI.csv
	rsync -e "ssh -i ~/.ssh/aws.pem" ubuntu@${ip}:/home/ubuntu/result_SMALL.csv ./data/${ip}_SMALL.csv
done
