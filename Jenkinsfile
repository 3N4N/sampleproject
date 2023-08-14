pipeline {
    agent any
    stages {
        stage('build') {
            steps {
                sh 'python3 -m venv env'
                sh 'source env/bin/activate'
                sh 'export GIT_BRANCH=master'
                sh 'python -m pip install -U pip setuptools build'
                sh 'python -m build -w'
            }
        }
    }
}