TIMESTAMP_NOW=`date '+%s'`
TEN_MINUTES="600"
TIMESTAMP_10minutes_ago=$((TIMESTAMP_NOW-TEN_MINUTES))

TIME_START="${1:-$TIMESTAMP_10minutes_ago}"
TIME_END="${2:-$TIMESTAMP_NOW}"

DATE_START=`date --date @${TIME_START} +"%Y/%m/%d-%H:%M:%S"`
DATE_END=`date --date @${TIME_END} +"%Y/%m/%d-%H:%M:%S"`

echo "Drawing flamegraphs from $TIME_START ($DATE_START) to $TIME_END ($DATE_END)"
rm  ./flamegraph.svg 2> /dev/null
python ./scripts/mongodb-to-jsons.py $TIME_START $TIME_END | ./scripts/jsons-to-stacks.py | ./FlameGraph/flamegraph.pl --color=java > flamegraph.svg
