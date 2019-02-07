from subprocess import call
import sys
########################NuevoServer##########################


if ((len(sys.argv) != 2)):

	cmd="echo 'Por favor, llame al comando de la forma correcta (python nuevoServerEnHost.py NombreDeNuevoServidor)'"
	call(cmd, shell=True)


else:

	nombreServer=str(sys.argv[1])
	cmd="sudo lxc-attach --clear-env -n "+nombreServer+" -- bash -c \"apt-get update\""
	call(cmd, shell=True)

	cmd="sudo lxc-attach --clear-env -n "+nombreServer+" -- bash -c \"curl -sL https://deb.nodesource.com/setup_8.x | bash -\""
	call(cmd, shell=True)

	cmd="sudo lxc-attach --clear-env -n "+nombreServer+" -- bash -c \"apt-get install -y nodejs\""
	call(cmd, shell=True)

	cmd="sudo lxc-attach --clear-env -n "+nombreServer+" -- bash -c \"cd /root; git clone https://github.com/CORE-UPM/quiz_2019.git\""
	call(cmd, shell=True)

	cmd="sudo lxc-attach --clear-env -n "+nombreServer+" -- bash -c \"cd /root/quiz_2019; npm install; npm install forever; npm install mysql2; export QUIZ_OPEN_REGISTER=yes; export DATABASE_URL=mysql://quiz:xxxx@20.2.4.31/quiz; ./node_modules/forever/bin/forever start ./bin/www\""
	call(cmd, shell=True)

	cmd="sudo lxc-attach --clear-env -n "+nombreServer+" -- bash -c \"ln -s /mnt/nas /root/quiz_2019/public/uploads\""
	call(cmd, shell=True)

