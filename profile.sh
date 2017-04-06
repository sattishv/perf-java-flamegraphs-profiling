while true
do
  out_file_name=`date +%s`.data
  perf record -F 505 -a -g -o recording/$out_file_name -- sleep 30
  mv recording/$out_file_name out
done
