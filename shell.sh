#!/bin/bash



#ssh root@172.16.1.140

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
disk_usage=$(sshpass -p $password  ssh $user@$ip_address 'df -Th | column -t')
echo "Disk Usage: $disk_usage"
