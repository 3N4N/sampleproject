pipeline {
    agent any
    stages {
        stage('build') {
            steps {
                sh 'python3 --version'
                sh 'export GIT_BRANCH=master'
                sh 'python3 -m pip install -U pip setuptools build'
                sh 'python3 -m build -w'
                sh 'pip list'
            }
        }
    }
}