#!/bin/bash

# Encender la bd
checkPort=`lsof -i :7474 -S | grep 7474`
/home/lorena/neo4j-4.4.18/bin/neo4j start &>/dev/null &
while [[ ${checkPort} == "" ]]; do
    sleep 1
    checkPort=`lsof -i :7474 -S | grep 7474`
done
#echo -e "checkPort: ${checkPort}"

# Ejecutar en segundo plano bucle para medir memoria maxima
./getPeak.sh neo4j- &

# Ejecutar query pasada como parametro
$1

# Matar servicio de la bd
pid=`ps -aux | grep -m 1 neo4j- | tr -s " " | cut -d " " -f 2`
kill -9 ${pid}

