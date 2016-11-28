#!/usr/bin/env python
# 脚本来安装virtualenv

echo "====================create install dirs"
mkdir -p /root/{setuptools,pip,virtualenv}

echo "====================install setuptools"
tar -zxvf /root/install_venv/setuptools-28.8.0.tar.gz -C /root/setuptools --strip-components=1
cd /root/setuptools
python setup.py install

echo "====================install pip"
tar -zxvf /root/install_venv/pip-8.1.2.tar.gz -C /root/pip --strip-components=1
cd /root/pip
python setup.py install

echo "====================install virtualenv"
tar -zxvf /root/install_venv/virtualenv-15.0.3.tar.gz -C /root/virtualenv --strip-components=1
cd /root/virtualenv
python setup.py install

echo "====================init winstore venv"
virtualenv --no-site-packages --no-download /opt/winstore/venv
