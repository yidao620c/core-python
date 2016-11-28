#!/bin/bash

# install winstore on centos7

cd install_ansible/
yum localinstall -yC --disablerepo=* *.rpm

cd ..

if [[ "$1" == "db" ]]; then
    ansible-playbook -i hosts --extra-vars "db_install=1" site.yml
else
    ansible-playbook -i hosts site.yml
fi

