pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                sh '''
                aws ecr get-login-password --region eu-north-1 | docker login --username AWS --password-stdin 700935310038.dkr.ecr.eu-north-1.amazonaws.com
                docker build -t url-yolo5 .
                docker tag url-yolo5:latest 700935310038.dkr.ecr.eu-north-1.amazonaws.com/url-yolo5:latest
                docker push 700935310038.dkr.ecr.eu-north-1.amazonaws.com/url-yolo5:latest
                '''
            }
        }
    }
}