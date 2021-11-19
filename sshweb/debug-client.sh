remote="106.52.124.182"
web="$remote:5000/getport"
custom_name="kaizhong"
username="kimi"
wget -O PORT $web/$custom_name
port=`cat ./PORT`
rm ./PORT
ssh $username@$remote -p $port
