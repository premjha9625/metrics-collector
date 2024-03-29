import paramiko
import time
import psutil
import os

p = paramiko.SSHClient()
cred = open("hostnames.csv","r")
cmd_list = ['timeout 1 top','df -Th', 'free -h']
#cmd_list = [psutil.cpu_percent(4),psutil.virtual_memory()[2], psutil.virtual_memory()[3]/1000000000]
prompts = ['The CPU usage is: ','RAM memory percent used:', 'RAM Used (GB):']
for i in cred.readlines():
        line=i.strip()
        ls =line.split(",")
        print(ls[0])
        # print(ls[1])
        # print(ls[2])
        p.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        p.connect("%s"%ls[0],port =22, username = "%s"%ls[1], password="%s"%ls[2])
        print(ls[1])
        for j in cmd_list:
                #for k in prompts:
                        stdin, stdout, stderr = p.exec_command(f"python -c '{total_memory, used_memory, free_memory = map(int, os.popen('free -t -m').readlines()[-1].split()[1:]); print("RAM memory % used:", round((used_memory/total_memory) * 100, 2))}'", get_pty=True)
                        #stdin, stdout, stderr = p.exec_command('df -Th' , get_pty=True)
                        #stdin.write("%s\n"%ls[2])
                        #time.sleep(3)
                        stdin.flush()
                        opt = stdout.readlines()
                        #output = stdout.read().decode().strip()
                        opt ="".join(opt)
                        #opt ="".join(output)
                        print(opt)
        # try:
        #                 p.connect("%s"%ls[0],port =22, username = "%s"%ls[1], password="%s"%ls[2])
        #                 for command, prompt in zip(cmd_list, prompts):
        #                         stdin, stdout, stderr = p.exec_command(f"python -c '{total_memory, used_memory, free_memory = map(int, os.popen('free -t -m').readlines()[-1].split()[1:]); print("RAM memory % used:", round((used_memory/total_memory) * 100, 2))}'", get_pty=True)
        #                         #stdin.write("%s\n"%ls[2])
        #                         #time.sleep(3)
        #                         stdin.flush()
        #                         #opt = stdout.readlines()
        #                         output = stdout.readlines()
        #                         #opt ="".join(opt)
        #                         opt ="".join(output)
        #                         print(opt)
        #                         print(prompt, output)
        # finally:
        #                 p.close()
cred.close()
