#!/bin/bash

ip_address="$1"
user="$2"
password="$3"


# CPU Usage
cpu_usage=$(sshpass -p $password ssh $user@$ip_address 'top -b -n 1 | grep -i "cpu(s)" | awk '\''{print "CPU min:", $8, "%"}; {print "CPU avg:", $2, "%"}; {print "CPU max:", $4, "%"}'\')

echo "CPU Usage: $cpu_usage"

echo "========================================================================"

# Memory Usage
mem_usage=$(sshpass -p $password  ssh $user@$ip_address "free | grep Mem | awk '{print \"RAM usage: is\", \$3/\$2 * 100.0\"%\"}'")
echo "Memory Usage: $mem_usage"

echo "========================================================================"


# disk Usage
#disk_usage=$(sshpass -p $password  ssh $user@$ip_address 'df -Th | column -t')
disk_usage=$(sshpass -p $password ssh $user@$ip_address 'df -Th | awk '\''BEGIN {print "Filesystem,Type,Size,Used,Available,Use%,Mounted on"} NR > 1 {print $1 "," $2 "," $3 "," $4 "," $5 "," $6 "," $7}'\'' > disk_usage.csv')
#echo "Disk Usage: $disk_usage"
