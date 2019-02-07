from subprocess import call


cmd="sudo lxc-attach --clear-env -n nas1 -- bash -c \"gluster peer probe 20.2.4.22\""
call(cmd, shell=True)

cmd="sudo lxc-attach --clear-env -n nas1 -- bash -c \"gluster peer probe 20.2.4.23\""
call(cmd, shell=True)

cmd="sudo lxc-attach --clear-env -n nas1 -- bash -c \"gluster volume create nas replica 3 nas1:/nas nas2:/nas nas3:/nas force\""
call(cmd, shell=True)

cmd="sudo lxc-attach --clear-env -n nas1 -- bash -c \"gluster volume start nas\""
call(cmd, shell=True)

cmd="sudo lxc-attach --clear-env -n nas1 -- bash -c \"gluster volume set nas network.ping-timeout 5\""
call(cmd, shell=True)

cmd="sudo lxc-attach --clear-env -n s1 -- bash -c \"mkdir /mnt/nas\""
call(cmd, shell=True)

cmd="sudo lxc-attach --clear-env -n s1 -- bash -c \"mount -t glusterfs 20.2.4.21:/nas /mnt/nas\""
call(cmd, shell=True)

cmd="sudo lxc-attach --clear-env -n s2 -- bash -c \"mkdir /mnt/nas\""
call(cmd, shell=True)

cmd="sudo lxc-attach --clear-env -n s2 -- bash -c \"mount -t glusterfs 20.2.4.21:/nas /mnt/nas\""
call(cmd, shell=True)

cmd="sudo lxc-attach --clear-env -n s3 -- bash -c \"mkdir /mnt/nas\""
call(cmd, shell=True)

cmd="sudo lxc-attach --clear-env -n s3 -- bash -c \"mount -t glusterfs 20.2.4.21:/nas /mnt/nas\""
call(cmd, shell=True)

