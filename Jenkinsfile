pipeline {

agent any


	environment {
		//Define environment variables for Git and DockerHub credentials
		GIT_REPOSITORY_URL = 'https://github.com/ansarishoebs/jenkins_demo.git'
		DOCKER_IMAGE_NAME = 'shoeb8174/docker_jenkins_demo'
		IMAGE_TAG = '1.0' // Make sure to use string for tag

	}



stages {
	stage('Clone Repository') {
		steps {

		 // Checkout the Git repository
		script {
			try {
				git branch: 'main', url: https://github.com/ansarishoebs/jenkins_demo.git

			} catch (Exception e) {

				 echo "Failed to clone repository: ${e.message}"
					error "Failed to clone repository"
			}

		}

		}

	}
}
}
