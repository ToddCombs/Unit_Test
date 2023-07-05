# kill locust process
pkill -9 locust

sleep 1

if [ $# != 1 ]; then
    echo "USAGE: bash $0 worker_num"
	echo "e.g.: bash $0 16"
	exit 1;
fi

WorkerNum=$1

locust -f locustfile.py --master &

sleep 2

for((i = 0; i < $WorkerNum; i++))
do
	locust -f locustfile.py --worker > /dev/null 2>&1 &
done
