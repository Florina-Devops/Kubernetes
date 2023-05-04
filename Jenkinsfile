pipeline {
    environment {
        imagename = "florina05/jenkins-docker"
        dockerImage = ''
 }
 agent any
    stages {
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
                    sh “docker run ${imagename}:latest”
 }
 }
 }
 
 }
}