pipeline {
    agent any

    stages {

        stage('Clone Repository') {
            steps {
                git branch: 'main',
                url: 'https://github.com/Jainandan-728/python.git'
            }
        }

        stage('Setup Python Environment') {
            steps {
                sh '''
                python3 -m venv venv
                ./venv/bin/pip install --upgrade pip
                '''
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''
                ./venv/bin/pip install -r requirements.txt
                '''
            }
        }

        stage('Run add Script') {
            steps {
                sh '''
                ./venv/bin/python add.py
                '''
            }
        }

       

    }

    post {
        success {
            echo 'Build and Tests Passed Successfully'
        }
        failure {
            echo 'Build Failed'
        }
    }
}
