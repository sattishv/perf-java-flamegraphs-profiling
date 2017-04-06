KERNEL_VERSION=`uname -r`

# Install perf
	sudo apt install linux-tools-$KERNEL_VERSION
	sudo apt install linux-cloud-tools-$KERNEL_VERSION
	sudo apt install linux-tools-generic
	sudo apt install linux-cloud-tools-generic
	

git clone https://github.com/brendangregg/FlameGraph
git clone https://github.com/jvm-profiling-tools/perf-map-agent
cd perf-map-agent
cmake .
make
cd ..
sudo cp -R perf-map-agent /usr/lib/jvm/perf-map-agent
rm -Rf perf-map-agent
