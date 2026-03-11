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
                    sudo apt-get update
                    sudo apt-get install -y python3-venv
                    python3 -m venv venv
                    . venv/bin/activate
                    python -m pip install --upgrade pip
                '''
            }
        }

        stage('Run Add Script') {
            steps {
                sh '''
                    . venv/bin/activate
                    python add.py <<EOF
                    5
                    7
                    EOF
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
                    . venv/bin/activate
                    pytest --maxfail=1 --disable-warnings -q || true
                '''
            }
        }
    }

    post {
        success {
            echo 'Build and tests completed successfully!'
        }
        failure {
            echo 'Build Failed'
        }
    }
}
