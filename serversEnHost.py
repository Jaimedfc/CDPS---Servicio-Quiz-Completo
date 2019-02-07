from subprocess import call

###########s1#####################

cmd="sudo lxc-attach --clear-env -n s1 -- bash -c \"apt-get update\""
call(cmd, shell=True)

cmd="sudo lxc-attach --clear-env -n s1 -- bash -c \"curl -sL https://deb.nodesource.com/setup_8.x | bash -\""
call(cmd, shell=True)

cmd="sudo lxc-attach --clear-env -n s1 -- bash -c \"apt-get install -y nodejs\""
call(cmd, shell=True)

cmd="sudo lxc-attach --clear-env -n s1 -- bash -c \"cd /root; git clone https://github.com/CORE-UPM/quiz_2019.git\""
call(cmd, shell=True)

cmd="sudo lxc-attach --clear-env -n s1 -- bash -c \"cd /root/quiz_2019; npm install; npm install forever; npm install mysql2; export QUIZ_OPEN_REGISTER=yes; export DATABASE_URL=mysql://quiz:xxxx@20.2.4.31/quiz; npm run-script migrate_cdps; npm run-script seed_cdps; ./node_modules/forever/bin/forever start ./bin/www\""
call(cmd, shell=True)

cmd="sudo lxc-attach --clear-env -n s1 -- bash -c \"ln -s /mnt/nas /root/quiz_2019/public/uploads\""
call(cmd, shell=True)


###################################s2#######

cmd="sudo lxc-attach --clear-env -n s2 -- bash -c \"apt-get update\""
call(cmd, shell=True)

cmd="sudo lxc-attach --clear-env -n s2 -- bash -c \"curl -sL https://deb.nodesource.com/setup_8.x | bash -\""
call(cmd, shell=True)

cmd="sudo lxc-attach --clear-env -n s2 -- bash -c \"apt-get install -y nodejs\""
call(cmd, shell=True)

cmd="sudo lxc-attach --clear-env -n s2 -- bash -c \"cd /root; git clone https://github.com/CORE-UPM/quiz_2019.git\""
call(cmd, shell=True)

cmd="sudo lxc-attach --clear-env -n s2 -- bash -c \"cd /root/quiz_2019; npm install; npm install forever; npm install mysql2; export QUIZ_OPEN_REGISTER=yes; export DATABASE_URL=mysql://quiz:xxxx@20.2.4.31/quiz; ./node_modules/forever/bin/forever start ./bin/www\""
call(cmd, shell=True)

cmd="sudo lxc-attach --clear-env -n s2 -- bash -c \"ln -s /mnt/nas /root/quiz_2019/public/uploads\""
call(cmd, shell=True)
########################s3#######################

cmd="sudo lxc-attach --clear-env -n s3 -- bash -c \"apt-get update\""
call(cmd, shell=True)

cmd="sudo lxc-attach --clear-env -n s3 -- bash -c \"curl -sL https://deb.nodesource.com/setup_8.x | bash -\""
call(cmd, shell=True)

cmd="sudo lxc-attach --clear-env -n s3 -- bash -c \"apt-get install -y nodejs\""
call(cmd, shell=True)

cmd="sudo lxc-attach --clear-env -n s3 -- bash -c \"cd /root; git clone https://github.com/CORE-UPM/quiz_2019.git\""
call(cmd, shell=True)

cmd="sudo lxc-attach --clear-env -n s3 -- bash -c \"cd /root/quiz_2019; npm install; npm install forever; npm install mysql2; export QUIZ_OPEN_REGISTER=yes; export DATABASE_URL=mysql://quiz:xxxx@20.2.4.31/quiz; ./node_modules/forever/bin/forever start ./bin/www\""
call(cmd, shell=True)

cmd="sudo lxc-attach --clear-env -n s3 -- bash -c \"ln -s /mnt/nas /root/quiz_2019/public/uploads\""
call(cmd, shell=True)


