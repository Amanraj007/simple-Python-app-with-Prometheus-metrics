pipeline {
    agent any

    environment {
        DOCKERHUB_CREDENTIALS = credentials('dockers-creds')  // Jenkins DockerHub creds
        IMAGE_NAME = "aman65f/sample-app"
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/Amanraj007/simple-Python-app-with-Prometheus-metrics.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    echo "Building Docker image..."
                    sh 'docker build -t $IMAGE_NAME:latest ./app'
                }
            }
        }

        stage('Push to DockerHub') {
            steps {
                script {
                    echo "Pushing image to DockerHub..."
                    withDockerRegistry([credentialsId: 'dockers-creds', url: '']) {
                        sh 'docker push $IMAGE_NAME:latest'
                    }
                }
            }
        }

        stage('Deploy with Docker-Compose') {
            steps {
                script {
                    echo "Deploying with docker-compose..."
                    sh 'docker-compose down || true'
                    sh 'docker-compose up -d --build'
                }
            }
        }
    }

    post {
        success {
            echo "✅ Deployment successful!"
        }
        failure {
            echo "❌ Deployment failed!"
        }
    }
}

