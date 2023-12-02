pipeline {
    agent any 

    tools {
        maven 'maven-3.9.5'
    }

    stages {
        stage ('Build-Maven') {
            steps {
                sh '''
                    cd ./maven/simple-war/
                    mvn clean package
                    cd ./target/
                    ls
                '''
            }
        }

        stage ('Deploy-Tomcat') {
            steps {
                script {
                    deploy adapters: [tomcat9(credentialsId: 'tomcat-manager', path: '', url: 'http://3.6.89.223:8080/')], 
                                     contextPath: '/itdefined-war-1.0.0', 
                                     war: 'maven/simple-war/target/itdefined-war-1.0.0.war'
                }
            }
        }
    }

}
