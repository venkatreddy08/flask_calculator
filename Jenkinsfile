pipeline{
    agent any

    environment{
        DOCKER_IMAGE = "venkatreddy08/flask_calculator"
    }

    stages{
        stage("Clone Repository"){
            steps{
                url : "https://github.com/venkatreddy08/flask_calculator.git" , branch : "main"
            }
            
        }

        stage("Build Docker Image"){
            steps{
                script {
                  sh "docker build -t $DOCKER_IMAGE ."
                }
            }
        }

        stage("push to docker hub"){
            steps{
                script{
                   withDockerRegistry([credentialsId: 'docker-hub-credentials', url: '']) {
                        sh 'docker push $DOCKER_IMAGE'
                    }
                }
            }
        }
        stage("Deploy to Prod"){
            steps{
                script{

                     sh 'docker stop flask-container || true'
                     sh 'docker rm flask-container || true'
                     sh 'docker run -d -p 5000:5000 --name flask-container $DOCKER_IMAGE'
                }
            }
                post {
        success {
            echo '🎉 Deployment Successful!'
        }
        failure {
            echo '❌ Deployment Failed!'
        }
    }

        }
    }
    
}