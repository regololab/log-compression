# log-compression
read and compress custom log file

**Use

In log_list.yaml add list custom log:

#list file log
log1: /var/log/my_log/log.log

log2: /var/log/my_log3/log.log

log3: /var/www/html/project/log/manelog.log

**in crontab

add row: 

\* 4 * * * /usr/bin/python3 [address file]/log_compression.py
