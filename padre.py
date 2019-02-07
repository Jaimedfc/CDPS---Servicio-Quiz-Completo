from subprocess import call

cmd="python fwEnHost.py"
call(cmd, shell=True)

cmd="python bbddEnHost.py"
call(cmd, shell=True)

cmd="python glusterEnHost.py"
call(cmd, shell=True)

cmd="python serversEnHost.py"
call(cmd, shell=True)

cmd="python lbEnHost.py"
call(cmd, shell=True)