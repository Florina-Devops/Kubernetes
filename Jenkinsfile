pipeline {
    environment {
        imagename = "florina05/jenkins-docker"
        dockerImage = ''
 }
 agent any
    stages {
        stage('Cloning Git') {
            steps {
                git([url: 'https://github.com/adithyak21/simple-docker.git', branch: 'main'])
 }
 }
        stage('Building image') {
            steps{
                script {
                    dockerImage = docker.build imagename
 }
 }
 }
        stage('Running image') {
            steps{
                script {
                    sh "docker run ${imagename}:latest"
 }
 }
 }
 
 }
}