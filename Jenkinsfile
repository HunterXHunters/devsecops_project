pipeline{
    //directives
    agent any
    tools{
        maven 'maven'

    }

    stages{
        //specifies various stage with in stage

        // Stage 1: Check Git Secrets



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
