TIME_START=1491649483
TIME_END=1491649653
rm ./flamegraph.svg
python ./scripts/mongodb-to-jsons.py $TIME_START $TIME_END | ./scripts/jsons-to-stacks.py | ./FlameGraph/flamegraph.pl --color=java > flamegraph.svg
