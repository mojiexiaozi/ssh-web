#!/bin/bash

remote_ip="106.52.124.182"
remote_user=lighthouse
port=6000
echo "remote at remote port: $port"

autossh -v -o "ExitOnForwardFailure=yes" -CNR 0.0.0.0:6001:0.0.0.0:22 $remote_user@$remote_ip
