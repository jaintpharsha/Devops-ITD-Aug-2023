pipeline {
   agent any 

   tools {
      maven 'maven-3.9.5'
   }

   stages {
      stage('BUILD') {
         steps {
               sh ''' 
                  cd maven/calculator_app
                  mvn clean package -Dmaven.test.skip=true
               '''
         }
      }

      stage('UNIT TEST') {
         steps {
            dir("maven/calculator_app") {
               sh 'mvn clean test'
            }
         }
      }

      stage('Integration TEST') {
         steps {
            dir("maven/calculator_app") {
               sh 'sudo mvn clean integration-test'
            }
         }
      }

      // stage('Deploy Tomcat Using maven plugin') {
      //    steps {
      //       dir("maven/calculator_app") {
      //          sh 'sudo mvn tomcat7:deploy'
      //       }
      //    }
      // }

      stage ('Deploy Tomcat Using jenkins plugin') {
         steps {
                script {
                    deploy adapters: [tomcat9(credentialsId: 'tomcat-manager', path: '', url: 'http://3.6.89.223:8080/')], 
                                     contextPath: '/calculator', 
                                     war: 'maven/calculator_app/target/calculator.war'
                }
         }
      }
   }
}