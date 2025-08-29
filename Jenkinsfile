pipeline {
    agent any

    environment {
        DOCKERHUB_CREDENTIALS = credentials('dockers-creds')  // DockerHub credentials
        IMAGE_NAME = "aman65f/sample-app"
    }

    stages {
        stage('Checkout') {
            steps {
                echo "Cloning repository..."
                git branch: 'main', url: 'https://github.com/Amanraj007/simple-Python-app-with-Prometheus-metrics.git', credentialsId: 'github-creds'
            }
        }

        stage('Build Docker Image') {
            steps {
                echo "Building Docker image..."
                sh 'docker build -t $IMAGE_NAME:latest ./app'
            }
        }

        stage('Push to DockerHub') {
            steps {
                echo "Pushing Docker image to Docker Hub..."
                withDockerRegistry([credentialsId: 'dockers-creds', url: '']) {
                    sh 'docker push $IMAGE_NAME:latest'
                }
            }
        }

        stage('Deploy with Docker Compose') {
            steps {
                echo "Deploying stack with docker-compose..."
                // Stop old containers, ignore errors if none running
                sh 'docker-compose down || true'
                // Start stack in detached mode
                sh 'docker-compose up -d --build'
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
