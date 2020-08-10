IPS="3.128.90.84 "

for ip in ${IPS}; do
	rsync -e "ssh -i ~/.ssh/aws.pem" ubuntu@${ip}:/home/ubuntu/result.csv ./data/${ip}.csv
done
