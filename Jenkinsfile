pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'shoeb8174/jenkins-demo'
        DOCKER_CREDENTIALS_ID = 'my-docker-hub-credentials-id'  // Replace with your Jenkins credentials ID
    }

    stages {
        stage('Clone Repository') {
            steps {
                git url: 'https://github.com/ansarishoebs/jenkins_demo.git', branch: 'main'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    sh "sudo su"
                    sh "docker build -t $DOCKER_IMAGE:latest ."
                }
            }
        }

        stage('Push to Docker Hub') {
            steps {
                script {
                    docker.withRegistry('https://index.docker.io/v1/', "${DOCKER_CREDENTIALS_ID}") {
                        dockerImage.push('latest')
                    }
                }
            }
        }
    }

    post {
        success {
            echo 'Image built and pushed successfully!'
        }
        failure {
            echo 'Build or push failed.'
        }
    }
}
