from subprocess import call

cmd="scp bbdd.py root@bbdd:"
call(cmd, shell=True)

cmd="sudo lxc-attach --clear-env -n bbdd -- bash -c \"python /root/bbdd.py\""
call(cmd, shell=True)

