pipeline {
    agent { label 'master' }
    environment {
        BRANCH_NAME="${env.BRANCH_NAME}"
    }

    stages {
        stage('BRANCH_NAME') {
            steps{
                sh 'echo BRANCH_NAME = ${BRANCH_NAME}'
            }
        }
        stage('build') {
            
            
            steps{
                    sh '''CONTAINER_NAME=counter-${BRANCH_NAME}
                          IMAGE_NAME=counter-${BRANCH_NAME}-img
                          if [ "$(docker ps -q --no-trunc -f name=^/$CONTAINER_NAME$)" ];then
                            docker stop ${CONTAINER_NAME}
                          fi
                          if [ "$(docker ps -a -q --no-trunc -f name=^/$CONTAINER_NAME$)" ];then
                            docker rm ${CONTAINER_NAME}
                          fi
                          docker build -t ${IMAGE_NAME} .
                          CID=$(docker run -d -p 5001:5001 -v /tmp/app:/tmp/app --hostname=${CONTAINER_NAME} --name=${CONTAINER_NAME} ${IMAGE_NAME})
                          echo CONTAINER_ID=${CID}
                          CIP=$(docker inspect --format '{{ .NetworkSettings.IPAddress }}' ${CID})
                          echo CONTAINER_IP=${CIP}
                          echo Increase counter using: curl -X POST "http://${CIP}:5001/"
                          echo Display counter using: curl http://${CIP}:5001/'''
                   
            }
        }
    }

    options {
            timestamps()
    }
}
