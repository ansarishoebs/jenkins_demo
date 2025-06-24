pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'shoeb8174/jenkins-demo1'
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
                    sh "echo 8174 | sudo -S docker build -t $DOCKER_IMAGE:latest ."
                }
            }
        }

        stage('Push to Docker Hub') {
            steps {
                script {
                    withCredentials([usernamePassword(credentialsId: 'my-docker-hub-credentials-id',usernameVariable: 'Username',passwordVariable: "Password")]){
                        sh "echo $Password | docker login -u $Username --password-stdin"
                        sh "echo 8174 | sudo -S docker push ${DOCKER_IMAGE}:latest"
                    }
                }
            }
        }
        stage('run the image'){
            steps{
                script{
                    sh "docker run -dit shoeb8174/jenkins-demo"
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
