#!/bin/bash
echo "Initial update"
    sudo apt update -y
    
echo "STEP1: Install JDK-11"
    sudo apt install openjdk-11-jdk -y

echo "STEP2: Add the apt key to add jenkins package to apt list"
    curl -fsSL https://pkg.jenkins.io/debian-stable/jenkins.io-2023.key | sudo tee /usr/share/keyrings/jenkins-keyring.asc > /dev/null

echo "STEP3: Add jenkins package to apt "
    echo deb [signed-by=/usr/share/keyrings/jenkins-keyring.asc] https://pkg.jenkins.io/debian-stable binary/ | sudo tee /etc/apt/sources.list.d/jenkins.list > /dev/null 

echo "STEP4: Update apt again"
    sudo apt update -y 



echo "STEP5: Final install the Jenkins"
    sudo apt-get install jenkins -y



