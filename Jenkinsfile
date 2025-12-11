pipeline{
    agent any

    environment{
        Imageregistry = 'docker1beginner1shivam'
        EC2_IP= '13.126.112.80'
        DockerComposeFile = 'docker-compose.yaml'
    }
    stages{
        stage("buildImage"){
            steps{
                script{
                    echo "Building Docker Image...."
                    sh "docker build -t ${Imageregistry}/${JOB_NAME}:${BUILD_NUMBER} ."
                }
            }
        }

        stage("pushImage"){
            steps{
                script{
                    echo "Pushing image to DockerHub...."
                    withCredentials([usernamePassword(credentialsId: 'docker-login', passwordVariable: 'PASS', usernameVariable: 'USER')]){
                        sh "echo $PASS | docker login -u $USER --password-stdin"
                        sh "docker push ${Imageregistry}/${JOB_NAME}:${BUILD_NUMBER}"
                    }
                }
            }
        }

        stage("deployCompose"){
            steps{
                script{
                    echo "Deploying with Docker Compose...."
                    sshagent(['ec2']){
                        sh """
                        scp -o StrictHostKeyChecking=no ${DockerComposeFile} ubuntu@{EC2_IP}:/home/ubuntu
                        ssh -o StrictHostKeyChecking=no ubuntu@{EC2_IP} "docker compose -f /home/ubuntu/${DockerComposeFile}"
                        """
                    }
                }
            }
        }
    }
    
}