from subprocess import call

cmd="scp fw.fw root@fw:"
call(cmd, shell=True)

cmd="sudo lxc-attach --clear-env -n fw -- bash -c \"./root/fw.fw\""
call(cmd, shell=True)


