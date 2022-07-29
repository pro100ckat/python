#!/bin/bash

hdfs dfs -rm -r /output

yarn jar c:\hadoop-2.8.0\share\hadoop\tools\lib\hadoop-streaming-*.jar \
-input /input/file1 \
-output /output \
-file .\mapper.py \
-file .\reducer.py \
-mapper "python .\mapper.py" \
-reducer "python .\reducer.py"

hadoop fs -text /output/part-00000
