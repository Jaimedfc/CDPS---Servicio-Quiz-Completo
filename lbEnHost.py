from subprocess import call



cmd="sudo lxc-attach --clear-env -n lb -- bash -c \"apt-get update\""
call(cmd, shell=True)

cmd="sudo lxc-attach --clear-env -n lb -- bash -c \"apt-get install -y haproxy\""
call(cmd, shell=True)

cmd="sudo lxc-attach --clear-env -n lb -- bash -c \"echo 'frontend lb' >> /etc/haproxy/haproxy.cfg\""
call(cmd, shell=True)

cmd="sudo lxc-attach --clear-env -n lb -- bash -c \"echo '	bind *:80' >> /etc/haproxy/haproxy.cfg\""
call(cmd, shell=True)

cmd="sudo lxc-attach --clear-env -n lb -- bash -c \"echo '	mode http' >> /etc/haproxy/haproxy.cfg\""
call(cmd, shell=True)

cmd="sudo lxc-attach --clear-env -n lb -- bash -c \"echo '	default_backend webservers' >> /etc/haproxy/haproxy.cfg\""
call(cmd, shell=True)

cmd="sudo lxc-attach --clear-env -n lb -- bash -c \"echo 'backend webservers' >> /etc/haproxy/haproxy.cfg\""
call(cmd, shell=True)

cmd="sudo lxc-attach --clear-env -n lb -- bash -c \"echo '	mode http' >> /etc/haproxy/haproxy.cfg\""
call(cmd, shell=True)

cmd="sudo lxc-attach --clear-env -n lb -- bash -c \"echo '	balance leastconn' >> /etc/haproxy/haproxy.cfg\""
call(cmd, shell=True)

cmd="sudo lxc-attach --clear-env -n lb -- bash -c \"echo '	server s1 20.2.3.11:3000 check' >> /etc/haproxy/haproxy.cfg\""
call(cmd, shell=True)

cmd="sudo lxc-attach --clear-env -n lb -- bash -c \"echo '	server s2 20.2.3.12:3000 check' >> /etc/haproxy/haproxy.cfg\""
call(cmd, shell=True)

cmd="sudo lxc-attach --clear-env -n lb -- bash -c \"echo '	server s3 20.2.3.13:3000 check' >> /etc/haproxy/haproxy.cfg\""
call(cmd, shell=True)

cmd="sudo lxc-attach --clear-env -n lb -- bash -c \"sudo service haproxy restart\""
call(cmd, shell=True)

