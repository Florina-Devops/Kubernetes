pipeline {
  environment {
    imagename = "florina-flaskapp"
    dockerImage = ''
  }
  agent any
  stages {
    stage('Cloning Git') {
      steps {
        git([url: 'https://github.com/Florina-Devops/Kubernetes.git', branch: 'main'])
 
      }
    }
    stage('Building image') {
      steps{
        script {
          dockerImage = docker.build imagename
        }
      }
    }
    stage('Running Image') {
      steps{
        script {
          sh "docker run ${imagename}:latest"
          }
        }
      }
    }
    
}
