#!/bin/bash

pidInit=`ps -aux | grep -m 1 $1 | tr -s " " | cut -d " " -f 2`
memInit=`ps -aux | grep -m 1 $1 | tr -s " " | cut -d " " -f 6` # Antes 5 (VmSize)	# 6 (VmRSS)

maxmem=0

#$@ &
pid=`ps -aux | grep -m 1 $1 | tr -s " " | cut -d " " -f 2`
while [[ ${pid} -eq ${pidInit} ]]; do
    mem=`cat /proc/${pid}/status | grep VmRSS | awk '{print $2}'`	# Antes 'grep VmSize'
    if [[ ${mem} -gt ${maxmem} ]]; then
        maxmem=${mem}
    fi
    sleep 1
    savedpid=${pid}
    pid=`ps -aux | grep -m 1 $1 | tr -s " " | cut -d " " -f 2`
done

#echo -e "Initial memory usage is: ${memInit} KB.\nMax memory usage is: ${maxmem} KB"
echo "${memInit} ${maxmem}"
