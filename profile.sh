mkdir -p out
mkdir -p recording

hash perf 2>/dev/null || { echo >&2 "I require foo but it's not installed.  Aborting."; exit 1; }

perf record  -a -- sleep 1 1>/dev/null 2>/dev/null
if [ $? -eq 0 ]; then
    echo ""
else
    echo "perf couldn't execute due to permission failures, run the allow_perf.sh script and try again or run perf record manually and check for errors"
    exit 1;
fi

while true
do
  out_file_name=`date +%s`.data
  perf record -F 505 -a -g -o recording/$out_file_name -- sleep 30
  mv recording/$out_file_name out
done

