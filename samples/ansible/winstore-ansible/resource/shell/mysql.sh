#!/usr/bin/env python
# 脚本来安装配置mysql
# mysql.sh mysql_password


echo "====================change root password===================="
mysqladmin -u root password $1 2>/dev/null

echo "====================grant privilege to remote================="
hostnm=$(hostname)
mysql -uroot -p$1 -e "grant all privileges on *.* to root@'%' identified by '$1'; flush privileges;" 2>/dev/null
mysql -uroot -p$1 -e "grant all privileges on *.* to root@'$hostnm' identified by '$1'; flush privileges;" 2>/dev/null
mysql -uroot -p$1 -e "CREATE DATABASE IF NOT EXISTS winstore default charset utf8 COLLATE utf8_general_ci;" 2>/dev/null

echo "====================mysql encoding utf8======================="
charset=$(cat /etc/my.cnf | grep 'default-character-set')
if [[ "$charset" == "" ]]; then
    cat <<EOF >>/etc/my.cnf
    [mysql]
    default-character-set = utf8
EOF
fi

echo "====================disable selinux========================="
if [[ -f /etc/selinux/config ]]; then
    sed -i 's/SELINUX=enforcing/SELINUX=disabled/g' /etc/selinux/config
fi

echo "====================open 3306 port==========================="
firewall-cmd --zone=public --add-service=mysql --permanent 2>/dev/null
systemctl restart firewalld 2>/dev/null

