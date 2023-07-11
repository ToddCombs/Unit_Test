# kill locust process
pkill -9 locust
rm -rf ./log_locust_*

sleep 1

if [ $# != 2 ]; then
    echo "USAGE: bash $0 worker_num master_ip"
	echo "e.g.: bash $0 16 127.0.0.1"
	exit 1;
fi

WorkerNum=$1

sleep 2

# locust -f locustfile.py --master &

for((i = 0; i < $WorkerNum; i++))
do
	locust -f demo/locust_test/locustfile.py --worker --master-host=$2 > log_locust_${i} 2>&1 &
done

echo "All Worker Started"
