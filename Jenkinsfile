pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                sh 'docker compose -f compose.yaml -f compose.ci.yaml build web'
            }
        }
    }
}
