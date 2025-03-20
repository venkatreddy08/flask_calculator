pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "venkatreddy08/flask_calculator"
    }

    stages {
        stage("Clone Repository") {
            steps {
                git branch: 'main', url: 'https://github.com/venkatreddy08/flask_calculator.git'
            }
        }

        stage("Build Docker Image") {
            steps {
                script {
                    sh "docker build -t $DOCKER_IMAGE ."
                }
            }
        }

        stage("Push to Docker Hub") {
            steps {
                script {
                    withDockerRegistry([credentialsId: 'docker-hub-credentials', url: '']) {
                        sh "docker push $DOCKER_IMAGE"
                    }
                }
            }
        }

        stage("Deploy to Production") {
            steps {
                script {
                    sh "docker stop flask-container || true"
                    sh "docker rm flask-container || true"
                    sh "docker run -d -p 5000:5000 --name flask-container $DOCKER_IMAGE"
                }
            }
        }
    }

    post {
        success {
            echo "🎉 Deployment Successful!"
        }
        failure {
            echo "❌ Deployment Failed!"
        }
    }
}
