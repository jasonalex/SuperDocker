pipeline {
    agent any
    options {
        skipStagesAfterUnstable()
    }
    parameters {
        string(name: 'os', defaultValue: 'alpine', description: 'Choose your Base OS')
        string(name: 'package', defaultValue: 'python', description: 'Choose your Package')
    }

    stages {
        stage('Creating Docker File') {
            steps {
                echo "Creating Docker File"
                sh 'python3 dockerfilegenerator.py -o ${params.os} -p ${params.package}'
            }
        }
        stage('Build Image'){
            steps {
              echo "Building Docker Image"
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
