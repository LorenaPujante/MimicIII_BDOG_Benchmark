#!/bin/bash

# Encender la bd
checkPort=`lsof -i :7300 -S | grep 7300`
/home/lorena/graphdb-10.2.2/bin/graphdb start -s &>/dev/null &
while [[ ${checkPort} == "" ]]; do
    sleep 1
    checkPort=`lsof -i :7300 -S | grep 7300`
done
#echo -e "checkPort: ${checkPort}"

# Ejecutar en segundo plano bucle para medir memoria maxima
./getPeak.sh graphdb &

# Ejecutar query pasada como parametro
$1

# Matar servicio de la bd
pid=`ps -aux | grep -m 1 graphdb | tr -s " " | cut -d " " -f 2`
kill -9 ${pid}
