#
#


#!/bin/bash


# Define an array of 10 servers to monitor
servers=(3.6.48.236 65.1.19.50 13.126.158.236 101.53.136.30 13.232.82.175 164.52.216.173  164.52.202.12  164.52.202.13 164.52.202.33  164.52.202.17  164.52.202.46  164.52.202.19 164.52.195.60 164.52.195.62 164.52.195.5 164.52.195.20 3.6.233.10 3.108.77.241 3.108.9.178 65.1.239.64 3.108.75.174 3.7.54.141 192.168.101.32 192.168.101.34 192.168.101.23 192.168.101.24 192.168.101.14 )


# Create a CSV file with headers
echo "Server,Date,Load_Average,Total_RAM,Used_RAM,Available_RAM,Total_Disk,Used_Disk,Available_Disk,Disk_used_in_%,partition,Total_Disk_nvme1n1,Used_Disk_nvme1n1,Available_Disk_nvme1n1,Disk_used_in_%_nvme1n1" > server_monitoring.csv

# Loop through the server array
for server in "${servers[@]}"; do
  # Try to SSH into the server and retrieve its load average, disk usage, and memory usage
  date_stamp=$(date "+%Y-%m-%d %H:%M:%S")
  load_average=$(ssh dba@"$server" "cat /proc/loadavg | awk '{print \$3}'")
  total_ram=$(ssh dba@"$server" "free -h | awk '/Mem:/ {print \$2}'")
  used_ram=$(ssh dba@"$server" "free -h | awk '/Mem:/ {print \$3}'")
  available_ram=$(ssh dba@"$server" "free -h | awk '/Mem:/ {print \$7}'")
  total_disk=$(ssh dba@"$server" "df -h | awk '/\/$/ {print \$2}'")
  used_disk=$(ssh dba@"$server" "df -h | awk '/\/$/ {print \$3}'")
  available_disk=$(ssh dba@"$server" "df -h | awk '/\/$/ {print \$4}'")
  disk_used_percentage=$(ssh dba@"$server" "df -h | awk '/\/$/ {print \$5}'")

  # Adding information for /dev/nvme1n1 filesystem
  nvme1n1_total_disk=$(ssh dba@"$server" "df -h | awk '/\/dev\/nvme1n1/ {print \$2}'")
  nvme1n1_used_disk=$(ssh dba@"$server" "df -h | awk '/\/dev\/nvme1n1/ {print \$3}'")
  nvme1n1_available_disk=$(ssh dba@"$server" "df -h | awk '/\/dev\/nvme1n1/ {print \$4}'")
  nvme1n1_used_percentage=$(ssh dba@"$server" "df -h | awk '/\/dev\/nvme1n1/ {print \$5}'")

  # Append the data to the CSV file
  echo "$server,$date_stamp,$load_average,$total_ram,$used_ram,$available_ram,$total_disk,$used_disk,$available_disk,$disk_used_percentage,/dev/nvme1n1,$nvme1n1_total_disk,$nvme1n1_used_disk,$nvme1n1_available_disk,$nvme1n1_used_percentage" >> server_monitoring.csv
done

cp -r server_monitoring.csv /home/chetan/work/disk_usage/server_monitoring$(date +%Y_%m_%dT%H_%M_%S).csv
