from subprocess import call
import sys

if ((len(sys.argv) != 3)):

	cmd="echo 'Por favor, llame al comando de la forma correcta (python lbNuevoServer.py NombreDeNuevoServidor DireccionIPNuevoServidorEnLAN3)'"
	call(cmd, shell=True)
	
	

else:

	nombreServer=str(sys.argv[1])
	IPServer=str(sys.argv[2])
	cmd="sudo lxc-attach --clear-env -n lb -- bash -c \"echo '	server " + nombreServer +" " + IPServer+":3000 check' >> /etc/haproxy/haproxy.cfg\""
	call(cmd, shell=True)

	cmd="sudo lxc-attach --clear-env -n lb -- bash -c \"sudo service haproxy restart\""
	call(cmd, shell=True)