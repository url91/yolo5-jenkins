agent {
    docker {
        image '700935310038.dkr.ecr.eu-north-1.amazonaws.com/url-jenkins_agent:latest'
        args  '--user root -v /var/run/docker.sock:/var/run/docker.sock'
    }

    parameters {
        string(name: 'YOLO5_IMAGE_URL', defaultValue: '', description: '')
    }

    stages {
        stage('Deploy') {
            steps {
                sh 'echo $YOLO5_IMAGE_URL'
            }
        }
    }
}