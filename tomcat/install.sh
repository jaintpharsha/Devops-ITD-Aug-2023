#!/bin/bash

if java --version; then 
	:
else 
	echo "Java not found, Install java first"
	sudo apt update -y 
	sudo apt install default-jdk -y
fi

echo "STEP1: Downloading 10.0.8 version of Apache Tomcat."
	wget https://archive.apache.org/dist/tomcat/tomcat-10/v10.0.8/bin/apache-tomcat-10.0.8.tar.gz
	
	echo "		STEP1_a: Extract the downloaded archive."
		sudo tar xzvf apache-tomcat-10.0.8.tar.gz
	echo "		STEP1_b: Create an installation directory /opt/tomcat/"
		sudo mkdir /opt/tomcat/
	echo "		STEP1_c: Move the extracted files to the installation directory."
		sudo mv apache-tomcat-10.0.8/* /opt/tomcat/
	echo "		STEP1_d: Change ownership of the installation directory."
		sudo chown -R www-data:www-data /opt/tomcat/
	echo "		STEP1_e: Change access permissions for the installation directory."
		sudo chmod -R 755 /opt/tomcat/

echo "		STEP1_f: Create a systemd unit file for Apache Tomcat to run it as a system.service."
	echo '[Unit]
Description=Tomcat
After=network.target

[Service]
Type=forking
User=root
Group=root
Environment="JAVA_HOME=/usr/lib/jvm/java-1.11.0-openjdk-amd64"
Environment="JAVA_OPTS=-Djava.security.egd=file:///dev/urandom"
Environment="CATALINA_BASE=/opt/tomcat"
Environment="CATALINA_HOME=/opt/tomcat"
Environment="CATALINA_PID=/opt/tomcat/temp/tomcat.pid"
Environment="CATALINA_OPTS=-Xms512M -Xmx1024M -server -XX:+UseParallelGC"
ExecStart=/opt/tomcat/bin/startup.sh
ExecStop=/opt/tomcat/bin/shutdown.sh

[Install]
WantedBy=multi-user.target	
' > /etc/systemd/system/tomcat.service

echo "STEP2: Configure administrator and manager user account for Apache Tomcat."
	echo ' Edit the tomcat-users.xml file and add below users config lines
		sudo vi /opt/tomcat/conf/tomcat-users.xml
	'
	echo '
		<role rolename="manager-gui" />
		<user username="manager" password="StrongPassword" roles="manager-gui,manager-script" />

		<role rolename="admin-gui" />
		<user username="admin" password="StrongPassword" roles="manager-gui,admin-gui" />
	'

echo "STEP3: Enable remote access to Apache Tomcat by editing manager and host-manager configuration files."
	echo '
		1. sudo vi /opt/tomcat/webapps/manager/META-INF/context.xml
		 	Note: Comment out the IP addresses section as shown below.

		<!-- <Valve className="org.apache.catalina.valves.RemoteAddrValve"
         allow="127\.\d+\.\d+\.\d+|::1|0:0:0:0:0:0:0:1" /> -->

        2. sudo vi /opt/tomcat/webapps/host-manager/META-INF/context.xml
        	Note: sudo vi /opt/tomcat/webapps/host-manager/META-INF/context.xml

        <!--<Valve className="org.apache.catalina.valves.RemoteAddrValve"
         allow="127\.\d+\.\d+\.\d+|::1|0:0:0:0:0:0:0:1" /> -->	
	'



echo "STEP4: Reload the systemd daemon, Start Apache Tomcat service and Enable the service to start up on system boot."
echo '
sudo systemctl daemon-reload
sudo systemctl enable tomcat
sudo systemctl start tomcat
sudo systemctl status tomcat
'



