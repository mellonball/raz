cd /home/pi/jasper/client/
rm -rf ../old_client
rm -f start_log
python main.py > start_log 2>start_log  &
