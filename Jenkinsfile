pipeline{
    //directives
    agent any
    tools{
        maven 'maven'

    }

    stages{
        //specifies various stage with in stage

        // Stage 1: Check Git Secrets

        stage("Check-Git-Secrets"){
            steps{
                sh 'rm trufflehog || true'
                sh 'docker run gesellix/trufflehog --json https://github.com/HunterXHunters/webapp.git > trufflehog'
                sh 'cat trufflehog'
            }
        }

        // stage 1: Build
        stage("Build"){
            steps{
                sh 'mvn clean install package'
            }
        }

        // Stage 2 : 
        stage("Test"){
            steps{
                echo 'testing'
            }
        }

    }


}
