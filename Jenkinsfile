pipeline {
    agent any
    stages {
        stage('build') {
            steps {
                script {
                    docker.image('ubuntu-python:3.10').inside {
                        sh 'git submodule update --init --recursive'
                        sh 'python3 --version'
                        sh 'pip3 --version'
                        sh 'export GIT_BRANCH=master'
                        sh 'python3 -m pip install -U pip setuptools build'
                        sh 'python3 -m build -w'
                    }
                }
            }
        }
    }
}