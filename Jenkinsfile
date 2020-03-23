pipeline {
    agent any
    options {
        skipStagesAfterUnstable()
    }
    parameters {
        choice(name: 'os', choices: ['alpine', 'debian'], description: 'Choose Base OS')
        choice(name: 'package', choices: ['python', 'node'], description: 'Choose Package')
    }

    stages {
        stage('Creating Docker File') {
            steps {
                echo "Creating Docker File"
                sh 'python dockerfilegenerator.py -o $os -p $package'
            }
        }
        stage('Build Image'){
            steps {
              echo "Building Docker Image"
              sh 'cd build'
              sh 'ls'
              sh 'docker build -t $package-$os:latest .'
            }
        }
        stage('Deploy to ECR') {
            when {
              expression {
                currentBuild.result == null || currentBuild.result == 'SUCCESS'
              }
            }
            steps {
                echo "Deploying Image to ECR"
            }
        }
    }
}
