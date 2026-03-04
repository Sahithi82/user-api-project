pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps { checkout scm }
        }

        stage('Build Docker Image') {
            steps {
                bat 'docker build -t user-api:1 .'
            }
        }

        stage('Run Container') {
            steps {
                bat 'docker rm -f user-api || exit 0'
                bat 'docker run -d --name user-api -p 5000:5000 user-api:1'
            }
        }
    }

    post {
        success { echo 'Deployed successfully ✅' }
        failure { echo 'Pipeline failed ❌' }
    }
}