pipeline {
    agent any

    environment {
        DOCKER_HUB = 'aman65f'
        APP_NAME = 'sample-app'
    }

    stages {
        stage('Checkout') {
            steps {
                git(
                    url: 'https://github.com/Amanraj007/simple-Python-app-with-Prometheus-metrics.git',
                    branch: 'main',
                    credentialsId: 'github-creds'
                )
            }
        }

        stage('Build Docker Image') {
            steps {
                sh "docker build -t $DOCKER_HUB/$APP_NAME:latest ./app"
            }
        }

        stage('Push to Docker Hub') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'dockers-creds', usernameVariable: 'USER', passwordVariable: 'PASS')]) {
                    sh "echo $PASS | docker login -u $USER --password-stdin"
                    sh "docker push $DOCKER_HUB/$APP_NAME:latest"
                }
            }
        }

        stage('Deploy with Docker Compose') {
            steps {
                echo "Deploying stack with docker-compose..."
                sh "docker-compose -f ./docker-compose.yml down || true"
                sh "docker-compose -f ./docker-compose.yml up -d --build"
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
