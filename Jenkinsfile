pipeline {
    agent any
    options {
        skipStagesAfterUnstable()
    }
    parameters {
        choice(name: 'os', choices: ['alpine', 'debian'], description: 'Choose Base OS')
        choice(name: 'package', choices: ['python', 'node'], description: 'Choose Package')
        string(name: 'aws_account', defaultValue: '787916049928', description: ' Destination AWS Account')
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
              sh 'docker build -f build/Dockerfile -t $package-$os:latest .'
            }
        }
        stage('Create ECR Repo') {
            when {
              expression {
                currentBuild.result == null || currentBuild.result == 'SUCCESS'
              }
            }
            steps {
                echo "Create ECR Repo"
                sh 'python3 ChooseEcr.py -o $os -p $package -c $aws_account'
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
                sh 'python3 DockerImagePush.py -o $os -p $package -c $aws_account'
            }
        }
    }
}
