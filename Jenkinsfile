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
          sh "docker build -t ${imagename}:latest ."
        }
      }
    }
    stage('Running Image') {
      steps{
        script {
          sh "docker run -d -p 5000:1234 --name jenkinstest-container ${imagename}:latest"
          }
        }
      }
    
}
}
