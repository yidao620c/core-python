#!/bin/bash

# install winstore on winserver

cd install_ansible/
yum localinstall -yC --disablerepo=* *.rpm

cd ..

if [[ "$1" == "db" ]]; then
    ansible-playbook -i hosts --extra-vars "winserver=1 db_install=1" site.yml
else
    ansible-playbook -i hosts --extra-vars "winserver=1" site.yml
fi

