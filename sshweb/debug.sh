#!/bin/bash

username=kaizhong
remote_ip="106.52.124.182"
remote_user=lighthouse

wget -O PORT $remote_ip:5000/start/$username
port=`cat ./PORT`
rm ./PORT

echo "remote at remote port: $port"
autossh -CNR 0.0.0.0:$port:0.0.0.0:22 $remote_user@$remote_ip
curl $remote_ip:5000/stop/$username
# ip=`cat $HOME/unitx_debug_ip`
#autossh -CNR $remote_ip:5555:localhost:36850 $remote_user@$remote_ip
