from subprocess import call
import sys

if ((len(sys.argv) != 3)):

	cmd="echo 'Por favor, llame al comando de la forma correcta (python padreNuevoServer.py NombreDeNuevoServidor DireccionIPNuevoServidorEnLAN3)'"
	call(cmd, shell=True)
	
	

else:

	nombreServer=str(sys.argv[1])
	IPServer=str(sys.argv[2])

	cmd="python glusterNuevoServer.py "+ nombreServer 
	call(cmd, shell=True)

	cmd="python nuevoServerEnHost.py "+ nombreServer
	call(cmd, shell=True)

	cmd="python lbNuevoServer.py "+ nombreServer +" "+IPServer
	call(cmd, shell=True)