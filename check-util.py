# import psutil, socket

# def check_system():
#     # Fetch data
#     hostname = socket.gethostname()
#     cpu_usage = psutil.cpu_percent(interval=1)
#     memory_usage = psutil.virtual_memory()
#     disk_usage          = psutil.disk_usage('/')

#     # Process memory data
#     memory_total        = memory_usage.total/1024**3
#     memory_free         = memory_usage.free/1024**3
#     memory_used         = memory_usage.used/1024**3
#     memory_used_percent = memory_usage.percent

#     # Process disk data
#     disk_total        = disk_usage.total/1024**3
#     disk_free         = disk_usage.free/1024**3
#     disk_used         = disk_usage.used/1024**3
#     disk_used_percent = disk_usage.percent


import os
 
# Getting all memory using os.popen()
total_memory, used_memory, free_memory = map(
    int, os.popen('free -t -m').readlines()[-1].split()[1:])
 
# Memory usage
print("RAM memory % used:", round((used_memory/total_memory) * 100, 2))