from subprocess import call


cmd="apt update"
call(cmd, shell=True)

cmd="apt -y install mariadb-server"
call(cmd, shell=True)

cmd="sed -i -e 's/bind-address.*/bind-address=0.0.0.0/' -e 's/utf8mb4/utf8/' /etc/mysql/mariadb.conf.d/50-server.cnf"
call(cmd, shell=True)

cmd="systemctl restart mysql"
call(cmd, shell=True)

cmd="mysqladmin -u root password xxxx"
call(cmd, shell=True)

cmd="mysql -u root --password='xxxx' -e \"CREATE USER 'quiz' IDENTIFIED BY 'xxxx';\""
call(cmd, shell=True)

cmd="mysql -u root --password='xxxx' -e \"CREATE DATABASE quiz;\""
call(cmd, shell=True)

cmd="mysql -u root --password='xxxx' -e \"GRANT ALL PRIVILEGES ON quiz.* to 'quiz'@'localhost' IDENTIFIED by 'xxxx';\""
call(cmd, shell=True)

cmd="mysql -u root --password='xxxx' -e \"GRANT ALL PRIVILEGES ON quiz.* to 'quiz'@'%' IDENTIFIED by 'xxxx';\""
call(cmd, shell=True)

cmd="mysql -u root --password='xxxx' -e \"FLUSH PRIVILEGES;\""
call(cmd, shell=True)

