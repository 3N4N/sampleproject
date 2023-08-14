pipeline {
    agent any
    stages {
        stage('build') {
            steps {
                sh 'export GIT_BRANCH=master'
                sh 'python -m pip install -U pip setuptools build'
                sh 'python -m build -w'
            }
        }
    }
}