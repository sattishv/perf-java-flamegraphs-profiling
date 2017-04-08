# perf-java-flamegraphs-profiling
This repository provides a series of scripts to profile applications using the linux 'perf' tool, including java applications without intrusive or the need to additional software, and create a stream of data that can be stored in a document-based database for later processing and flamegraph generation in near real-time and on-demand.

## Requirements

### [linux perf tool](https://perf.wiki.kernel.org/index.php/Main_Page)
With perf, system-wise profiling is achievable at a very low level.

* :exclamation: _**perf is able to profile from the kernel level upwards and thus requires adjusting of the level of access user have. To create application and java flamegraphs, kernel addresses translation is not required, but still some access has to be provided by the admin. To allow profiling collection, run the allow_perf.sh script**_ :exclamation:
* To install perf tools, you can use the 'install-perf' script

### [Perf Java Mapping Agent](https://github.com/jvm-profiling-tools/perf-map-agent)
Because perf is not able to map Java's JVM bytecode addresses, this external mapping agent is needed
* To install these tools on the system, you can use the 'install-perf-java-mapper' script
* :exclamation: _**In order to attach the mapping agent to all running java machines, currently admin priviledges are required.**_ :exclamation:

### [FlameGraphs generation tool](https://github.com/brendangregg/FlameGraph)
In order to process the raw data generated by the perf tool, the scripts from the original flamegraphs idea project by Brendan Gregg are used.
* To download these scripts, you can use the 'install-flamegraphs' script

### [MongoDB](https://www.mongodb.com/) + [Eve (python REST API framework)](http://python-eve.org/)
* To store the documents that create the profiling data, a MongoDB database is used, although any document-based database is valid.
* To store the documents using a REST API, Eve is used.


## Download and install
```
git clone https://github.com/JonatanEnes/perf-java-flamegraphs-profiling
cd perf-java-flamegraphs-profiling
bash install-dependencies.sh
bash install-perf.sh
bash install-flamegraphs.sh
bash install-perf-java-mapper.sh
```

## Usage

There are three main script that can be used individually, profile.sh, map.sh and send.sh

### Profiler
The profile, in the profile.sh script, polls continually profiling data with the 'perf record' comand, it has a time window (time between file dumps) and a profiling frequency (number of stack samples collected per second) as adjustable parameters.

* To profile with a time window of 20 seconds (default is 30) with a frequency of 202 Hz (default is 303), run:
```
bash profile.sh 20 202
```
* The resulting file will be stored with the timestamp in a recording folder while the polling is not finished and in an out folder once finished.

* :exclamation: _**The time window parameter adjusts the resolution of the time window that can be later used to create flamegraphs between two time points. For example, with a profiling time window of 20 seconds, profiling data will be plotted with 20 seconds increments. This parameters can be tuned for a more real-time scenario.**_ :exclamation:

### Java Mapper
The java mapper is able to connect to the instance running JVMs and do a dump of their address spaces to a map file that is later used to create java-translated profiling info and documents. Currently, to do this dumping, the 'jmaps' script from the FlameGraph repository. The script accepts a time window configurable parameter.

* To continually map the instance running java machines every 10 seconds (default is 10), run:
```
bash map.sh 10
```

* :exclamation: _**Be aware that the 'jmaps' script uses a hardcoded JAVA_HOME path so as to force the usage of Java 8 or higher**_ :exclamation:

* :exclamation: _**In order to avoid missing data, the mapper should do a dump with a lower frequency than the life expectancy of the java machines. Any java machine that ends without being mapped will likely incur in a loss of data and result in unmapped addresses.**_ :exclamation:

### Sender
the sender script processes the output of the profiler using 'perf script', which in turn uses the maps created by the mapper and finally sends the processed data to a MongoDB database.

* To continually send the generated data every 30 seconds (default is 30), run:
```
bash send.sh 30
```

## Example

Using the simple draw.sh script and passing two UNIX timestamps variables as TIME_START and TIME_END, it is possible to retrieve raw data from the mongodb database and generate locally a flamegraph in svg format, which can be interactively viewed in a browser.
```
bash draw.sh 1491650215 1491650518
```

