#!/bin/bash

# This will install Java and Jenkins only in Ubuntu 
# To install directly in any ubuntu ec2, run below command 
#   curl -s https://raw.githubusercontent.com/jaintpharsha/Devops-ITD-Aug-2023/main/Jenkins/install.sh | bash 

usage() {
echo "
Usage: $0 
This will install Java and Jenkins only in Ubuntu 
Mandatory arguments to long options are mandatory for short options too.
  -h, --help                  Display usage of the script.
"
}

[[ "$1" == '-h' ]] && usage 
[[ "$1" == '--help' ]] && usage 

echo -e "\n---------------------------- STEP_1 Update apt ----------------------------\n"
	sleep 4
	sudo apt update 

echo -e "\n---------------------------- STEP_2: Install Java .... ----------------------------\n"
	sleep 4
	sudo apt install -y fontconfig openjdk-17-jre 

echo -e "\n---------------------------- STEP_3 Add Jenkins to apt list ----------------------------\n" 
	sleep 4
	sudo wget -O /usr/share/keyrings/jenkins-keyring.asc https://pkg.jenkins.io/debian/jenkins.io-2023.key
	echo deb [signed-by=/usr/share/keyrings/jenkins-keyring.asc] https://pkg.jenkins.io/debian binary/ | sudo tee /etc/apt/sources.list.d/jenkins.list > /dev/null
	sudo apt update

echo -e "\n---------------------------- STEP_4 Install Jenkins ----------------------------\n"
	sleep 4
 	sudo apt install -y jenkins 

echo -e "\n ---------------------------- STEP_5 Check Jenkins service status ----------------------------\n"
	sudo systemctl status jenkins 

echo -e "\n ---------------------------- STEP_6: Open default port of Jenkins 8080 & secondary port 50000 in ec2 SG ----------------------------"

echo -e "\n---------------------------- STEP_7 Get Initial Admin Password ----------------------------"
	sudo cat /var/lib/jenkins/secrets/initialAdminPassword

