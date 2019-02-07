from subprocess import call
import sys

if ((len(sys.argv) != 2)):

	cmd="echo 'Por favor, llame al comando de la forma correcta (python glusterNuevoServer.py NombreDeNuevoServidor)'"
	call(cmd, shell=True)


else:
	
	nombreServer=str(sys.argv[1])
	cmd="sudo lxc-attach --clear-env -n "+nombreServer+" -- bash -c \"mkdir /mnt/nas\""
	call(cmd, shell=True)

	cmd="sudo lxc-attach --clear-env -n "+nombreServer+" -- bash -c \"mount -t glusterfs 20.2.4.21:/nas /mnt/nas\""
	call(cmd, shell=True)