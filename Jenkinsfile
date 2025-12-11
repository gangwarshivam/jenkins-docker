pipeline {
    agent any

    environment {
        Imageregistry = 'docker1beginner1shivam'
        EC2_IP = '3.7.71.179'
        DockerComposeFile = 'docker-compose.yaml'
        PROJECT_NAME = 'multi-service-app'
        DOCKER_IMAGE_TAG = "${Imageregistry}/${PROJECT_NAME}:${BUILD_NUMBER}"
    }

    stages {

        stage("transferSource") {
            steps {
                script {
                    echo "Transferring project files to EC2"
                    sshagent(['ec2']) {
                        sh """
                        tar czf project.tar.gz *
                        scp -o StrictHostKeyChecking=no project.tar.gz ubuntu@${EC2_IP}:/home/ubuntu
                        ssh -o StrictHostKeyChecking=no ubuntu@${EC2_IP} "tar xzf project.tar.gz"
                        """
                    }
                }
            }
        }

        stage("buildOnEC2") {
            steps {
                script {
                    echo "Building Docker images on EC2..."
                    sshagent(['ec2']) {
                        sh """
                        ssh -o StrictHostKeyChecking=no ubuntu@${EC2_IP} "
                            cd /home/ubuntu &&
                            docker-compose build &&
                            docker tag ${PROJECT_NAME}_backend ${DOCKER_IMAGE_TAG}-backend &&
                            docker tag ${PROJECT_NAME}_frontend ${DOCKER_IMAGE_TAG}-frontend
                        "
                        """
                    }
                }
            }
        }

        stage("pushImage") {
            steps {
                script {
                    echo "Pushing images from EC2"
                    sshagent(['ec2']) {
                        withCredentials([usernamePassword(credentialsId: 'docker-login', passwordVariable: 'PASS', usernameVariable: 'USER')]) {
                            sh """
                            ssh -o StrictHostKeyChecking=no ubuntu@${EC2_IP} "
                                echo $PASS | docker login -u $USER --password-stdin &&
                                docker push ${DOCKER_IMAGE_TAG}-backend &&
                                docker push ${DOCKER_IMAGE_TAG}-frontend
                            "
                            """
                        }
                    }
                }
            }
        }

        stage("deployCompose") {
            steps {
                script {
                    echo "Deploying with Docker Compose on EC2..."
                    sshagent(['ec2']) {
                        sh """
                        scp -o StrictHostKeyChecking=no ${DockerComposeFile} ubuntu@${EC2_IP}:/home/ubuntu
                        ssh -o StrictHostKeyChecking=no ubuntu@${EC2_IP} "docker-compose -f /home/ubuntu/${DockerComposeFile} up -d"
                        """
                    }
                }
            }
        }
    }
}

