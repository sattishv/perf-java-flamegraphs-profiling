mkdir -p out
mkdir -p recording

hash perf 2>/dev/null || { echo >&2 "I require perf but it's not installed.  Aborting."; exit 1; }

while true
do
  out_file_name=`date +%s`.data
  perf record -F 505 -a -g -o recording/$out_file_name -- sleep 30
  mv recording/$out_file_name out
done
