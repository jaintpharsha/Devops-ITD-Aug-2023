pipeline {
	agent { label 'slave2' }
  
  triggers {
        pollSCM '* * * * *'
  }

  tools {
    maven 'maven-3.9.2' 
  }
  stages {
    stage ('Build') {
      steps {
        sh '''
        	cd ./maven/simple-war 
          cat ./src/main/webapp/index.jsp
        	mvn clean package
        	cd ./target/
        	ls
           '''
      }
    }
    stage ('Deploy') {
      steps {
        script {
          // url: ‘http://<ip_address>:8080/’ –> Your tomcat url
          // contextPath: ‘/pipeline’         –> Context path to deploy in Tomcat
          // onFailure: false                 –> Flag used to control the deployment, 
          //                                     If pipeline Job fails, below deploy block will not run.
          // war: ‘target/*.war’ –> Your war file name
          deploy adapters: [tomcat9(credentialsId: 'tomcat_manager', path: '', url: 'http://65.2.40.144:8080/')], 
                           contextPath: '/itdefined-war-1.0.0', 
                           onFailure: false, 
                           war: 'maven/simple-war/target/*.war' 
        }
      }
    }
  }

  // post { 
  //     always { 
  //         cleanWs()
  //     }
  // }

}