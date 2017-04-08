TIME_START=1491650215
TIME_END=1491650518
rm ./flamegraph.svg
python ./scripts/mongodb-to-jsons.py $TIME_START $TIME_END | ./scripts/jsons-to-stacks.py | ./FlameGraph/flamegraph.pl --color=java > flamegraph.svg
