mkdir -p timestamps
<<<<<<< HEAD
export LC_ALL=C
=======

export MONGODB_PORT=8000
>>>>>>> 33aa3f85fd5c56e9425dc5a99d555438c4d4777a
TIME_WINDOW_SECONDS="${1:-30}"
echo "[MONGODB SENDER] Going to send data every '$TIME_WINDOW_SECONDS' seconds."
while true
do
	for filename in "out"/*.data
	do
		if [ $filename == "out/*.data" ]; then
		   #Skip directory expansion failed because it was empty
		   echo "Nothing to send at " `date`
		else
		   timestamp=$(echo $filename | cut -d "/" -f 2 | cut -d "." -f 1)
		   echo "Sending" $filename "with timestamp " $timestamp
		   export TIMESTAMP=$timestamp
		   (perf script -F comm,pid,tid,cpu,time,event,ip,sym,dso -i $filename 2>/dev/null | ./FlameGraph/stackcollapse-perf.pl --pid | python ./scripts/stacks-to-jsons.py | python ./scripts/jsons-to-mongodb.py && rm $filename) &
		fi
	done
	sleep $TIME_WINDOW_SECONDS
done


