#!/bin/bash
sudo apt update -y
sudo apt upgrade -y
sudo apt install mysql-server -y
mysqladmin -u root password 'Iamr00t$'
mysql -u root -pIamr00t$ -e "CREATE USER 'reader'@'%' IDENTIFIED BY 'Iamr00t$'; GRANT ALL PRIVILEGES ON *.* TO 'reader'@'%' WITH GRANT OPTION;"
mysql -u reader -pIamr00t$ -e "CREATE DATABASE ContainerDemo DEFAULT CHARACTER SET utf8 COLLATE utf8_unicode_ci;"
mysql -u reader -pIamr00t$ < ContainerDemo.sql
