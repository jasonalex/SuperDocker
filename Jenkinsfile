pipeline {
    agent any
    options {
        skipStagesAfterUnstable()
    }
    stages {
        stage('Creating Docker File') {
            steps {
                echo "Creating Docker File"
            }
        }
        stage('Build Image'){
            steps {
              echo "Building Docker Image"
            }
        }
        stage('Deploy to ECR'){
        when {
          expression {
            currentBuild.result == null || currentBuild.result == 'SUCCESS'
          }
        }
        steps {
            echo 'Deploying to ECR'
            python -v
        }
    }
}
