pipeline {
    agent any

    environment {
        IMAGE_NAME = "viveknshet112/flask_dockerswarm112"
    }

    stages {

        stage('Checkout Code') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/1ms24mc112-vivek/Flask-app-exam.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    dockerImage = docker.build("${IMAGE_NAME}:latest")
                }
            }
        }

        stage('Push Image to Docker Hub') {
            steps {
                script {
                    docker.withRegistry('https://index.docker.io/v1/', 'dockerhub112') {
                        dockerImage.push("latest")
                    }
                }
            }
        }
    }

    post {
        success {
            echo "Flask Docker image built and pushed successfully!"
        }
        failure {
            echo "Pipeline failed!"
        }
        always {
            cleanWs()
        }
    }
}
