pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                sh 'docker compose -f compose.yaml -f compose.ci.yaml build web'
            }
        }

        stage('Tests') {
            steps {
                withCredentials([file(credentialsId: 'helpdesk-ci-env', variable: 'ENV_FILE')]) {
                    sh '''
                        cp "$ENV_FILE" .env.ci
                        docker compose -f compose.yaml -f compose.ci.yaml run --rm web pytest
                        rm -f .env.ci
                    '''
                }
            }
        }
    }
}
