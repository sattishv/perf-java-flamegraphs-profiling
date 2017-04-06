for filename in "out"/*
do
   perf script -F comm,pid,tid,cpu,time,event,ip,sym,dso -i $filename 2>/dev/null | ./FlameGraph/stackcollapse-perf.pl --pid | python ./scripts/stacks-to-jsons.py | python ./scripts/jsons-to-mongodb.py
   rm $filename
done
